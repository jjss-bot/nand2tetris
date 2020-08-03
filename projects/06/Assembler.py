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
    
    if cmd == 0:                    # if command == L_COMMAND
        s = x.symbol()
        if not z.contains(s):      
            z.addEntry(s, i_rom)    # Add symbol to SymbolTable
    else:
        i_rom += 1                  # ROM Adrress + 1

    x.advance()


# Second Pass: Now go again through the entire program, and parse each line

# Create file .hack
file = open(argv[1].rstrip('.asm') + '.hack', 'w')      

while (w.hasMoreCommands()):
    
    cmd = w.commandType()
    
    if cmd == 1:                            # if command == A_COMMAND

        s = w.symbol()

        if not s.isdigit():                 # if is symbol

            if z.contains(s):               # if found symbol

                addr = z.GetAddress(s)

            else:
                z.addEntry(s, i_ram)        # Add variable name to SymbolTable
                addr = i_ram
                i_ram += 1                  # RAM Adrress + 1
        else:
            addr = s

        # Write binary A_COMMAND 
        file.write('{:16b}'.format(int(addr)).replace(' ', '0') + '\n')
    
    elif cmd == 2:                          # if command == C_COMMAND
        
        a = w.comp()
        b = w.dest()
        c = w.jump() 

        d = y.comp(a)
        e = y.dest(b)
        f = y.jump(c)

        # Write binary C_COMMAND 
        file.write('111' + d + e +f + '\n')

    w.advance()


file.close()

   




    

