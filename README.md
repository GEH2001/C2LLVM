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
- 数据类型 void int float bool char
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