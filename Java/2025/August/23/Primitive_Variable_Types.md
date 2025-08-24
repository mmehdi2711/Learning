```
There are many types of Primitive Variables, but the four that are supported by Java are:
1. byte - 8 bits, from -128 to 127
2. short - 16 bits, from -32,000 to 32000
3. int - 32 bits, from -2.1 billion to 2.1 billion
4. long - 64 bits, from -9.2 quintillion, to 9.2 quintillion

There are other types as well, such as:
5. float - numbers that have decimal values, with the same constraints as int
6. double - like float, but with the constrains of long

One thing to note about float and double is that you can have a float value as a double, but once a value is set to a double, it cannot be set back to a float.

7. char - while the other primitive variable types are used to store numbers, the char variable type is used to set a letter.
8. boolean - used to set a true or false value. (must use lowercase true and lowercase false)
```
```
Integer Types:
- byte:
Size: 8-bit (1 byte)
Range: -128 to 127
- short:
Size: 16-bit (2 bytes)
Range: -32,768 to 32,767
- int:
Size: 32-bit (4 bytes)
Range: -2,147,483,648 to 2,147,483,647 (approximately -2^31 to 2^31 - 1)
- long:
Size: 64-bit (8 bytes)
Range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (approximately -2^63 to 2^63 - 1)
Floating-Point Types:
- float:
Size: 32-bit (4 bytes)
Range: Approximately 1.4e-45f to 3.4e+38f (single-precision)
- double:
Size: 64-bit (8 bytes)
Range: Approximately 4.9e-324 to 1.8e+308 (double-precision)
Character Type:
- char:
Size: 16-bit (2 bytes)
Range: 0 to 65,535 (Unicode characters)
Boolean Type:
- boolean: 
Size: Not precisely defined by the JVM, but typically represented as 1 bit or 1 byte.
Range: true or false
```