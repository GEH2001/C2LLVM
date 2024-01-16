# C2LLVM

## 项目简介

A simple compiler: from C to LLVM IR.

## 项目结构

```
C2LLVM
├─ .gitignore
├─ README.md
├─ doc
│    ├─ report.md		# 报告文档
│    └─ report.pdf
├─ exe
│    └─ readme.txt		# 程序执行方式
└─ src
       ├─ Generator	# 中间代码生成器
       │    ├─ ErrorLisenter.py	# 语义错误监听
       │    ├─ SymbolTable.py	# 符号表定义
       │    └─ Visitor.py	# 语义分析，继承自SimpleCVisitor
       ├─ main.py
       ├─ parser	# 除g4文件外，该目录下其他文件均由antlr4自动生成
       │    ├─ SimpleC.g4	# 语法规则文件
       │    ├─ SimpleC.interp
       │    ├─ SimpleC.tokens
       │    ├─ SimpleCLexer.interp
       │    ├─ SimpleCLexer.py
       │    ├─ SimpleCLexer.tokens
       │    ├─ SimpleCListener.py
       │    ├─ SimpleCParser.py
       │    └─ SimpleCVisitor.py
       └─ test	# 测例
            ├─ palindrome.c		# 检测回文
            ├─ palindrome.ll
            ├─ sort.c			# 排序
            ├─ sort.ll
            ├─ userfunc.c		# 用于展示对自定义函数的支持
            └─ userfunc.ll
```

## 环境配置

- 系统：Ubuntu 22.04.3 LTS

- 语言：Python 3.11.7

- 安装antlr4，antlr4-python3-runtime，llvmlite

  ```bash
  # 1.安装altlr4
  $ pip install antlr-tools
  $ antlr4	# 执行此命令会自动检查并安装antlr4运行所需要的Java环境
  ...
  # 2.安装antlr4-python3-runtime
  $ pip antlr4-python3-runtime
  # 3.安装llvmlite
  $ pip install llvmlite
  ```

- 安装clang/llvm

  ```bash
  $ sudo apt-get install llvm
  $ sudo apt-get install clang
  ```

## 使用说明

以下命令均运行在`src`目录下

- 生成某个源代码的IR

  ```bash
  $ pwd
  ~/C2LLVM/src
  $ python main.py test/xxx.c		# 在xxx.c同级目录下生成xxx.ll
  ```

- 执行IR

  ```bash
  $ lli xxx.ll
  ```

测例使用方法：

* palindrome.c 用于检测输入的字符串是否为回文，输出 `True` 或 `False`
* sort.c 用于排序，输入是用英文逗号分隔的若干个整数，将它们按照从小到大的顺序排序后重新输出。例如：输入 `5,8,4,9`，输出 `4,5,8,9`
* userfunc.c 用于展示对自定义函数的支持，用户无须输入，输出是 `2 3 4 5 6 7 8 9 10 11`

## 参考资料

- [User guide — llvmlite documentation (pydata.org)](https://llvmlite.pydata.org/en/latest/user-guide/index.html)

  llvmlite文档，通过它查询LLVM接口的使用方式

- [LLVM 相关内容 · GitBook (buaa-se-compiling.github.io)](https://buaa-se-compiling.github.io/miniSysY-tutorial/pre/llvm.html)

  miniSysY编译实验，介绍了LLVM工具链、LLVM IR，对本项目很有帮助

- [antlr4/doc at dev · antlr/antlr4 (github.com)](https://github.com/antlr/antlr4/tree/dev/doc)

  antlr4官方文档，get-started.md 有如何配置antlr4环境，python-target.md 有如何生成python代码的语法分析工具

- [SerCharles/CToLLVMCompiler: A compiler (github.com)](https://github.com/SerCharles/CToLLVMCompiler)

  一个学长实现的代码，我主要参考了这个

- [Getting Started with LLVM Core Libraries（中文版）](https://getting-started-with-llvm-core-libraries-zh-cn.readthedocs.io/zh-cn/latest/index.html)

  LLVM核心库介绍，本次项目没怎么参考，但是对深入理解LLVM有用处

- [The LLVM Compiler Infrastructure Project](https://llvm.org/)

  LLVM官网，没参考

- [TinyCompiler: c compiler based on flex(lex), bison(yacc) and LLVM](https://github.com/stardust95/TinyCompiler)

  比较好的一个简易C编译器，但是词法分析和语法分析基于flex和bison，而本项目使用的是antlr4，所以没怎么参考

- [flosacca/c-compiler: Compile C to LLVM with Python. (github.com)](https://github.com/flosacca/c-compiler/tree/master)

  也是GitHub上找到的一个貌似学长的作业，但是它的语法规则是直接从antlr4官网复制来的，我觉得太冗余了，所以也没参考

