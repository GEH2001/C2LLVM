from antlr4 import *
from llvmlite import ir
from parser.SimpleCParser import SimpleCParser

from parser.SimpleCVisitor import SimpleCVisitor
from parser.SimpleCLexer import SimpleCLexer
from Generator.SymbolTable import SymbolTable
from Generator.ErrorLisenter import SemanticError
from Generator.ErrorLisenter import SyntaxErrorListener

double = ir.DoubleType()
int1 = ir.IntType(1)
int8 = ir.IntType(8)
int32 = ir.IntType(32)
void = ir.VoidType()

class Visitor(SimpleCVisitor):
    """
    
    """
    def __init__(self):
        super(SimpleCVisitor, self).__init__()

        self.Module = ir.Module()
        self.Module.triple = "x86_64-pc-linux-gnu"
        self.Module.data_layout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
        
        # 基本块
        self.Blocks = []

        # 用于emit llvm 语句
        self.Builders = []

        # 符号表
        self.SymbolTable = SymbolTable()

        # 函数表
        self.Funs = {}

        # 常量序号, visitString 需要为字符串常量分配序号
        self.Constants = 0
    
    def save(self, filename):
        """
        输出LLVM IR到文件
        """
        with open(filename, "w") as f:
            # f.write(repr(self.Module))
            f.write(str(self.Module))

    def visitProgram(self, ctx: SimpleCParser.ProgramContext):
        """
        program : includes declarations functions ;
        """
        self.visit(ctx.getChild(0))
        self.visit(ctx.getChild(1))
        self.visit(ctx.getChild(2))

    def visitDeclarations(self, ctx: SimpleCParser.DeclarationsContext):
        """
        declarations : declaration* ;
        """
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return
    
    def visitDeclaration(self, ctx: SimpleCParser.DeclarationContext):
        """
        declaration : variableDeclaration | arrayDeclaration ;
        """
        self.visit(ctx.getChild(0))
        return
    
    def visitVariableDeclaration(self, ctx: SimpleCParser.VariableDeclarationContext):
        """
        // int a;  int a = 3, b = 2, c;
        variableDeclaration : (type) id ('=' expr)?  (',' id ('=' expr)?)* ';
        """
        VariableType = self.visit(ctx.getChild(0))
        len = ctx.getChildCount()
        i = 1
        while i < len:
            id = ctx.getChild(i).getText()
            NewVariable = None
            # 全局变量
            if self.SymbolTable.IsGlobalScope():
                NewVariable = ir.GlobalVariable(self.Module, VariableType, name=id)
                NewVariable.linkage = "internal"
            # 局部变量
            else:
                builder = self.Builders[-1]
                NewVariable = builder.alloca(VariableType, name=id)
            # 插入符号表
            symbol = {"type": VariableType, "name": NewVariable}
            res = self.SymbolTable.AddItem(id, symbol)
            if res["result"] == "failure":  # 变量重复定义
                raise SemanticError(res["msg"], ctx)
            # 初始化赋值
            if ctx.getChild(i + 1).getText() == '=':
                value = self.visit(ctx.getChild(i + 2))
                if self.SymbolTable.IsGlobalScope():
                    NewVariable.initializer = ir.Constant(value['type'], value['name'].constant)
                else:
                    value = self.assignConvert(VariableType, value, ctx)
                    builder = self.Builders[-1]
                    builder.store(value['name'], NewVariable)
                i += 4
            else:
                i += 2
        return


    def visitArrayDeclaration(self, ctx: SimpleCParser.ArrayDeclarationContext):
        """
        // int a[10];
        arrayDeclaration : type id '[' integer ']' ';' ;
        """
        VarType = self.visit(ctx.getChild(0))
        id = ctx.getChild(1).getText()
        arrlen = int(ctx.getChild(3).getText())

        NewVariable = None
        if self.SymbolTable.IsGlobalScope():
            NewVariable = ir.GlobalVariable(self.Module, ir.ArrayType(VarType, arrlen), name=id)
            NewVariable.linkage = "internal"
        else:
            builder = self.Builders[-1]
            NewVariable = builder.alloca(ir.ArrayType(VarType, arrlen), name=id)
        # 插入符号表
        symbol = {"type": ir.ArrayType(VarType, arrlen), "name": NewVariable}
        res = self.SymbolTable.AddItem(id, symbol)
        if res["result"] == "failure":
            raise SemanticError(res["msg"], ctx)
        return

    def visitFunctions(self, ctx: SimpleCParser.FunctionsContext):
        """
        functions : function* ;
        """
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return
    
    def visitFunction(self, ctx: SimpleCParser.FunctionContext):
        """
        function : functype id '(' parameters ')' '{' body '}' ;
        """
        retType = self.visit(ctx.getChild(0))
        # retType : int32
        funcName = ctx.getChild(1).getText()
        funcParams = self.visit(ctx.getChild(3))
        # funcParams : [{"type", int32, "id", "a"}, {"type", int8, "id", "b"}]
        
        # 形参类型
        args = []
        for param in funcParams:
            args.append(param['type'])
        # args : [int32, int8]
        funcType = ir.FunctionType(retType, args)
        function = ir.Function(self.Module, funcType, name=funcName)
        
        # 形参名
        for i in range(len(funcParams)):
            function.args[i].name = funcParams[i]['id']

        if funcName in self.Funs:
            raise SemanticError("函数重复定义", ctx)
        self.Funs[funcName] = function

        block = function.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        self.Blocks.append(block)
        self.Builders.append(builder)

        # 作用域
        self.SymbolTable.EnterScope()

        # 参数load
        for i in range(len(funcParams)):
            newtempt = builder.alloca(funcParams[i]['type'])
            builder.store(function.args[i], newtempt)
            # 插入符号表
            symbol = {"type": funcParams[i]['type'], "name": newtempt}
            res = self.SymbolTable.AddItem(funcParams[i]['id'], symbol)
            if res["result"] == "failure":
                raise SemanticError(res["msg"], ctx)
        
        # 函数体
        self.visit(ctx.getChild(6))
        
        # 退出作用域
        self.SymbolTable.ExitScope()
        self.Builders.pop()
        self.Blocks.pop()
        return

    def visitFunctype(self, ctx: SimpleCParser.FunctypeContext):
        """
        functype : type | 'void' ;
        """
        if ctx.getText() == "void":
            return void
        else:
            return self.visit(ctx.getChild(0))
    
    def visitParameters(self, ctx: SimpleCParser.ParametersContext):
        """
        parameters : parameter (',' parameter)* | ;
        """
        params = []
        if ctx.getChildCount() == 0:
            return params

        i = 0
        while i < ctx.getChildCount():
            params.append(self.visit(ctx.getChild(i)))
            i += 2
        return params
    
    def visitParameter(self, ctx: SimpleCParser.ParameterContext):
        """
        parameter : type id ;
        """
        VarType = self.visit(ctx.getChild(0))
        id = ctx.getChild(1).getText()
        return {"type": VarType, "id": id}
    
    def visitFuncBody(self, ctx: SimpleCParser.FuncBodyContext):
        """
        // 函数体
        funcBody : body returnBlock ;
        """
        # TODO: 这里的EnterScope和ExitScope是否需要？
        self.SymbolTable.EnterScope()
        self.visit(ctx.getChild(0))
        self.visit(ctx.getChild(1))
        self.SymbolTable.ExitScope()
        return
    
    def visitBody(self, ctx: SimpleCParser.BodyContext):
        """
        // body -> block(语句块) or func(函数调用)
        body : (block | func ';')* ;
        """
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
            if self.Blocks[-1].is_terminated:
                break
        return
    
    def visitBlock(self, ctx: SimpleCParser.BlockContext):
        """
        // 语句块：声明语句、赋值语句、if语句、while语句、for语句、return语句
        block : declaration | assignBlock | ifBlocks | whileBlock | forBlock | returnBlock ; // | breakBlock |
        """
        self.visit(ctx.getChild(0))
        return
    
    def visitAssignBlock(self, ctx: SimpleCParser.AssignBlockContext):
        """
        // 赋值语句
        assignBlock : (id | arrayItem) '=' expr ';' ;
        """
        builder = self.Builders[-1]
        lval = self.visit(ctx.getChild(0))  # 左值
        rval = self.visit(ctx.getChild(2))  # 右值
        if lval['type'] != rval['type']:
            # 强制类型转换
            rval = self.assignConvert(lval['type'], rval, ctx)
        builder.store(rval['name'], lval['name'])
        return
    
    def visitArrayItem(self, ctx: SimpleCParser.ArrayItemContext):
        """
        arrayItem : id '[' expr ']' ;
        返回数组元素的 左值, 即指针
        """
        id = ctx.getChild(0).getText()
        builder = self.Builders[-1]
        symbol = self.SymbolTable.GetItem(id)
        if symbol is None:
            raise SemanticError("变量未定义", ctx)
        
        if not isinstance(symbol['type'], ir.ArrayType):
            raise SemanticError("不是数组", ctx)
        
        index = self.visit(ctx.getChild(2))
        if index['type'] != int32:
            raise SemanticError("数组索引类型错误", ctx)
        index = index['name']
        newt = builder.gep(symbol['name'], [ir.Constant(int32, 0), index])
        # symbol['type'] : ir.ArrayType(int32, 10), symbol['type'].element : int32
        return {"type": symbol['type'].element, "name": newt}

    ## ----------------------------------if 语句----------------------------------
    def visitCondition(self, ctx:SimpleCParser.ConditionContext):
        """
        condition : expr ;
        """
        val = self.visit(ctx.getChild(0))
        val = self.toBoolean(val)
        return val


    def visitIfBlocks(self, ctx:SimpleCParser.IfBlocksContext):
        """
        ifBlocks : ifBlock (elseIfBlock)* (elseBlock)? ;
        -----------------------------------------
        下面的讨论我用 `子block` 来描述 ifBlock、elseIfBlock、elseBlock
        子block 里面都有 br label %next 语句
        但是%next是所有子block处理完之后才能确定, 所以采取回填假链的方法
        我用 self.Blocks[-1] 表示 %next
        在 visitElseBlock 里面, 我显示的定义了 %next,
        但是如果没有 elseBlock, self.Blocks[-1] 就是 if/elif 的 falseBlock
        --------------------------------------
        """
        begin = len(self.Blocks)
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        
        end = len(self.Blocks)
        # 假链回填 falselist, %next是self.Blocks[-1]
        for i in range(begin, end - 1):
            builder = self.Builders[i]
            block = self.Blocks[i]
            if not block.is_terminated:
                builder.branch(self.Blocks[-1])
        return
    
    def visitIfBlock(self, ctx:SimpleCParser.IfBlockContext):
        """
        ifBlock : 'if' '(' condition ')' '{' body '}' ;
        -----------------------------------------
            ...         ; 紧跟着上一个block, 不需要新建基本块
            %cond = ...
            br i1 %cond, label %true, label %false
        true:
            ...body...
            br label %next
        false:
            ...
        -----------------------------------------
        """
        self.SymbolTable.EnterScope()
        # if condition 引导2个基本块, true 和 false
        builder = self.Builders[-1]
        trueBlock = builder.append_basic_block()
        # falseBlock = builder.append_basic_block()
        cond = self.visit(ctx.getChild(2))  # visit condition
        # builder.cbranch(cond['name'], trueBlock, falseBlock)
        # trueBlock - body
        self.Blocks.append(trueBlock)
        self.Builders.append(ir.IRBuilder(trueBlock))
        self.visit(ctx.getChild(5))
        # falseBlock
        # visit body 之后才新增 falseBlock 并 cbranch, 因为body里面可能有 if 语句, 这样保证输出的 IR 是顺序的
        falseBlock = builder.append_basic_block()
        builder.cbranch(cond['name'], trueBlock, falseBlock)
        
        self.Blocks.append(falseBlock)
        self.Builders.append(ir.IRBuilder(falseBlock))

        self.SymbolTable.ExitScope()

    def visitElseIfBlock(self, ctx:SimpleCParser.ElseIfBlockContext):
        """
        elseIfBlock : 'else' 'if' '(' condition ')' '{' body '}' ;
        -----------------------------------------
            ...           ; 紧跟着上一个 if 的 falseBlock
            %cond = ...
            br i1 %cond, label %true, label %false
        true:
            ...body...
            br label %next
        false:
            ...
        -----------------------------------------
        """
        self.SymbolTable.EnterScope()
        builder = self.Builders[-1]
        cond = self.visit(ctx.getChild(3))  # visit condition
        trueBlock = builder.append_basic_block()
        # falseBlock = builder.append_basic_block()
        # builder.cbranch(cond['name'], trueBlock, falseBlock)
        
        # trueBlock - body
        self.Blocks.append(trueBlock)
        self.Builders.append(ir.IRBuilder(trueBlock))
        self.visit(ctx.getChild(6))
        # falseBlock
        falseBlock = builder.append_basic_block()
        builder.cbranch(cond['name'], trueBlock, falseBlock)
        self.Blocks.append(falseBlock)
        self.Builders.append(ir.IRBuilder(falseBlock))

        self.SymbolTable.ExitScope()
        return
    
    def visitElseBlock(self, ctx:SimpleCParser.ElseBlockContext):
        """
        elseBlock : 'else' '{' body '}' ;
        -----------------------------------------
            ...      ; 紧跟着上一个 if/elif 的 falseBlock
            ...body...
            br label %next
        next:
        -----------------------------------------
        """
        self.SymbolTable.EnterScope()
        builder = self.Builders[-1]
        self.visit(ctx.getChild(2))
        block = builder.append_basic_block()    # next
        # 可以不用在这里 branch, 因为 visitIfBlocks 会回填假链
        # builder.branch(block)
        self.Blocks.append(block)
        self.Builders.append(ir.IRBuilder(block))
        self.SymbolTable.ExitScope()
        return

    ## ----------------------------------while 语句----------------------------------
    def visitWhileBlock(self, ctx:SimpleCParser.WhileBlockContext):
        """
        whileBlock : 'while' '(' condition ')' '{' body '}' ;
        -----------------------------------------
            ...             ; 紧跟着上一个 block
            br label %begin
        begin:
            %cond = ...
            br i1 %cond, label %true, label %false
        true:
            ...body...
            br label %begin
        false:
            ...
        -----------------------------------------
        """
        self.SymbolTable.EnterScope()

        builder = self.Builders[-1]
        # beginBlock,  while 入口, condition
        beginBlock = builder.append_basic_block()
        builder.branch(beginBlock)
        self.Blocks.append(beginBlock)
        self.Builders.append(ir.IRBuilder(beginBlock))
        beginbuilder = self.Builders[-1]
        cond = self.visit(ctx.getChild(2))  # visit condition
        # trueBlock -> body
        trueBlock = builder.append_basic_block()
        self.Blocks.append(trueBlock)
        self.Builders.append(ir.IRBuilder(trueBlock))
        self.visit(ctx.getChild(5)) # visit body
        self.Builders[-1].branch(beginBlock)    # 回到 while 入口
        # falseBlock
        falseBlock = builder.append_basic_block()
        # 注意beginBuilder 是 beginBlock 的 builder
        beginbuilder.cbranch(cond['name'], trueBlock, falseBlock)
        self.Blocks.append(falseBlock)
        self.Builders.append(ir.IRBuilder(falseBlock))
        
        self.SymbolTable.ExitScope()

    def visitId(self, ctx: SimpleCParser.IdContext):
        """
        id : Identifier ;
        左值: id = 3 
        右值: a = id
        id 可能作为左值或右值, 这里只返回id在符号表中的信息 (左值形式 id 的指针)
        调用者需要根据上下文判断是左值还是右值, 如果是右值, 需要调用 load() 加载
        TODO: 参数 load 用于判断是左值还是右值
        """
        id = ctx.getText()
        symbol = self.SymbolTable.GetItem(id)
        if symbol is None:
            raise SemanticError("变量未定义", ctx)
        return {"type": symbol['type'], "name": symbol['name']}
    
    def visitReturnBlock(self, ctx: SimpleCParser.ReturnBlockContext):
        """
        // return 语句
        returnBlock : 'return' (id | integer)? ';' ;
        """
        builder = self.Builders[-1]
        if ctx.getChildCount() == 2:
            builder.ret_void()
            return
        
        # 判断孩子节点是id还是integer
        child = ctx.getChild(1)
        if isinstance(child, SimpleCParser.IdContext):
            symbol = self.visit(child)
            newt = builder.load(symbol['name'])
            # builder.ret(newt)
            val = {"type": symbol['type'], "name": newt}
            # 根据函数返回值类型进行强制类型转换
            retType = builder.function.return_value.type
            val = self.assignConvert(retType, val, ctx)
            builder.ret(val['name'])
        else:
            value = self.visit(child)
            builder.ret(value['name'])
        return

    def visitInteger(self, ctx: SimpleCParser.IntegerContext):
        """
        integer : Integer ;
        """
        return {"type": int32, "name": ir.Constant(int32, int(ctx.getText()))}
    
    def visitDouble(self, ctx:SimpleCParser.DoubleContext):
        """
        double : Double ;
        """
        return {"type": double, "name": ir.Constant(double, float(ctx.getText()))}

    def visitBool(self, ctx:SimpleCParser.BoolContext):
        """
        bool : Bool ;
        """
        if ctx.getText()=="true":
            return {"type": int1, "name": ir.Constant(int1, True)}
        elif ctx.getText()=="false":
            return {"type": int1, "name": ir.Constant(int1, False)}
    
    def visitType(self, ctx: SimpleCParser.TypeContext):
        """
        type : 'int' | 'bool' | 'double' | 'char' ;
        """
        if ctx.getText() == "int":
            return int32
        elif ctx.getText() == "bool":
            return int1
        elif ctx.getText() == "double":
            return double
        elif ctx.getText() == "char":
            return int8
        else:
            raise SemanticError("类型错误", ctx)
    ## ---------------------------expr--------------------------------
    def visitParens(self, ctx:SimpleCParser.ParensContext):
        """
        expr : '(' expr ')' ;   # parens
        """
        return self.visit(ctx.getChild(1))
    
    def toBoolean(self, val, notFlag=True):
        """
        将val转换为bool类型, 即int1
        val: {"type": int32, "name": "a"}
        """
        builder = self.Builders[-1]
        op = "!=" if notFlag else "=="
        newt = None
        if val['type'] == int8 or val['type'] == int32:
            newt =  builder.icmp_signed(op, val['name'], ir.Constant(val['type'], 0))
            return {"type": int1, "name": newt}
        elif val['type'] == double:
            newt = builder.fcmp_ordered(op, val['name'], ir.Constant(val['type'], 0))
            return {"type": int1, "name": newt}
        else:
            return val
        
    def visitNeg(self, ctx:SimpleCParser.NegContext):
        """
        expr : expr op='!' expr # Neg
        """
        val = self.visit(ctx.getChild(1))
        val = self.toBoolean(val, False)
        return val
    
    def visitAnd(self, ctx:SimpleCParser.AndContext):
        """
        expr : expr op='&&' expr # And
        """
        val1 = self.visit(ctx.getChild(0))
        val2 = self.visit(ctx.getChild(2))
        val1 = self.toBoolean(val1)
        val2 = self.toBoolean(val2)
        builder = self.Builders[-1]
        newt = builder.and_(val1['name'], val2['name'])
        return {"type": int1, "name": newt}
    
    def visitOr(self, ctx:SimpleCParser.OrContext):
        """
        expr : expr op='||' expr
        """
        val1 = self.visit(ctx.getChild(0))
        val2 = self.visit(ctx.getChild(2))
        val1 = self.toBoolean(val1)
        val2 = self.toBoolean(val2)
        builder = self.Builders[-1]
        newt = builder.or_(val1['name'], val2['name'])
        return {"type": int1, "name": newt}

    def convertIIZ(self, val, newType):
        """
        IIZ: interger to integer zero extend
        Zero-extend integer value to integer type typ.
        int1 -> int8
        int1 -> int32
        """
        builder = self.Builders[-1]
        newt = builder.zext(val['name'], newType)
        return {"type": newType, "name": newt}
    def convertIIS(self, val, newType):
        """
        Sign-extend integer value to integer type typ.
        int8 -> int32
        """
        builder = self.Builders[-1]
        newt = builder.sext(val['name'], newType)
        return {"type": newType, "name": newt}
    def convertIFS(self, val, newType):
        """
        IFS: signed interger to float
        Convert signed integer value to floating-point type typ.
        int -> float
        """
        builder = self.Builders[-1]
        newt = builder.sitofp(val['name'], newType)
        return {"type": newType, "name": newt}
    def convertFIS(self, val, newType):
        """
        FIS: float to signed interger
        Convert floating-point value to signed integer type typ.
        float -> int
        """
        builder = self.Builders[-1]
        newt = builder.fptosi(val['name'], newType)
        return {"type": newType, "name": newt}

    def isIntType(self, typ):
        """
        判断typ是否为整型
        """
        # return val['type'] == int1 or val['type'] == int8 or val['type'] == int32
        return hasattr(typ, 'width')

    def assignConvert(self, newType, val, ctx):
        """
        赋值类型转换
        """
        if newType == val['type']:
            return val
        newVal = val
        if self.isIntType(newType) and self.isIntType(val['type']):
            if val['type'] == int1:
                newVal = self.convertIIZ(val, newType)
            elif val['type'].width < newType.width:
                newVal = self.convertIIS(val, newType)
            else:
                raise SemanticError("赋值类型转换错误", ctx)
        elif newType == double and self.isIntType(val['type']):
            newVal = self.convertIFS(val, newType)
        elif self.isIntType(newType) and val['type'] == double:
            newVal = self.convertFIS(val, newType)
        return newVal

    def arithmeticConvert(self, val1, val2, ctx):
        """
        算术运算类型转换
        int8 + int32 -> int32 + int32
        int + float -> float + float
        """
        if val1['type'] == val2['type']:
            return val1, val2
        if self.isIntType(val1['type']) and self.isIntType(val2['type']):
            if val1['type'].width >= val2['type'].width:
                if val2['type'].width == 1:
                    val2 = self.convertIIZ(val2, val1['type'])
                else:
                    val2 = self.convertIIS(val2, val1['type'])
            else:
                if val1['type'].width == 1:
                    val1 = self.convertIIZ(val1, val2['type'])
                else:
                    val1 = self.convertIIS(val1, val2['type'])
        elif val1['type'] == double and self.isIntType(val2['type']):
            val2 = self.convertIFS(val2, val1['type'])
        elif val2['type'] == double and self.isIntType(val1['type']):
            val1 = self.convertIFS(val1, val2['type'])
        else:
            raise SemanticError("类型错误", ctx)
        return val1, val2

    def visitMulDiv(self, ctx:SimpleCParser.MulDivContext):
        """
        expr : expr op=('*' | '/' | '%') expr   # MulDiv
        """
        val1 = self.visit(ctx.getChild(0))
        val2 = self.visit(ctx.getChild(2))
        val1, val2 = self.arithmeticConvert(val1, val2, ctx)
        op = ctx.getChild(1).getText()
        builder = self.Builders[-1]
        newt = None
        if val1['type'] == double:
            if op == '*':
                newt = builder.fmul(val1['name'], val2['name'])
            elif op == '/':
                newt = builder.fdiv(val1['name'], val2['name'])
            elif op == '%':
                raise SemanticError("浮点数不能取余", ctx)
        else:
            if op == '*':
                newt = builder.mul(val1['name'], val2['name'])
            elif op == '/':
                newt = builder.sdiv(val1['name'], val2['name'])
            elif op == '%':
                newt = builder.srem(val1['name'], val2['name'])
        return {"type": val1['type'], "name": newt}

    def visitAddSub(self, ctx:SimpleCParser.AddSubContext):
        """
        expr : expr op=('+' | '-') expr     # AddSub
        """
        val1 = self.visit(ctx.getChild(0))
        val2 = self.visit(ctx.getChild(2))
        val1, val2 = self.arithmeticConvert(val1, val2, ctx)
        op = ctx.getChild(1).getText()
        builder = self.Builders[-1]
        newt = None
        if val1['type'] == double:
            if op == '+':
                newt = builder.fadd(val1['name'], val2['name'])
            elif op == '-':
                newt = builder.fsub(val1['name'], val2['name'])
        else:
            if op == '+':
                newt = builder.add(val1['name'], val2['name'])
            elif op == '-':
                newt = builder.sub(val1['name'], val2['name'])
        return {"type": val1['type'], "name": newt}

    def visitCompare(self, ctx:SimpleCParser.CompareContext):
        """
        expr : expr op=('<' | '>' | '<=' | '>=') expr   # Compare
        """
        val1 = self.visit(ctx.getChild(0))
        val2 = self.visit(ctx.getChild(2))
        val1, val2 = self.arithmeticConvert(val1, val2, ctx)

        builder = self.Builders[-1]
        op = ctx.getChild(1).getText()
        newt = None
        if val1['type'] == double:
            newt = builder.fcmp_ordered(op, val1['name'], val2['name'])
        else:
            newt = builder.icmp_signed(op, val1['name'], val2['name'])
        return {"type": int1, "name": newt}

    def visitEqual(self, ctx:SimpleCParser.EqualContext):
        """
        expr : expr op=('==' | '!=') expr   # Equal
        """
        val1 = self.visit(ctx.getChild(0))
        val2 = self.visit(ctx.getChild(2))
        val1, val2 = self.arithmeticConvert(val1, val2, ctx)

        builder = self.Builders[-1]
        op = ctx.getChild(1).getText()
        newt = None
        if val1['type'] == double:
            newt = builder.fcmp_ordered(op, val1['name'], val2['name'])
        else:
            newt = builder.icmp_signed(op, val1['name'], val2['name'])
        return {"type": int1, "name": newt}

    def visitIdentifier(self, ctx:SimpleCParser.IdentifierContext):
        """
        expr : id ;  # Identifier
        返回 id 的右值
        """
        val = self.visit(ctx.getChild(0))   # visitId 返回的是左值
        builder = self.Builders[-1]
        newt = builder.load(val['name'])
        return {"type": val['type'], "name": newt}

    def visitExprint(self, ctx:SimpleCParser.ExprintContext):
        """
        expr : (op='-')? integer   # Exprint
        """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            val = self.visit(ctx.getChild(1))
            builder = self.Builders[-1]
            newt = builder.neg(val['name'])
            return {"type": val['type'], "name": newt}
    
    def visitExprdouble(self, ctx:SimpleCParser.ExprdoubleContext):
        """
        expr : (op='-')? double        #exprdouble
        """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            val = self.visit(ctx.getChild(1))
            builder = self.Builders[-1]
            newt = builder.fneg(val['name'])
            return {"type": val['type'], "name": newt}
        
    def visitExprarrayitem(self, ctx:SimpleCParser.ExprarrayitemContext):
        """
        expr : arrayItem ;  # exprarrayitem
        返回数组元素的 右值
        """
        val = self.visit(ctx.getChild(0))
        builder = self.Builders[-1]
        newt = builder.load(val['name'])
        return {"type": val['type'], "name": newt}
    
    def visitExprfunction(self, ctx:SimpleCParser.ExprfunctionContext):
        """
        expr : func ;     #exprfunction
        """
        return self.visit(ctx.getChild(0))
    
    def visitFunc(self, ctx:SimpleCParser.FuncContext):
        """
        func : standardFunc | userFunc ;
        """
        return self.visit(ctx.getChild(0))
    
    def visitStandardFunc(self, ctx:SimpleCParser.StandardFuncContext):
        """
        standardFunc : strlenFunc | printfFunc | scanfFunc | atoiFunc | getsFunc ;
        """
        return self.visit(ctx.getChild(0))
    
    def visitPrintfFunc(self, ctx:SimpleCParser.PrintfFuncContext):
        """
        printfFunc : 'printf' '(' string (',' expr)* ')' ;
        """
        printf = None
        if 'printf' in self.Funs:
            printf = self.Funs['printf']
        else:
            printfType = ir.FunctionType(int32, [ir.PointerType(int8)], var_arg=True)
            printf = ir.Function(self.Module, printfType, name="printf")
            self.Funs['printf'] = printf
        
        builder = self.Builders[-1]
        retname = None

        # printf("hello"), 只有一个string参数
        if ctx.getChildCount() == 4:
            strval = self.visit(ctx.getChild(2))    # visit string
            strptr = builder.gep(strval['name'], [ir.Constant(int32, 0), ir.Constant(int32, 0)])
            retname = builder.call(printf, [strptr])
        # print("hello %d", a), 有多个参数
        else:
            strval = self.visit(ctx.getChild(2))
            strptr = builder.gep(strval['name'], [ir.Constant(int32, 0), ir.Constant(int32, 0)])
            args = [strptr]
            for i in range(4, ctx.getChildCount() - 1, 2):
                val = self.visit(ctx.getChild(i))
                args.append(val['name'])
            retname = builder.call(printf, args)
        return {"type": int32, "name": retname}

    def visitString(self, ctx:SimpleCParser.StringContext):
        """
        string : String ;
        常量字符串, 如 "hello"
        返回数组类型 ir.ArrayType(int8, length)
        而不是指针 ir.PointerType(int8) 
        如 {"type": ir.ArrayType(int8, length), "name": ".str.1"}
        """
        if(self.Constants == 0):
            name = ".str"
        else:
            name = ".str." + str(self.Constants)
        self.Constants += 1

        string = ctx.getText().replace('\\n', '\n')  # 替换为转义符
        string = string[1:-1]   # 去除双引号
        string += '\0'      # 添加字符串结束符
        length = len(bytearray(string, 'utf8'))

        retname = ir.GlobalVariable(self.Module, ir.ArrayType(int8, length), name)
        # string.linkage = "internal"
        retname.global_constant = True
        retname.initializer = ir.Constant(ir.ArrayType(int8, length), bytearray(string, 'utf8'))
        # return {"type": ir.PointerType(int8), "name": retname}
        return {"type": ir.ArrayType(int8, length), "name": retname}
        
def generate(inputfile, outputfile):
    """
    生成LLVM IR
    """
    input = FileStream(inputfile)
    lexer = SimpleCLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleCParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(SyntaxErrorListener())
    tree = parser.program()
    visitor = Visitor()
    visitor.visit(tree)
    visitor.save(outputfile)