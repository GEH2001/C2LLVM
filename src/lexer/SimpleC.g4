grammar SimpleC;

// ----------------- 语法 -----------------

program : includes declarations functions ;

// ------------头文件----------
includes : include* ;
include : '#include' '<' lib '>' ;


// ----------变量声明----------
declarations : declaration* ;
declaration : variableDeclaration | arrayDeclaration ;

// int a;  int a = 3, b = 2, c;
variableDeclaration : (type) id ('=' expr)?  (',' id ('=' expr)?)* ';' ;
// int a[10];
arrayDeclaration : type id '[' integer ']' ';' ;



// ----------函数定义----------

functions : function* ;
function : functype id '(' parameters ')' '{' body '}' ;
functype : type | 'void' ; 


parameters : parameter (',' parameter)* | ;    // `| ` 表示没有参数
parameter : type id;

// body -> block(语句块) or func(函数调用)
body : (block | func ';')* ;

// 语句块：声明语句、赋值语句、if语句、while语句、for语句、return语句
block : declaration | assignBlock | ifBlocks | whileBlock | forBlock | returnBlock ; // | breakBlock | continueBlock ;

// 赋值语句
assignBlock : (id | arrayItem) '=' expr ';' ;
arrayItem : id '[' expr ']' ;

// if 语句
ifBlocks : ifBlock (elseIfBlock)* (elseBlock)? ;
ifBlock : 'if' '(' condition ')' '{' body '}' ;
elseIfBlock : 'else' 'if' '(' condition ')' '{' body '}' ;
elseBlock : 'else' '{' body '}' ;

// while 语句
whileBlock : 'while' '(' condition ')' '{' body '}' ;

// for 语句
forBlock : 'for' '(' forInit ';' condition ';' forUpdate ')' ('{' body '}' | ';') ;
forInit : id '=' expr (',' forInit)* | ;
forUpdate : id '=' expr (',' forUpdate)* | ;

// return 语句
returnBlock : 'return' (id | integer)? ';' ;

condition : expr ;

expr
    : '(' expr ')'                              #parens
    | expr op='!' expr                          #Neg
    | expr op=( '*' | '/' | '%' ) expr          #MulDiv
    | expr op=( '+' | '-' ) expr                #AddSub
    | expr op=( '>=' | '<=' | '>' | '<' ) expr  #Compare
    | expr op=( '==' | '!=' ) expr              #Equal
    | expr op='&&' expr                         #And
    | expr op='||' expr                         #Or
    | id                                        #Identifier
    | (op='-')? integer                         #exprint
    | (op='-')? float                           #exprfloat
    | char                                      #exprchar
    | bool                                      #exprbool
    | arrayItem                                 #exprarrayitem
    | string                                    #exprstring
    | func                                      #exprfunction
    ;

func : standardFunc | userFunc ;
// 自定义函数
userFunc : id '(' arguments ')' ;
arguments : argument (',' argument)* | ;
argument : id | integer | float | char | bool | string ;
// 标准库函数
standardFunc : strlenFunc | printfFunc | scanfFunc | atoiFunc | getsFunc ;
strlenFunc : 'strlen' '(' id ')' ;
printfFunc : 'printf' '(' string (',' expr)* ')' ;
scanfFunc : 'scanf' '(' string (',' '&'? (id | arrayItem) )* ')' ;
atoiFunc : 'atoi' '(' id ')' ;
getsFunc : 'gets' '(' id ')' ;


type : 'int' | 'bool' | 'float' | 'char' ;

lib : Lib ;

id : Identifier ;

integer : Integer ;
float : Float ;
char : Char ;
bool : Bool ;
string : String ;



// -------------------------- 词法 -------------------------
// 库文件名


// 变量名
Identifier : [a-zA-Z_][0-9A-Za-z_]* ;

// Lib 必须在 Identifier 之后，因为 Lib 也是 Identifier 的一种，
// 如果放在 Identifier 之前，会优先匹配 Lib，导致 Identifier 无法匹配
Lib : [a-zA-Z]+'.h'? ;

// 整数 浮点数 字符 布尔值 字符串
Integer : [0-9]+ ;
Float : [0-9]+'.'[0-9]+ ;
Char : '\'' . '\'' ;
Bool : 'true' | 'false' ;
String : '"' .*? '"' ;

// --skip--
Whitespace
    :   [ \t]+
        -> skip
    ;

Newline
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
    ;

BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;