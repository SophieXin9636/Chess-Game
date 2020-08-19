# In this file, fill in the ... parts with lines of code. Do not
# create new functions.

from random import seed, randrange
P=" ♟♜♝♞♛♚"; L,R,BL,TL="▌▐▄▀"
BonR=WonR=WonB=DonR=DonB=RonB=GonR=GonB=RonG='\033[1;m\033['
WonR+='7;31;47m' # For drawing a white piece on a red background
WonB+='7;30;47m' # For drawing a white piece on a black background
DonR+='2;37;41m' # For drawing a dark piece on a red background
DonB+='2;37;40m' # For drawing a dark piece on a black background
GonR+='2;33;41m' # For drawing gold on a red background
GonB+='2;33;40m' # For drawing gold on a black background
RonG+='2;31;43m' # For drawing red on a gold background
RonB+='7;30;41m' # For drawing red on a black background
BonR+='0;30;41m' # For drawing black on a red background

def Black(x,w,c):
    """A function to print a chess piece on a black background.
        Inputs:
         x: A single-character string indicating the value to put in
            this square. It will be one of the following: " ", "♟",
            "♜", "♝", "♞", "♛", or "♚". (Note that " " is one of the
            options, and is used for empty squares.)
         w: A boolean value indicating whether this is a white piece.
         c: An integer indicating the column of this square. (We need
            to know this because the leftmost square (c=0) has gold 
            on the left side, and the rightmost square (c=7) has gold
            on the right side.

       Outputs: (Done)
       -To begin, in the one case that c=0, 3 spaces are printed. 
       -Next, regardless of c's value, the one character passed in
        as x is printed, in the indicated color.
       -Finally, in the one case that c=7, a newline character is 
        printed.                                                  """
    
    if(c==0): print(P[0]*3, sep="", end="")
    if(c==0): print(GonB+L, sep="", end="")
    if(w): print(WonB,x, sep="", end="") # is white piece
    else: print(DonB,x, sep="", end="") # is dark piece
    
    if(c==7): print(GonB+R)

def Red(x,w,c):
    """A function to print a chess piece on a red background.
        Inputs: These are the same as the inputs for Black()
         x: A string indicating the value to put in this square. 
         w: A boolean value indicating whether this is a white piece.
         c: An integer indicating the column of this square. 

       Outputs:
       -To begin, in the one case that c=0, 3 spaces are printed. 
       -Next, regardless of c's value, three characters always print:
         1: A "▐" character that is red on its right side, and that 
            is either gold (if c=0) or black (otherwise) on its left
            side. (Done)
         2: The character passed in as x, in the indicated color.
         3: A "▌" character that is red on its left side and that is
            either gold (if c=7) or black (otherwise) on its right
            side. (Done)
       -Finally, in the one case that c=7, a newline is printed.
        But somethings needs to be understood here. First, you don't 
        really need to print a "\n", you can just NOT use an "end=''"
        when printing this last "▌" piece. Second, you also need to 
        change the color to GonB before going to the next line, to 
        prevent colored bars from drawing on the left.            """
    
    if(c==0): print(P[0]*3, sep="", end="")

    if(c==0): print(GonR+L, sep="", end="")
    else: print(RonB+R, sep="", end="")

    if(w): print(WonR,x, sep="", end="") # is white piece
    else: print(DonR,x, sep="", end="") # is dark piece
    
    if(c==7): print(GonR+R+GonB)
    else: print(RonB+L, sep="",end="")


def DrawBoard(B,W):
    """A function to draw a chess board with its pieces.
        Inputs:
         B: This is the board. It must be a list of 8 strings, which
            indicate the 8 rows of the chessboard. The 8 strings are
            each 8 characters wide, indicating the 8 rows of the
            chessboard. The individual characters in the strings are
            any of the following: " ","♟","♜","♝","♞","♛", or "♚".
         W: This is a list of 16 complex numbers. Each number encodes
            the row/column position of one of the 16 white pieces.
            (We don't need a similar list of dark pieces, because
            anything that is not white can print as dark.

       Outputs:
        The output is to print the eight rows of the board, along 
        with two more rows for the top and bottom gold border.    """
    
    def DrawRow(r,B,W):
        """A function to draw a single row of the chess board.
           Input:
            r: An integer indicating the row number.
            B: This is the board.
            W: This is a list of white piece locations.

           Outputs:
            The output is the printing of the indicated row.      """
        for c in range(8):
            if complex(r,c) in W: 
                w = True
            else:
                w = False

            i = B[c]
            if(r % 2 == 0):
                if(c % 2 == 0): Black(i,w,c)
                else: Red(i,w,c)
            else:
                if(c % 2 == 0): Red(i,w,c)
                else: Black(i,w,c)

    print(GonB+P[0]*3+BL*17, sep="")

    for i in range(8):
        DrawRow(i,B[i],W)
    
    print(GonB+P[0]*3+TL*17+'\n', sep="")


def DrawAnInitialBoard():
    """A function to create and draw an initial board. This means the
       board is: ["♜♝♞♛♚♞♝♜","♟♟♟♟♟♟♟♟","        ","        ",
                  "        ","        ","♟♟♟♟♟♟♟♟","♜♝♞♛♚♞♝♜"].
       and it also means that the white pieces are in the last two 
       rows.                                """
    
    board=[P[2::1]+P[4:1:-1], P[1]*8, P[0]*8, P[0]*8,
           P[0]*8, P[0]*8, P[1]*8, P[2::1]+P[4:1:-1]]
    pos = [complex(a,b) for a in range(2) for b in range(8)]
    DrawBoard(board, pos)
DrawAnInitialBoard()
    
def DrawRandomBoard():
    """A function to create and draw a board with all 32 pieces in
       random positions.                                         """
    def RandomPlacement(color,otherColor):
        """A function to randomly place the 16 pieces of one color.
            Inputs:
             color: An empty list that we'll add these 16 pieces to. 
             otherColor: The list for the other color. (This list 
                         will be empty on the first call and full on
                         the second call.)

            Outputs:
             The color list will now contain 16 complex numbers, to
             indicate the row/column positions of these pieces. 
             These numbers must be unique, occurring only once in
             either color or otherColor.                          """
        
        # put 16 piece in color
        i = 0
        while i<16:
            a,b = randrange(0,8,1), randrange(0,8,1)
            if (complex(a,b) not in otherColor) and (complex(a,b) not in color):
                color.append(complex(a,b))
                i+=1


    #seed(0) # Comment this line to make it run differently each time    
    W=[];D=[];B=[] #This B object is the board. // W: White , D: Dark
    RandomPlacement(W, D)
    RandomPlacement(D, W)
    # Now that we know where the pieces go, we need to create the
    # eight rows of the board, inserting pieces into those spots.
    # Here, it does not matter how you decide to map the 16 pieces
    # of each color to the 16 positions in the W or D lists.
    
    # create 16 pieces
    Wpiece = [P[1] for i in range(8)]
    for i in range(2):
        Wpiece += P[2], P[3], P[4]
    Wpiece += P[5], P[6]
    Dpiece = Wpiece.copy()

    s = []
    for i in range(8):
        for j in range(8):
            if(complex(i,j) in W):
                wl = len(Wpiece)
                if(wl):
                    w = randrange(0,wl)
                    s+=Wpiece[w]
                    del(Wpiece[w])
                else:
                    Wpiece.pop()
            elif(complex(i,j) in D):
                dl = len(Dpiece)
                if(dl): 
                    d = randrange(0,dl)
                    s+=Dpiece[d]
                    del(Dpiece[d])
                else:
                    Dpiece.pop()
            else:
                s+=" "
        if(j == 7):
            newstr = ''.join(s)
            B.append(newstr) # add pieces
            s = ""

    DrawBoard(B,W)
DrawRandomBoard()