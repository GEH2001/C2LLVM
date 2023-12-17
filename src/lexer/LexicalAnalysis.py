from antlr4 import *
from SimpleCLexer import SimpleCLexer
from SimpleCParser import SimpleCParser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-testfile', type=str, default = None)
args = parser.parse_args()

#读取测试文件
with open(args.testfile) as f:
    content = f.read()

# 创建词法和语法分析器
input_stream = InputStream(content)
lexer = SimpleCLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = SimpleCParser(stream)

# 开始解析
tree = parser.program()

# 获取计算结果
for token in stream.getTokens(0,99999999):
    print(token)