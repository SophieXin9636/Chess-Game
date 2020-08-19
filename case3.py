#!/usr/bin/python
#coding:utf-8
# Homework 3
# Due: Sunday, June 16th at noon.
# What to submit: a file named <your_student_id>.pa3.py
# Beware: Don't cheat -- you will be caught and fail the class.
# Beware: Don't procrastinate -- you will be busy studying you other classes
#         later next week.
# Beware: Don't not do it. Although not worth as many points as the previous
#         assignment, it is still worth a lot of points.
# Beware: Don't procrastinate -- you will be busy studying for other classes
#         later next week.
# Beware: Don't miss the deadline. Noon is 12:00. It is in the middle of the
#         day not at night.

import PA2a #Notice that I have provided this file.

class board():
    def __init__(self):
        global W, B #___2___
        W={key:value for key,value in zip([(a,b)for a in range(1,3) for b in range(1,9)],"♜♞♝♛♚♝♞♜♟♟♟♟♟♟♟♟")}
        B={key:value for key,value in zip([(a,b)for a in range(7,9) for b in range(1,9)],(piece for piece in W.values()))}

    def __str__(self):
        def DrawRow(r):
            nonlocal s
            for c in range(1,9):
                s+=PA2a.FillInASquare((c+r)%2,pos(r,c).__str__(),(r,c) in W,c)
        s=PA2a.top()
        for r in range(8,0,-1):
            DrawRow(r)
        s+=PA2a.bot()
        return s

#From the above, there are 5 blanks for you to fill in:
# ___1___: This defines the constructor method
# ___2___: This lets W and B be treated as globals
# ___3___: This defines the dictionary named W. The values are the symbols for
#          all of the 16 white pieces (so there are 8 "♟", 2 "♞", etc). The
#          keys are tuples of (x,y) coordinates for the starting positions of
#          these 6 pieces.
#          -In this homework (1,1) is the lower-left corner (ie, a1) and (8,8)
#           is the upper-right corner.
#          -Note that the end of this line is: ,"♜♞♝♛♚♝♞♜♟♟♟♟♟♟♟♟")}. You must
#           use this part precisely as written. You must put you answer on one
#           line. And you cannot use semicolons (;).
#          -Note that white goes at the bottom of the board (with its pieces
#           located from (1,1) to (8,2)).
#          -Note that the knights are next to the rooks (I had misplaced these
#           knights on the previous homework).
#
# ___4___: This defines the dictionary named B for the 16 black pieces. As with
#          ___3___, the end part of the line is given. Here, however, you have
#          to use W as the basis for defining B. So this line can't use any
#          quote or semicolon symbols.
#
# ___5___: Like ___1___, this line lets you write to a nonlocal variable (this
#          time, that variable is "s".
#          Note that this uses some functions from the PA2a.py file that I've
#          provided.
#
# Moving on:

class piece():
    def __init__(self,symbol,color):
        self.symbol=symbol
        self.color=color
        
class pos():
    def __init__(self,x,y): #___6___
        self.__pos = (x,y)
                # This constructor takes 2 passed-in arguments (the x and y
                # coordinates of the position that this object will represent).
                # It then stores these coordinates into a tuple that is named
                # with a private name. As described in ___3___, the orientation
                # is such that (1,1) is in the lower-left of the board.
                            
    def __str__(self):
        if self.__pos in W.keys():
            return W[self.__pos]
        elif self.__pos in B.keys():
            return B[self.__pos]
        else:
            return " "

        #...7... 
                # This method returns a single character. It is the unicode
                # symbol for the type of chess-piece at this board position.
                # If there is no piece here, it returns " ".
                # But consider: How do we know what piece is stored here?
                # The answer is you have to consult the W and B dictionaries.
                # Also, note that I've here said "...7..." instead of "___7___"
                # as a way of indicating that this can go on multiple lines.
                
    def toAset(self):
        return {1} if self.__pos in W.keys() else {2} if self.__pos in B.keys() else set() # return set
        #return {1 if self.__pos in W else 2} # return set
        #return ___8___ # This one expression is complicated, because it uses
                       # the technique of Lecture 12, Slide #4.
                       # Q: What does this method do?
                       # A: It returns {1} if the piece at the position of
                       #    this pos object is white. It returns a {2} if the
                       #    piece is black. It returns an empty set if this 
                       #    position is currently empty.
                       # Q2:Why would we want to do that?
                       # A2:Recall that sets impose a partial order (Lectures
                       #    7&8 Slide #95).
                       #    Well, I want pos to have a partial order too: empty
                       #    positions are Less Than filled ones. And if two
                       #    position have the same color, they will both be
                       #    Less Than Or Equal to (<=) each other.
                       #    Thus two spots are equal if they have the same
                       #    color.
                       #    But the order is partial. Neither Black nor White
                       #    is less than or equal to the other.
                       # Q3:Why would I want to do all of that?
                       # A3:Well, we aren't going to reimplement the previous
                       #    homework. But, if we did, the comparison operators
                       #    would create cleaner code.
                       # Q4:But why do we need toAset()?
                       # A4:We'll compare the toAset answers for different
                       #    positions to determine our comparison answers. 
                       
    def __lt__(self,otherColor):# <
        return self.toAset() < otherColor
    def __le__(self,otherColor):# <=
        return self.toAset() <= otherColor

    def __eq__(self,otherColor):# ==
        return (self.toAset() & otherColor) == (self.toAset() | otherColor)
    def __ne__(self,otherColor):# !=
        return (self.toAset() & otherColor) != (self.toAset() | otherColor)
    def __ge__(self,otherColor):# >=
        return self.toAset() >= otherColor
    def __gt__(self,otherColor):# >
        return self.toAset() > otherColor
    def __contains__(self,otherColor):# in
        return (self.toAset() & otherColor) == (self.toAset() | otherColor)

    #...9... # These methods define the following operators: <, <=, ==, !=, >=,
            # >, and "in".
            # You just use the corresponding set operator.
            # But there is one detail: the color that is passed in (that is,
            # passed in so that it can be compared to the color of the piece
            # at this position) will not be a set, it will be number: either
            # 1 for white, 2 for black, or None for empty.
            # And this detail creates a complication: you can easily turn a 1
            # into a {1} and 2 into a {2}, but {None} is not the empty set.
            # the solution is understand how the subtraction operator works on
            # sets (Lecture 7&8, Slide #94) and to use one (ie, use a '-') to
            # turn {None} into an empty set.
            # Note: You have to think about what you are doing here. In the
            #       end, however, the code to do it is quite short, and is
            #       the same for each of the methods you'll implement here.

    def remove(self):
        if self.__pos in W.keys():
            temp = W[self.__pos]
        elif self.__pos in B.keys():
            temp = B[self.__pos]
        else:
            temp = None

        if(temp == None):
            p = piece(temp,set())
        else: 
            p = piece(temp,self.toAset())

        try:
            del W[self.__pos]
        except:
            try:
                del B[self.__pos]
            except:
                return p
        finally:
            return p

        #...10...: # The idea here is a little odd. We don't remove this pos
                  # object (after all, this object contains nothing but a
                  # coordinate position). No, the thing that we want to remove
                  # is the chess piece at this coordinate position.
                  # We want to remove it from the dictionary that it is in
                  # (which means either W or B.)
                  # But there are some rules:
                  #  1. You have to use "try" and just try removing it from
                  #     the dictionaries without testing first whether it is
                  #     in them.
                  #  2. Before deleting it, save it to a variable.
                  #  3. Return an object belonging to the class "piece" (which
                  #     we've defined above. This object holds the character
                  #     symbol for the chess piece and a color code (1 for
                  #     white, 2 for black).
                  #  4. If there is no piece at this position, return: None.

    def __ilshift__(self,pos_):
        # self.__pos : new position
        #pos__ : class pos object : old position (pos_.__pos)

        # 1.test that this is a legal spot to move to, in the sense that
        # the destination square is either empty or holds a piece of the other color.
        if (self == pos_.toAset()):
            assert False

        # 2. Remove it from its original home 
        p = pos_.remove() # return class piece()
        #print(p)
        # 3. validate that a piece was removed.
        assert pos_.__pos not in W.keys() or pos_.__pos not in B.keys()

        assert len(p.color)

        # 4. Remove any piece already at the position of yourself.
        # Note: The remove method defined above wasn't upset
        # if you tried removing but nothing was there: it just return None

        # 5. Update the position of this moved piece, in either
        pos_.__pos = self.__pos
        if(1 in p.color): # white turn
            if(self.__pos in B.keys()):
                del B[self.__pos]
            W[pos_.__pos] = p.symbol
        else: # black turn
            if(self.__pos in W.keys()):
                del W[self.__pos]
            B[pos_.__pos] = p.symbol

        # 6. Return True if you have just the other side's king. Otherwise, return False.
        #...11...: # This method defines the <<= operator (logical shift left).
                  # We, however, will not use this operator as intended by
                  # Python. For us, "x <<= y" means move the piece at position
                  # "y" to position "x".
                  # Q: And what does such a "move" mean?
                  #    1: Use some of the above-defined operators to test that
                  #       this is a legal spot to move to, in the sense that
                  #       the destination square is either empty or holds a
                  #       piece of the other color.
                  #       Note: You cannot use any "_" symbols in your code.
                  #             Instead use the operators themselves.
                  #       Note: In these comparisons, you are "self".
                  #       Note: If the test fails, assert an error, with the
                  #             FEWEST character necessary.
                  #    2: Remove it from its original home ("y" in the "x<<=y"
                  #       example.)
                  #       Q: And what does such a "remove" mean?
                  #       A: Well, notice that:
                  #           i.  "y" is also a pos object.
                  #           ii. We have define above a remove method for pos
                  #               objects.
                  #           iii.That remove method had returned a value, so
                  #               we'll need to save that returned value when
                  #               we do the remove.
                  #    3: With the FEWEST characters possible, do an assert to
                  #       validate that a piece was removed. (The meaning is
                  #       this code considers it an error to try moving from
                  #       a location that hold nothing that can be moved. (See
                  #       the provided image file for an example of this error
                  #       being triggered.
                  #    4: Remove any piece already at the position of yourself.
                  #       Note: The remove method defined above wasn't upset
                  #       if you tried removing but nothing was there: it just
                  #       returned None.
                  #    5: Update the position of this moved piece, in either
                  #       W or B.
                  #    6: Return True if you have just the other side's king.
                  #       Otherwise, return False.

# The following code initializes the code:
G=board();  print(G)

# The following plays some moves. They are all legal, until the last one.
# See the provide image file for an illustration of the expected output for
# these test. That image also has a discussion of why only the last move
# fails. Further, note that you should test other cases too. For example,
# capturing the king. Note: remember that you can catch the king on the first
# move of the game, because the movement paths aren't tested for legality. 
p=pos(4,5); p<<=pos(2,5); print(G)
p=pos(5,5); p<<=pos(7,5); print(G)
p=pos(3,6); p<<=pos(1,7); print(G)
p=pos(6,4); p<<=pos(7,4); print(G)
p=pos(4,4); p<<=pos(2,4); print(G)
p=pos(4,7); p<<=pos(8,3); print(G)
p=pos(5,5); p<<=pos(4,4); print(G)
p=pos(3,6); p<<=pos(4,7); print(G) # kill the knight
p=pos(3,6); p<<=pos(1,4); print(G)
p=pos(5,5); p<<=pos(6,4); print(G)
p=pos(4,3); p<<=pos(1,6); print(G)
p=pos(6,6); p<<=pos(8,7); print(G)
p=pos(3,2); p<<=pos(3,6); print(G)
p=pos(7,5); p<<=pos(8,4); print(G)
p=pos(3,3); p<<=pos(1,2); print(G)
p=pos(6,3); p<<=pos(7,3); print(G)
p=pos(5,7); p<<=pos(1,3); print(G)
p=pos(5,2); p<<=pos(7,2); print(G)
p=pos(5,2); p<<=pos(3,3); print(G)
p=pos(7,4); p<<=pos(8,2); print(G)
p=pos(8,2); p<<=pos(7,4); print(G) #not an error, for us
p=pos(8,2); p<<=pos(7,4); print(G) #triggers an error
