```
# Life Cycle of a Java Program  

A Java program generally goes through **three main stages**:  

1. **Editing the program**  
   - First, you type the program in a text editor (e.g., Notepad, Notepad++, WordPad, TextEdit).  
   - When saving the file, you must use the **`.java` extension**.  
   - By convention, the filename should match the class name.  
     - Example: If the class name is `Sample`, the file should be saved as **`Sample.java`**.  

2. **Compiling the source code**  
   - Java programs are compiled using the **Java compiler (`javac`)**.  
   - The compiler takes the **source file** (e.g., `Sample.java`) as input.  
   - It produces **bytecode** (platform-independent code).  
   - The bytecode is saved in a file with the **`.class` extension**.  
     - Example: `Sample.class`.  

3. **Executing the bytecode**  
   - The **Java Virtual Machine (JVM)** executes the bytecode.  
   - The JVM translates bytecode into **machine code (0s and 1s)**, which the computer’s CPU can understand and run.  

```