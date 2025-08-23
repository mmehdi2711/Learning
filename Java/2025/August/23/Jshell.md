`````````````````````````````````````````````````````````````````````````````````````````````````````````````````
@heheboyy27 ➜ .../Java/2025/August/23 (main) $ jshell
|  Welcome to JShell -- Version 21.0.7
|  For an introduction type: /help intro

jshell> int a = 10
a ==> 10

jshell> int b = 20
b ==> 20

jshell> int b = 30
b ==> 30

jshell> System.out.printf("%d + %d + %d = %d", a, b, c, a+b+c).println()
|  Error:
|  cannot find symbol
|    symbol:   variable c
|  System.out.printf("%d + %d + %d = %d", a, b, c, a+b+c).println()
|                                               ^
|  Error:
|  cannot find symbol
|    symbol:   variable c
|  System.out.printf("%d + %d + %d = %d", a, b, c, a+b+c).println()
|                                                      ^

jshell> int c = 30
c ==> 30

jshell> System.out.printf("%d + %d + %d = %d", a, b, c, a+b+c).println()
10 + 30 + 30 = 70

jshell> int 

jshell> 

jshell> System.out.printf("%d + %d + %d = %d", a, b, c, a+b+c).println()
10 + 30 + 30 = 70

jshell> int b = 20
b ==> 20

jshell> System.out.printf("%d + %d + %d = %d", a, b, c, a+b+c).println()
10 + 20 + 30 = 60

jshell> a = 50
a ==> 50

jshell> System.out.printf("%d + %d + %d = %d", a, b, c, a+b+c).println()
50 + 20 + 30 = 100

jshell> b = 60
b ==> 60

jshell> System.out.printf("%d + %d + %d = %d", a, b, c, a+b+c).println()
50 + 60 + 30 = 140
```````````````````````````````````````````````````````````````````````````````````````````````````````````````````