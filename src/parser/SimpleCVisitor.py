# Generated from SimpleC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SimpleCParser import SimpleCParser
else:
    from SimpleCParser import SimpleCParser

# This class defines a complete generic visitor for a parse tree produced by SimpleCParser.

class SimpleCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleCParser#program.
    def visitProgram(self, ctx:SimpleCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#includes.
    def visitIncludes(self, ctx:SimpleCParser.IncludesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#include.
    def visitInclude(self, ctx:SimpleCParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#declarations.
    def visitDeclarations(self, ctx:SimpleCParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#declaration.
    def visitDeclaration(self, ctx:SimpleCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:SimpleCParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:SimpleCParser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#functions.
    def visitFunctions(self, ctx:SimpleCParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#function.
    def visitFunction(self, ctx:SimpleCParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#functype.
    def visitFunctype(self, ctx:SimpleCParser.FunctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#parameters.
    def visitParameters(self, ctx:SimpleCParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#parameter.
    def visitParameter(self, ctx:SimpleCParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#funcBody.
    def visitFuncBody(self, ctx:SimpleCParser.FuncBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#body.
    def visitBody(self, ctx:SimpleCParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#block.
    def visitBlock(self, ctx:SimpleCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#assignBlock.
    def visitAssignBlock(self, ctx:SimpleCParser.AssignBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#arrayItem.
    def visitArrayItem(self, ctx:SimpleCParser.ArrayItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#ifBlocks.
    def visitIfBlocks(self, ctx:SimpleCParser.IfBlocksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#ifBlock.
    def visitIfBlock(self, ctx:SimpleCParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#elseIfBlock.
    def visitElseIfBlock(self, ctx:SimpleCParser.ElseIfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#elseBlock.
    def visitElseBlock(self, ctx:SimpleCParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#whileBlock.
    def visitWhileBlock(self, ctx:SimpleCParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#forBlock.
    def visitForBlock(self, ctx:SimpleCParser.ForBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#forInit.
    def visitForInit(self, ctx:SimpleCParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#forUpdate.
    def visitForUpdate(self, ctx:SimpleCParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#returnBlock.
    def visitReturnBlock(self, ctx:SimpleCParser.ReturnBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#condition.
    def visitCondition(self, ctx:SimpleCParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#exprint.
    def visitExprint(self, ctx:SimpleCParser.ExprintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#parens.
    def visitParens(self, ctx:SimpleCParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#exprarrayitem.
    def visitExprarrayitem(self, ctx:SimpleCParser.ExprarrayitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#Or.
    def visitOr(self, ctx:SimpleCParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#MulDiv.
    def visitMulDiv(self, ctx:SimpleCParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#AddSub.
    def visitAddSub(self, ctx:SimpleCParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#exprdouble.
    def visitExprdouble(self, ctx:SimpleCParser.ExprdoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#exprbool.
    def visitExprbool(self, ctx:SimpleCParser.ExprboolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#exprstring.
    def visitExprstring(self, ctx:SimpleCParser.ExprstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#Neg.
    def visitNeg(self, ctx:SimpleCParser.NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#Identifier.
    def visitIdentifier(self, ctx:SimpleCParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#Equal.
    def visitEqual(self, ctx:SimpleCParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#And.
    def visitAnd(self, ctx:SimpleCParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#exprfunction.
    def visitExprfunction(self, ctx:SimpleCParser.ExprfunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#Compare.
    def visitCompare(self, ctx:SimpleCParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#exprchar.
    def visitExprchar(self, ctx:SimpleCParser.ExprcharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#func.
    def visitFunc(self, ctx:SimpleCParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#userFunc.
    def visitUserFunc(self, ctx:SimpleCParser.UserFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#arguments.
    def visitArguments(self, ctx:SimpleCParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#argument.
    def visitArgument(self, ctx:SimpleCParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#standardFunc.
    def visitStandardFunc(self, ctx:SimpleCParser.StandardFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#strlenFunc.
    def visitStrlenFunc(self, ctx:SimpleCParser.StrlenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#printfFunc.
    def visitPrintfFunc(self, ctx:SimpleCParser.PrintfFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#scanfFunc.
    def visitScanfFunc(self, ctx:SimpleCParser.ScanfFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#atoiFunc.
    def visitAtoiFunc(self, ctx:SimpleCParser.AtoiFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#getsFunc.
    def visitGetsFunc(self, ctx:SimpleCParser.GetsFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#type.
    def visitType(self, ctx:SimpleCParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#lib.
    def visitLib(self, ctx:SimpleCParser.LibContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#id.
    def visitId(self, ctx:SimpleCParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#integer.
    def visitInteger(self, ctx:SimpleCParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#double.
    def visitDouble(self, ctx:SimpleCParser.DoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#char.
    def visitChar(self, ctx:SimpleCParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#bool.
    def visitBool(self, ctx:SimpleCParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#string.
    def visitString(self, ctx:SimpleCParser.StringContext):
        return self.visitChildren(ctx)



del SimpleCParser