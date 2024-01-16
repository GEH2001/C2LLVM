; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
entry:
  %"array" = alloca [100 x i32]
  %"str" = alloca [200 x i8]
  %".2" = getelementptr [49 x i8], [49 x i8]* @".str", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = getelementptr [3 x i8], [3 x i8]* @".str.1", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %".4", [200 x i8]* %"str")
  %"p" = alloca i32
  %"q" = alloca i32
  %"r" = alloca i32
  %"n" = alloca i32
  %"len" = alloca i32
  store i32 0, i32* %"p"
  store i32 0, i32* %"q"
  store i32 0, i32* %"r"
  store i32 0, i32* %"n"
  %".10" = getelementptr [200 x i8], [200 x i8]* %"str", i32 0, i32 0
  %".11" = call i32 @"strlen"(i8* %".10")
  store i32 %".11", i32* %"len"
  %"buf" = alloca [20 x i8]
  br label %".13"
.13:
  %".15" = load i32, i32* %"p"
  %".16" = load i32, i32* %"len"
  %".17" = icmp slt i32 %".15", %".16"
  br i1 %".17", label %".18", label %".115"
.18:
  %".20" = load i32, i32* %"p"
  %".21" = getelementptr [200 x i8], [200 x i8]* %"str", i32 0, i32 %".20"
  %".22" = load i8, i8* %".21"
  %".23" = icmp eq i8 %".22", 44
  br i1 %".23", label %".19", label %".62"
.19:
  store i32 0, i32* %"r"
  br label %".25"
.25:
  %".27" = load i32, i32* %"q"
  %".28" = load i32, i32* %"p"
  %".29" = icmp slt i32 %".27", %".28"
  br i1 %".29", label %".30", label %".44"
.30:
  %".31" = load i32, i32* %"r"
  %".32" = getelementptr [20 x i8], [20 x i8]* %"buf", i32 0, i32 %".31"
  %".33" = load i32, i32* %"q"
  %".34" = getelementptr [200 x i8], [200 x i8]* %"str", i32 0, i32 %".33"
  %".35" = load i8, i8* %".34"
  store i8 %".35", i8* %".32"
  %".37" = load i32, i32* %"r"
  %".38" = add i32 %".37", 1
  store i32 %".38", i32* %"r"
  %".40" = load i32, i32* %"q"
  %".41" = add i32 %".40", 1
  store i32 %".41", i32* %"q"
  br label %".25"
.44:
  %".46" = load i32, i32* %"r"
  %".47" = getelementptr [20 x i8], [20 x i8]* %"buf", i32 0, i32 %".46"
  store i8 0, i8* %".47"
  %".49" = load i32, i32* %"n"
  %".50" = getelementptr [100 x i32], [100 x i32]* %"array", i32 0, i32 %".49"
  %".51" = getelementptr [20 x i8], [20 x i8]* %"buf", i32 0, i32 0
  %".52" = call i32 @"atoi"(i8* %".51")
  store i32 %".52", i32* %".50"
  %".54" = load i32, i32* %"n"
  %".55" = add i32 %".54", 1
  store i32 %".55", i32* %"n"
  %".57" = load i32, i32* %"p"
  %".58" = add i32 %".57", 1
  store i32 %".58", i32* %"p"
  %".60" = load i32, i32* %"p"
  store i32 %".60", i32* %"q"
  br label %".110"
.62:
  %".64" = load i32, i32* %"p"
  %".65" = load i32, i32* %"len"
  %".66" = sub i32 %".65", 1
  %".67" = icmp eq i32 %".64", %".66"
  br i1 %".67", label %".68", label %".105"
.68:
  store i32 0, i32* %"r"
  br label %".70"
.70:
  %".72" = load i32, i32* %"q"
  %".73" = load i32, i32* %"p"
  %".74" = icmp sle i32 %".72", %".73"
  br i1 %".74", label %".75", label %".89"
.75:
  %".76" = load i32, i32* %"r"
  %".77" = getelementptr [20 x i8], [20 x i8]* %"buf", i32 0, i32 %".76"
  %".78" = load i32, i32* %"q"
  %".79" = getelementptr [200 x i8], [200 x i8]* %"str", i32 0, i32 %".78"
  %".80" = load i8, i8* %".79"
  store i8 %".80", i8* %".77"
  %".82" = load i32, i32* %"r"
  %".83" = add i32 %".82", 1
  store i32 %".83", i32* %"r"
  %".85" = load i32, i32* %"q"
  %".86" = add i32 %".85", 1
  store i32 %".86", i32* %"q"
  br label %".70"
.89:
  %".91" = load i32, i32* %"r"
  %".92" = getelementptr [20 x i8], [20 x i8]* %"buf", i32 0, i32 %".91"
  store i8 0, i8* %".92"
  %".94" = load i32, i32* %"n"
  %".95" = getelementptr [100 x i32], [100 x i32]* %"array", i32 0, i32 %".94"
  %".96" = getelementptr [20 x i8], [20 x i8]* %"buf", i32 0, i32 0
  %".97" = call i32 @"atoi"(i8* %".96")
  store i32 %".97", i32* %".95"
  %".99" = load i32, i32* %"n"
  %".100" = add i32 %".99", 1
  store i32 %".100", i32* %"n"
  %".102" = load i32, i32* %"p"
  %".103" = add i32 %".102", 1
  store i32 %".103", i32* %"p"
  br label %".110"
.105:
  %".107" = load i32, i32* %"p"
  %".108" = add i32 %".107", 1
  store i32 %".108", i32* %"p"
  br label %".110"
.110:
  br label %".13"
.115:
  %"i" = alloca i32
  %"j" = alloca i32
  %"temp" = alloca i32
  store i32 1, i32* %"i"
  br label %".118"
.118:
  %".120" = load i32, i32* %"i"
  %".121" = load i32, i32* %"n"
  %".122" = icmp slt i32 %".120", %".121"
  br i1 %".122", label %".123", label %".171"
.123:
  store i32 0, i32* %"j"
  br label %".125"
.125:
  %".127" = load i32, i32* %"j"
  %".128" = load i32, i32* %"n"
  %".129" = load i32, i32* %"i"
  %".130" = sub i32 %".128", %".129"
  %".131" = icmp slt i32 %".127", %".130"
  br i1 %".131", label %".132", label %".165"
.132:
  %".134" = load i32, i32* %"j"
  %".135" = getelementptr [100 x i32], [100 x i32]* %"array", i32 0, i32 %".134"
  %".136" = load i32, i32* %".135"
  %".137" = load i32, i32* %"j"
  %".138" = add i32 %".137", 1
  %".139" = getelementptr [100 x i32], [100 x i32]* %"array", i32 0, i32 %".138"
  %".140" = load i32, i32* %".139"
  %".141" = icmp sgt i32 %".136", %".140"
  br i1 %".141", label %".133", label %".158"
.133:
  %".142" = load i32, i32* %"j"
  %".143" = getelementptr [100 x i32], [100 x i32]* %"array", i32 0, i32 %".142"
  %".144" = load i32, i32* %".143"
  store i32 %".144", i32* %"temp"
  %".146" = load i32, i32* %"j"
  %".147" = getelementptr [100 x i32], [100 x i32]* %"array", i32 0, i32 %".146"
  %".148" = load i32, i32* %"j"
  %".149" = add i32 %".148", 1
  %".150" = getelementptr [100 x i32], [100 x i32]* %"array", i32 0, i32 %".149"
  %".151" = load i32, i32* %".150"
  store i32 %".151", i32* %".147"
  %".153" = load i32, i32* %"j"
  %".154" = add i32 %".153", 1
  %".155" = getelementptr [100 x i32], [100 x i32]* %"array", i32 0, i32 %".154"
  %".156" = load i32, i32* %"temp"
  store i32 %".156", i32* %".155"
  br label %".158"
.158:
  %".161" = load i32, i32* %"j"
  %".162" = add i32 %".161", 1
  store i32 %".162", i32* %"j"
  br label %".125"
.165:
  %".167" = load i32, i32* %"i"
  %".168" = add i32 %".167", 1
  store i32 %".168", i32* %"i"
  br label %".118"
.171:
  store i32 0, i32* %"i"
  br label %".174"
.174:
  %".176" = load i32, i32* %"i"
  %".177" = load i32, i32* %"n"
  %".178" = icmp slt i32 %".176", %".177"
  br i1 %".178", label %".179", label %".199"
.179:
  %".180" = getelementptr [3 x i8], [3 x i8]* @".str.2", i32 0, i32 0
  %".181" = load i32, i32* %"i"
  %".182" = getelementptr [100 x i32], [100 x i32]* %"array", i32 0, i32 %".181"
  %".183" = load i32, i32* %".182"
  %".184" = call i32 (i8*, ...) @"printf"(i8* %".180", i32 %".183")
  %".186" = load i32, i32* %"i"
  %".187" = load i32, i32* %"n"
  %".188" = sub i32 %".187", 1
  %".189" = icmp slt i32 %".186", %".188"
  br i1 %".189", label %".185", label %".192"
.185:
  %".190" = getelementptr [2 x i8], [2 x i8]* @".str.3", i32 0, i32 0
  %".191" = call i32 (i8*, ...) @"printf"(i8* %".190")
  br label %".192"
.192:
  %".195" = load i32, i32* %"i"
  %".196" = add i32 %".195", 1
  store i32 %".196", i32* %"i"
  br label %".174"
.199:
  %".201" = getelementptr [2 x i8], [2 x i8]* @".str.4", i32 0, i32 0
  %".202" = call i32 (i8*, ...) @"printf"(i8* %".201")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@".str" = constant [49 x i8] c"Please type the numbers (separated by a comma):\0a\00"
declare i32 @"scanf"(i8* %".1", ...)

@".str.1" = constant [3 x i8] c"%s\00"
declare i32 @"strlen"(i8* %".1")

declare i32 @"atoi"(i8* %".1")

@".str.2" = constant [3 x i8] c"%d\00"
@".str.3" = constant [2 x i8] c",\00"
@".str.4" = constant [2 x i8] c"\0a\00"