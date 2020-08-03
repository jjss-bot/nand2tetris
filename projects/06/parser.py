import re

#Reads an assembly language command, parses it,
#and provides convenient access to the command’s components
class Parser:
    
    def __init__(self, file_name):
        self.f = open(file_name, 'r')
        self.line = None
        self.command = -1
        self.advance()

    #Reads the next command from the input and makes it the current command. 
    def advance(self):
        while True:

            self.line = self.f.readline().lstrip(' ')
            # skip spaces and comments
            if not self.line.isspace() and not self.line.startswith("//"):
                break

    #Are there more commands in the input?
    def hasMoreCommands(self):
        
        if not self.line:
            return False
            
        else:
            return True

    #Returns the type of the current command
    def commandType(self):
        
        # split comments 
        tmp = self.line.split('//')
        # Ignore comments
        self.instruction = tmp[0].replace(' ', '').replace('\t', '').replace('\n', '')
        
        # L_COMMAND
        if self.instruction.startswith('('):
            self.command = 0    
            return 0

        # A_COMMAND
        elif self.instruction.startswith('@'):
            self.command = 1
            return 1

        # C_COMMAND        
        else:
            self.command = 2
            return 2
    
    #Returns the symbol of the current command when commandType() is  A_COMMAND or L_COMMAND.
    def symbol(self):
       
        if self.command == 0:
            return self.instruction.lstrip('(').rstrip(')')
           
        elif self.command == 1:
            return self.instruction.lstrip('@')
       
        else:
            return None

    #Returns the dest mnemonic in the current C-command 
    def dest(self):
        
        tmp = self.instruction.split('=')
        
        if len(tmp) > 1:
            return tmp[0]
        
        else:
            return 'null'

    #Returns the comp mnemonic in the current C-command 
    def comp(self):
        
        a = self.instruction.split('=')        
        
        if len(a) > 1:
            return a[1]
        
        else:
            b = a[0].split(';')
            return b[0]
    
    #Returns the jump mnemonic in the current C-command
    def jump(self):
        
        a = self.instruction.split('=')        
        
        if len(a) > 1:
            c = a[1].split(';')
        
        else:
            c = a[0].split(';')
        
        if len(c) > 1:
            return c[1]
        
        else:
            return 'null'

    def __del__(self):
        self.f.close()