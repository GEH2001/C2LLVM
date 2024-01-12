# C to LLVM IR Compiler

## 项目结构
```
C2LLVM
├─ README.md
├─ doc
│    └─ report.md
├─ exe
└─ src
       ├─ .antlr
       ├─ parser    # 语法分析
       │    ├─ .antlr
       │    └─ SimpleC.g4
       └─ test      # 测试文件
              └─ example.c
```

## 语法支持

- 示例代码见`src/test/example.c`
- 源代码必须按照 **头文件->变量声明->函数定义** 的顺序组织
- 数据类型 void int double bool char
- if
- while
- for
- 一维数组
- 单行注释
- 块注释
- 标准库函数`gets strlen printf scanf atoi`

## 不支持
- 结构体
- 单目运算符`++`和`--`
- 不支持中文注释
- break
- continue

## 环境配置

参考[antlr4/doc/getting-started.md](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

- 安装Python 3.11.7

- 安装antlr

  ```bash
  $ pip install antlr-tools
  $ antlr4
  ANTLR tool needs Java to run; install Java JRE 11 yes/no (default yes)? yes
  Installed Java in C:\Users\geh20\.jre\jdk-11.0.21+9-jre; remove that dir to uninstall
  ANTLR Parser Generator  Version 4.13.1
  ...
  ```

- 安装Antlr Python3 runtime

  ```bash
  $ pip install antlr4-python3-runtime==4.13.1
  ```

- 安装llvmlite

  ```bash
  $ pip install llvmlite
  ```

## Usage

进入src目录

```bash
$ pwd
~/src
$ python main.py hello.c	# 生成hello.ll
$ lli hello.ll	# 执行中间代码
```
[!note] 测试时, 请在自己的本地仓库src目录下新建C文件, 命名最好是`hello.c`, 因为我已经在gitignore中设置忽略hello.c和hello.ll, 这样可以保证自己在本地的测试内容不会被提交到GitHub (冗余提交)

## Antlr4命令

语法分析树（文本形式）

```bash
$ antlr4-parse Expr.g4 prog -tree
10+20*30
^Z				# end of input, use ^D in unix
```

打印token流

```bash
$ antlr4-parse Expr.g4 prog -tokens -trace
10+20*30
^Z
```

语法分析树（直观图）

```bash
$ antlr4-parse Expr.g4 prog -gui
10+20*30
^Z
```

生成语法分析代码

```bash
$ antlr4 -visitor -Dlanguage=Python3 Expr.g4
```

## Clang/LLVM

Clang只在unix上支持的比较好，windows上不太行（而且缺少很多工具比如lli）

1. 安装

[LLVM 工具链下载 · GitBook (buaa-se-compiling.github.io)](https://buaa-se-compiling.github.io/miniSysY-tutorial/pre/llvm_download.html)

```bash
$ sudo apt-get install llvm
$ sudo apt-get install clang
```

测试安装是否成功

```bash
$ clang -v # 查看版本，若出现版本信息则说明安装成功
$ lli --version # 查看版本，若出现版本信息则说明安装成功
```

2. 命令行

[LLVM 工具链介绍 · GitBook (buaa-se-compiling.github.io)](https://buaa-se-compiling.github.io/miniSysY-tutorial/pre/llvm_tool_chain.html)

```bash
# 1. 生成 main.c 对应的 .ll 格式的文件
$ clang -S  -emit-llvm main.c -o main.ll -O0

# 2. 用 lli 解释执行生成的 .ll 文件
$ lli main.ll
```

## IR

[LLVM IR 快速上手 · GitBook (buaa-se-compiling.github.io)](https://buaa-se-compiling.github.io/miniSysY-tutorial/pre/llvm_ir_quick_primer.html)

阅读上述内容，理解IR的变量、结构

## llvmlite

llvmlite是一个python包，用于辅助生成LLVM IR

按照我的理解，LLVM提供了完整的库用于辅助生成IR，详细可查看[Getting Started with LLVM Core Libraries（中文版）](https://getting-started-with-llvm-core-libraries-zh-cn.readthedocs.io/zh-cn/latest/index.html)【第5章LLVM中间表示】

llvmlite应该是将其封装为python接口，方便python调用

llvmlite文档: [User guide — llvmlite documentation (pydata.org)](https://llvmlite.pydata.org/en/latest/user-guide/index.html)

阅读 IR Layer 内容，理解Types、Values、Modules、IR Builders

Builder用来生成IR，Values是LLVM IR中用到的所有类（Function、Block）



## Done
符号表, 自定义函数, 变量声明, 赋值语句, ret语句, if语句, while语句, expr表达式求值, 标准库函数printf

## TODO

forBlock

expr : char

expr : string

自定义函数调用: userFunc

标准库函数调用: strlenFunc, scanfFunc, atoiFunc, getsFunc

char : Char ;

bool : Bool ;
