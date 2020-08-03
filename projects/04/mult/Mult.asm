// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

(START)
    @R2
    M = 0
    @R0	// R0 = 0
    D = M
    @i
    M = D	// i = R0
    
(LOOP)		// while (i > 0)
    @i
    D = M
    @END
    D; JGT	// if (i == 0): goto END

    @R1	
    D = M	// D = R!
    @R2
    M = M + D	// R2 = D + R2
    @i
    M = M - 1  // i--
    @LOOP
    0; JMP	// goto LOOP


(END)		// While (true):
    @END
    0; JMP	// goto END



