; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

@"cnt" = internal global [10 x i32] undef
define void @"init"(i32 %"n", i32 %"value")
{
entry:
  %".4" = alloca i32
  store i32 %"n", i32* %".4"
  %".6" = alloca i32
  store i32 %"value", i32* %".6"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %".9"
.9:
  %".11" = load i32, i32* %"i"
  %".12" = load i32, i32* %".4"
  %".13" = icmp slt i32 %".11", %".12"
  br i1 %".13", label %".14", label %".26"
.14:
  %".15" = load i32, i32* %"i"
  %".16" = getelementptr [10 x i32], [10 x i32]* @"cnt", i32 0, i32 %".15"
  %".17" = load i32, i32* %".6"
  store i32 %".17", i32* %".16"
  %".19" = load i32, i32* %".6"
  %".20" = add i32 %".19", 1
  store i32 %".20", i32* %".6"
  %".22" = load i32, i32* %"i"
  %".23" = add i32 %".22", 1
  store i32 %".23", i32* %"i"
  br label %".9"
.26:
  ret void
}

define void @"print"(i32 %"n")
{
entry:
  %".3" = alloca i32
  store i32 %"n", i32* %".3"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %".6"
.6:
  %".8" = load i32, i32* %"i"
  %".9" = load i32, i32* %".3"
  %".10" = icmp slt i32 %".8", %".9"
  br i1 %".10", label %".11", label %".21"
.11:
  %".12" = getelementptr [4 x i8], [4 x i8]* @".str", i32 0, i32 0
  %".13" = load i32, i32* %"i"
  %".14" = getelementptr [10 x i32], [10 x i32]* @"cnt", i32 0, i32 %".13"
  %".15" = load i32, i32* %".14"
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".15")
  %".17" = load i32, i32* %"i"
  %".18" = add i32 %".17", 1
  store i32 %".18", i32* %"i"
  br label %".6"
.21:
  %".23" = getelementptr [2 x i8], [2 x i8]* @".str.1", i32 0, i32 0
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@".str" = constant [4 x i8] c"%d \00"
@".str.1" = constant [2 x i8] c"\0a\00"
define i32 @"main"()
{
entry:
  %"n" = alloca i32
  store i32 10, i32* %"n"
  %"value" = alloca i32
  store i32 2, i32* %"value"
  %".4" = load i32, i32* %"n"
  %".5" = load i32, i32* %"value"
  call void @"init"(i32 %".4", i32 %".5")
  %".7" = load i32, i32* %"n"
  call void @"print"(i32 %".7")
  ret i32 0
}
