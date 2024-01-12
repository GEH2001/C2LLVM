from antlr4.error.ErrorListener import ErrorListener


class SemanticError(Exception):
    """
    语义错误
    """
    def __init__(self, msg, ctx=None):
        super().__init__()
        if ctx:
            self.line = ctx.start.line
            self.column = ctx.start.column
        else:
            self.line = 0
            self.column = 0
        self.msg = msg
    
    def __str__(self):
        return "SemanticError: line %d:%d %s" % (self.line, self.column, self.msg)