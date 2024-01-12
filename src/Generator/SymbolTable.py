
class SymbolTable:
    """
    符号表类
    """

    def __init__(self):

        # Table[i]是一个字典，Table[0] 为全局符号表
        # {
        #     "a" : {"type": "int32", "name" : "%.1"},
        #     "b" : {"type": "int8", "name" : "%.2"},
        # }   # name 为 llvm 中的变量名, a, b 是identifier
        self.Table = [{}]
        self.Scope = 0          # 作用域

    def GetItem(self, id):
        """
        获取符号表中的项
        """
        for i in range(self.Scope, -1, -1):
            if id in self.Table[i]:
                return self.Table[i][id]
        return None

    def AddItem(self, id, symbol):
        """
        添加符号表项
        """
        if id in self.Table[self.Scope]:
            Result = {"result": "failure", "msg": "变量重复定义"}
            return Result
        self.Table[self.Scope][id] = symbol
        return {"result": "success"}
    
    def JudgeExist(self, id):
        """
        判断变量是否存在
        """
        for i in range(self.Scope, -1, -1):
            if id in self.Table[i]:
                return True
        return False
    
    def EnterScope(self):
        """
        进入新的作用域
        """
        self.Table.append({})
        self.Scope += 1
    
    def ExitScope(self):
        """
        退出作用域
        """
        if self.Scope == 0:
            return
        self.Table.pop()
        self.Scope -= 1


    def IsGlobalScope(self):
        """
        判断是否为全局作用域
        """
        return self.Scope == 0