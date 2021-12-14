from sys import argv
import parser
import code
import symbol

w = parser.Parser(argv[1])
x = parser.Parser(argv[1])
y = code.Code()
z = symbol.SymbolTable()

# ROM and RAM default address
i_rom = 0
i_ram = 16

# First Pass: Go through the entire assembly program, line by line, and build the
# symbol table without generating any code.

while (x.hasMoreCommands()):
    
    cmd = x.commandType()
    # if command == L_COMMAND
    if cmd == 0:                   
        s = x.symbol()
        if not z.contains(s):      
            # Add symbol to SymbolTable
            z.addEntry(s, i_rom)   
    else:
        # ROM Adrress + 1
        i_rom += 1                 

    x.advance()


# Second Pass: Now go again through the entire program, and parse each line

# Create file .hack
file = open(argv[1].rstrip('.asm') + '.hack', 'w')      

while (w.hasMoreCommands()):
    cmd = w.commandType()
    # if command == A_COMMAND
    if cmd == 1:                           
        s = w.symbol()
        # if is symbol
        if not s.isdigit():               
            # if found symbol
            if z.contains(s):              
                addr = z.GetAddress(s)
            else:
                # Add variable name to SymbolTable
                z.addEntry(s, i_ram)        
                addr = i_ram
                # RAM Adrress + 1
                i_ram += 1                  
        else:
            addr = s

        # Write binary A_COMMAND 
        file.write('{:16b}'.format(int(addr)).replace(' ', '0') + '\n')
    
    # if command == C_COMMAND
    elif cmd == 2:                         
        
        a = w.comp()
        b = w.dest()
        c = w.jump() 

        d = y.comp(a)
        e = y.dest(b)
        f = y.jump(c)

        # Write binary C_COMMAND 
        file.write('111' + d + e +f + '\n')

    w.advance()
# Close file .hack
file.close()

   




    

