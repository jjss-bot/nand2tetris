// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(START)	// while (true)
    @R0
    M = 0	// R0 = 0
    @SUB1
    D = A	
    @R1
    M = D	// R1 = SET address
    @FILL	// call fill
    0; JMP
(SUB1)    	
    @R0	// return here after call fill
    M = -1	// R0 = -1
(WHILE)	// while (KBD == 0)
    @KBD
    D = M
    @WHILE
    D; JEQ	// goto WHILE
    @SUB2
    D = A
    @R1
    M = D	// R1 = WHILE address
    @FILL	// Call fill
    0; JMP
(SUB2) 	// while (KBD != 0)
    @KBD	// return here after call fill	
    D = M
    @SUB2
    D; JNE	// goto SUB2	
    @START
    0; JMP	// goto START


// Fill the screen with R0 value
(FILL)		// fill(color) 	
    @KBD
    D = A	
    @n
    M = D	// n = 24,579
    @SCREEN
    D = A	
    @i		// i = 16,384
    M = D
(LOOP)  	// for (i < n)
    @n
    D = M
    @i
    D = M - D	// i = n - i
    @R1
    A = M	
    D; JEQ	// if (i == 0) goto address in R1
    @R0
    D = M	
    @i
    A = M	// A = i
    M = D	// M[A] = R0
    @i
    M = M + 1	// i++
    @LOOP
    0; JMP	

    
    

