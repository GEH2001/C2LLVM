; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
entry:
  %"i" = alloca i32
  %"j" = alloca i32
  %"s" = alloca [80 x i8]
  %".2" = getelementptr [23 x i8], [23 x i8]* @".str", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = getelementptr [3 x i8], [3 x i8]* @".str.1", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %".4", [80 x i8]* %"s")
  %"flag" = alloca i32
  store i32 1, i32* %"flag"
  store i32 0, i32* %"i"
  %".8" = getelementptr [80 x i8], [80 x i8]* %"s", i32 0, i32 0
  %".9" = call i32 @"strlen"(i8* %".8")
  %".10" = sub i32 %".9", 1
  store i32 %".10", i32* %"j"
  br label %".12"
.12:
  %".14" = load i32, i32* %"i"
  %".15" = load i32, i32* %"j"
  %".16" = icmp slt i32 %".14", %".15"
  br i1 %".16", label %".17", label %".37"
.17:
  %".19" = load i32, i32* %"i"
  %".20" = getelementptr [80 x i8], [80 x i8]* %"s", i32 0, i32 %".19"
  %".21" = load i8, i8* %".20"
  %".22" = load i32, i32* %"j"
  %".23" = getelementptr [80 x i8], [80 x i8]* %"s", i32 0, i32 %".22"
  %".24" = load i8, i8* %".23"
  %".25" = icmp ne i8 %".21", %".24"
  br i1 %".25", label %".18", label %".27"
.18:
  store i32 0, i32* %"flag"
  br label %".27"
.27:
  %".30" = load i32, i32* %"i"
  %".31" = add i32 %".30", 1
  store i32 %".31", i32* %"i"
  %".33" = load i32, i32* %"j"
  %".34" = sub i32 %".33", 1
  store i32 %".34", i32* %"j"
  br label %".12"
.37:
  %".40" = load i32, i32* %"flag"
  %".41" = icmp ne i32 %".40", 0
  br i1 %".41", label %".39", label %".45"
.39:
  %".42" = getelementptr [6 x i8], [6 x i8]* @".str.2", i32 0, i32 0
  %".43" = load [80 x i8], [80 x i8]* %"s"
  %".44" = call i32 (i8*, ...) @"printf"(i8* %".42", [80 x i8] %".43")
  br label %".50"
.45:
  %".47" = getelementptr [7 x i8], [7 x i8]* @".str.3", i32 0, i32 0
  %".48" = load [80 x i8], [80 x i8]* %"s"
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".47", [80 x i8] %".48")
  br label %".50"
.50:
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@".str" = constant [23 x i8] c"Please type a string:\0a\00"
declare i32 @"scanf"(i8* %".1", ...)

@".str.1" = constant [3 x i8] c"%s\00"
declare i32 @"strlen"(i8* %".1")

@".str.2" = constant [6 x i8] c"True\0a\00"
@".str.3" = constant [7 x i8] c"False\0a\00"