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
    if(c==0): print(P[0]*3, sep="", end="")
    if(c==0): print(GonB+L, sep="", end="")
    if(w): print(WonB,x, sep="", end="") # is white piece
    else: print(DonB,x, sep="", end="") # is dark piece
    
    if(c==7): print(GonB+R)

def Red(x,w,c):    
    if(c==0): print(P[0]*3, sep="", end="")
    if(c==0): print(GonR+L, sep="", end="")
    else: print(RonB+R, sep="", end="")

    if(w): print(WonR,x, sep="", end="") # is white piece
    else: print(DonR,x, sep="", end="") # is dark piece
    
    if(c==7): print(GonR+R+GonB)
    else: print(RonB+L, sep="",end="")


def DrawBoard(B,W):   
    def DrawRow(r,B,W):
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


def DrawABoard(*pos, **chessboard):
	board_list = []
	item = chessboard.items()
	s = ""
	i = 0
	for key, value in item:
		s += value
		if(i % 8 == 7):
			board_list.append(s)
			s = ""
		i+=1
	DrawBoard(board_list, wpos)

############################## HW 3 ##############################

piece = "RNBQK"
file = "abcdefgh"
rank = "12345678"
attack = "x"

board_ref = {'a8':0j,'b8':1j,'c8':2j,'d8':3j,'e8':4j,'f8':5j,'g8':6j,'h8':7j,
'a7':(1+0j),'b7':(1+1j),'c7':(1+2j),'d7':(1+3j),'e7':(1+4j),'f7':(1+5j),'g7':(1+6j),'h7':(1+7j),
'a6':(2+0j),'b6':(2+1j),'c6':(2+2j),'d6':(2+3j),'e6':(2+4j),'f6':(2+5j),'g6':(2+6j),'h6':(2+7j),
'a5':(3+0j),'b5':(3+1j),'c5':(3+2j),'d5':(3+3j),'e5':(3+4j),'f5':(3+5j),'g5':(3+6j),'h5':(3+7j),
'a4':(4+0j),'b4':(4+1j),'c4':(4+2j),'d4':(4+3j),'e4':(4+4j),'f4':(4+5j),'g4':(4+6j),'h4':(4+7j),
'a3':(5+0j),'b3':(5+1j),'c3':(5+2j),'d3':(5+3j),'e3':(5+4j),'f3':(5+5j),'g3':(5+6j),'h3':(5+7j),
'a2':(6+0j),'b2':(6+1j),'c2':(6+2j),'d2':(6+3j),'e2':(6+4j),'f2':(6+5j),'g2':(6+6j),'h2':(6+7j),
'a1':(7+0j),'b1':(7+1j),'c1':(7+2j),'d1':(7+3j),'e1':(7+4j),'f1':(7+5j),'g1':(7+6j),'h1':(7+7j)}

wpos = [complex(a,b) for a in range(6,8) for b in range(8)]

def GetAMove(color, *before_pos, **chessboard):
	# start with white
	if(color == 0):
		# white move
		while(True):
			move = input("Please enter white piece movement: ")
			before_pos = Legal(move, color, **chessboard)
			if(type(before_pos) == tuple): break
	else:
		# black move
		while(True):
			move = input("Please enter black piece movement: ")
			before_pos = Legal(move, color, **chessboard)
			if(type(before_pos) == tuple): break

	size = len(move)
	tup = board_ref[move[size-2:size]]
	new_pos = (int(tup.real), int(tup.imag))
	return (before_pos, new_pos)

def Legal(move, iswhite, **chessboard):
	#print('Enter Legal()')
	if(SyntacticallyLegal(move)): 
		new_pos = SemanticallyLegal(move, iswhite, **chessboard)
		if(type(new_pos) == tuple):
			return new_pos
		else:
			return False
	else: return False

def SyntacticallyLegal(move):
	#print('Enter SyntacticallyLegal()')
	size = len(move)

	if(size < 2): return False

	# check Syntax of position
	if(move[size-2] not in file): return False
	if(move[size-1] not in rank): return False

	# is Pawn
	if(size == 2): return True
	if(size == 3 and move[0] == attack): return True
	if(size == 3 and (move[0] in file or move[0] in rank)): return True
	if(size == 4 and (move[0] in file and move[1] in rank)): return True
	if(size == 5 and (move[0] in file and move[1] in rank) and move[2] in attack): return True 
	# is not piece
	if(move[0] not in piece): return False

	# check attack, e.g. Qh4xe1
	if(size == 6 and move[size-3] != attack): return False
	return True

def SemanticallyLegal(move, color, **chessboard):
	#print('Enter SemanticallyLegal()')
	size = len(move)
	target = move[size-2:size] # move position

	if('x' in move): attack = True
	else: attack = False
	if(color == 0): white_turn = True
	else: white_turn = False

	# attack case: If it is not attack, so the move cannot have piece.
	if(attack == False and chessboard[target] != " "): return False
	if(attack == True  and chessboard[target] == " "): return False
	f, r = target[0], target[1]

	# can not white(black) piece attack white(black) piece
	if(white_turn and chessboard[target] != " " and board_ref[target] in wpos):
		return False
	if(not white_turn and chessboard[target] != " " and board_ref[target] not in wpos):
		return False

	# check Rook
	if('R' in move):
		rook = []
		f_d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # file
		f_index = f_d.index(f)

		# check rank right direction
		for i in range(f_index+1,8):
			Rpos = f_d[i] + r
			if(chessboard[Rpos] != '♜' and chessboard[Rpos] != ' '):
				break # other piece in front of the rook
			# white
			if(chessboard[Rpos] == '♜' and board_ref[Rpos] in wpos):
				if(white_turn): 
					rook.append(Rpos)
					break
			# black
			if(chessboard[Rpos] == '♜' and board_ref[Rpos] not in wpos):
				if(not white_turn): 
					rook.append(Rpos)
					break

		# check rank left direction
		for i in range(0,f_index):
			Rpos = f_d[i] + r
			if(chessboard[Rpos] != '♜' and chessboard[Rpos] != ' '):
				break # other piece in front of the rook
			# white
			if(chessboard[Rpos] == '♜' and board_ref[Rpos] in wpos):
				if(white_turn): 
					rook.append(Rpos)
					break
			# black
			if(chessboard[Rpos] == '♜' and board_ref[Rpos] not in wpos):
				if(not white_turn): 
					rook.append(Rpos)
					break

		# check file up direction
		for rd in range(int(r)+1,9):
			Rpos = f + str(rd)
			if(chessboard[Rpos] != '♜' and chessboard[Rpos] != ' '):
				break # other piece in front of the rook
			# white
			if(chessboard[Rpos] == '♜' and board_ref[Rpos] in wpos):
				if(white_turn): 
					rook.append(Rpos)
					break
			# black
			if(chessboard[Rpos] == '♜' and board_ref[Rpos] not in wpos):
				if(not white_turn): 
					rook.append(Rpos)
					break

		# check file down direction
		for rd in range(int(r)-1,0,-1):
			Rpos = f + str(rd)
			if(chessboard[Rpos] != '♜' and chessboard[Rpos] != ' '):
				break # other piece in front of the rook
			# white
			if(chessboard[Rpos] == '♜' and board_ref[Rpos] in wpos):
				if(white_turn): 
					rook.append(Rpos)
					break
			# black
			if(chessboard[Rpos] == '♜' and board_ref[Rpos] not in wpos):
				if(not white_turn): 
					rook.append(Rpos)
					break
		
		if(len(rook) == 0): return False
		elif(len(rook) == 1):
			tup = board_ref[rook[0]]
			return (int(tup.real), int(tup.imag))
		# ambiguous case
		else:
			if(size == 3 or (size == 4 and attack)):
				print("This move is ambiguous.")
				return False
			else:
				if(size == 4): start = move[1] # file or rank
				elif(size == 5 and not attack): start = move[1:3] # file + rank
				elif(size == 5 and attack): start = move[1] # file or rank
				else: start = move[1:3] # file + rank
				check = 0
				result = ""
				for p in rook:
					if(start in p):
						check += 1
						result = p
				if(check > 1): 
					print("This move is ambiguous.")
					return False
				else:
					tup = board_ref[result]
					return (int(tup.real), int(tup.imag))

	# check kNight, e.g. Nc4, Nxe4, Ndxe4, N2xe4
	if('N' in move):
		# check 8 direction
		knight = []
		# in descending order of preference
		f_d = [2, 2, 1, 1, -1, -1, -2, -2] # file direction
		r_d = [1, -1, 2, -2, 2, -2, 1, -1] # rank direction

		for fd, rd in zip(f_d, r_d):
			Npos = chr(ord(f)+fd)+chr(ord(r)+rd)
			if(Npos[0] not in file or Npos[1] not in rank): continue
			# white
			if(chessboard[Npos] == '♞' and board_ref[Npos] in wpos): 
				if(white_turn): knight.append(Npos)
			# black
			if(chessboard[Npos] == '♞' and board_ref[Npos] not in wpos): 
				if(not white_turn): knight.append(Npos)

		if(len(knight) == 0): return False
		elif(len(knight) == 1):
			tup = board_ref[knight[0]]
			return (int(tup.real), int(tup.imag))
		# ambiguous case
		else:
			if(size == 3 or (size == 4 and attack)):
				print("This move is ambiguous.")
				return False
			else:
				if(size == 4): start = move[1] # file or rank
				elif(size == 5 and not attack): start = move[1:3] # file + rank
				elif(size == 5 and attack): start = move[1] # file or rank
				else: start = move[1:3] # file + rank
				check = 0
				result = ""
				for p in knight:
					if(start in p):
						check += 1
						result = p
				if(check > 1): 
					print("This move is ambiguous.")
					return False
				else:
					tup = board_ref[result]
					return (int(tup.real), int(tup.imag))

	# check Bishop
	if('B' in move):
		bishop = []
		# check 4 oblique direction
		f_d = [1, 1, -1, -1]
		r_d = [1, -1, 1, -1]
		Bpos = target
		i = 0 # index
		while(i < 4):
			Bpos = chr(ord(Bpos[0])+f_d[i])+chr(ord(Bpos[1])+r_d[i])
			if(Bpos == target): continue
			# check out of range
			if(Bpos[0] not in file or Bpos[1] not in rank):
				i += 1
				Bpos = target
				continue
			if(chessboard[Bpos] != '♝' and chessboard[Bpos] != ' '):
				i += 1 # other piece in front of the bishop, change direction
				Bpos = target
				continue
			# white
			if(chessboard[Bpos] == '♝' and board_ref[Bpos] in wpos):
				if(white_turn): bishop.append(Bpos)
			# black
			if(chessboard[Bpos] == '♝' and board_ref[Bpos] not in wpos):
				if(not white_turn): bishop.append(Bpos)

		if(len(bishop) == 0): return False
		elif(len(bishop) == 1):
			tup = board_ref[bishop[0]]
			return (int(tup.real), int(tup.imag))
		# ambiguous case
		else:
			if(size == 3 or (size == 4 and attack)):
				print("This move is ambiguous.")
				return False
			else:
				if(size == 4): start = move[1] # file or rank
				elif(size == 5 and not attack): start = move[1:3] # file + rank
				elif(size == 5 and attack): start = move[1] # file or rank
				else: start = move[1:3] # file + rank
				check = 0
				result = ""
				for p in bishop:
					if(start in p):
						check += 1
						result = p
				if(check > 1): 
					print("This move is ambiguous.")
					return False
				else:
					tup = board_ref[result]
					return (int(tup.real), int(tup.imag))

	# check Queen
	if('Q' in move):
		queen = []
		f_d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # file
		f_index = f_d.index(f)

		# check queen right direction
		for i in range(f_index+1,8):
			Qpos = f_d[i] + r
			if(chessboard[Qpos] != '♛' and chessboard[Qpos] != ' '):
				break # other piece in front of the queen
			# white
			if(chessboard[Qpos] == '♛' and board_ref[Qpos] in wpos):
				if(white_turn): 
					queen.append(Qpos)
					break
			# black
			if(chessboard[Qpos] == '♛' and board_ref[Qpos] not in wpos):
				if(not white_turn): 
					queen.append(Qpos)
					break

		# check queen left direction
		for i in range(0,f_index):
			Qpos = f_d[i] + r
			if(chessboard[Qpos] != '♛' and chessboard[Qpos] != ' '):
				break # other piece in front of the queen
			# white
			if(chessboard[Qpos] == '♛' and board_ref[Qpos] in wpos):
				if(white_turn): 
					queen.append(Qpos)
					break
			# black
			if(chessboard[Qpos] == '♛' and board_ref[Qpos] not in wpos):
				if(not white_turn): 
					queen.append(Qpos)
					break

		# check queen file up direction
		for rd in range(int(r)+1,9):
			Qpos = f + str(rd)
			if(chessboard[Qpos] != '♛' and chessboard[Qpos] != ' '):
				break # other piece in front of the queen
			# white
			if(chessboard[Qpos] == '♛' and board_ref[Qpos] in wpos):
				if(white_turn): 
					queen.append(Qpos)
					break
			# black
			if(chessboard[Qpos] == '♛' and board_ref[Qpos] not in wpos):
				if(not white_turn): 
					queen.append(Qpos)
					break

		# check queen file down direction
		for rd in range(int(r)-1,0,-1):
			Qpos = f + str(rd)
			if(chessboard[Qpos] != '♛' and chessboard[Qpos] != ' '):
				break # other piece in front of the queen
			# white
			if(chessboard[Qpos] == '♛' and board_ref[Qpos] in wpos):
				if(white_turn): 
					queen.append(Qpos)
					break
			# black
			if(chessboard[Qpos] == '♛' and board_ref[Qpos] not in wpos):
				if(not white_turn): 
					queen.append(Qpos)
					break

		# check 4 oblique direction
		Qfd = [1, 1, -1, -1]
		Qrd = [1, -1, 1, -1]
		Qpos = target
		i = 0 # index
		while(i < 4):
			Qpos = chr(ord(Qpos[0])+Qfd[i])+chr(ord(Qpos[1])+Qrd[i])
			if(Qpos == target): continue
			# check out of range
			if(Qpos[0] not in file or Qpos[1] not in rank):
				i += 1
				Qpos = target
				continue
			if(chessboard[Qpos] != '♛' and chessboard[Qpos] != ' '):
				i += 1 # other piece in front of the queen, change direction
				Qpos = target
				continue
			# white
			if(chessboard[Qpos] == '♛' and board_ref[Qpos] in wpos):
				if(white_turn): queen.append(Qpos)
			# black
			if(chessboard[Qpos] == '♛' and board_ref[Qpos] not in wpos):
				if(not white_turn): queen.append(Qpos)
		print(queen)
		if(len(queen) == 0): return False
		elif(len(queen) == 1):
			tup = board_ref[queen[0]]
			return (int(tup.real), int(tup.imag))
		# ambiguous case
		else:
			if(size == 3 or (size == 4 and attack)):
				print("This move is ambiguous.")
				return False
			else:
				if(size == 4): start = move[1] # file or rank
				elif(size == 5 and not attack): start = move[1:3] # file + rank
				elif(size == 5 and attack): start = move[1] # file or rank
				else: start = move[1:3] # file + rank
				check = 0
				result = ""
				for p in queen:
					if(start in p):
						check += 1
						result = p
				if(check > 1): 
					print("This move is ambiguous.")
					return False
				else:
					tup = board_ref[result]
					return (int(tup.real), int(tup.imag))

	# check King
	if('K' in move):
		# check 8 direction
		king = []
		# in descending order of preference
		f_d = [1, 1, 1, 0, 0, -1, -1, -1] # file direction
		r_d = [1, 0, -1 ,1 ,-1, 1, 0, -1] # rank direction
		
		for fd, rd in zip(f_d, r_d):
			Kpos = chr(ord(f)+fd)+chr(ord(r)+rd)
			if(Kpos[0] not in file or Kpos[0] not in rank): continue
			# white
			if(chessboard[Kpos] == '♚' and board_ref[Kpos] in wpos): 
				if(white_turn): king.append(Kpos)
			# black
			if(chessboard[Kpos] == '♚' and board_ref[Kpos] not in wpos): 
				if(not white_turn): king.append(Kpos)

		if(len(king) == 0): return False
		elif(len(king) == 1):
			tup = board_ref[king[0]]
			return (int(tup.real), int(tup.imag))
		# ambiguous case
		else:
			if(size == 3 or (size == 4 and attack)):
				print("This move is ambiguous.")
				return False
			else:
				if(size == 4): start = move[1] # file or rank
				elif(size == 5 and not attack): start = move[1:3] # file + rank
				elif(size == 5 and attack): start = move[1] # file or rank
				else: start = move[1:3] # file + rank
				check = 0
				result = ""
				for p in King:
					if(start in p):
						check += 1
						result = p
				if(check > 1): 
					print("This move is ambiguous.")
					return False
				else:
					tup = board_ref[result]
					return (int(tup.real), int(tup.imag))
	
	# check pawn
	pawn = []
	if(white_turn): # white
		if(attack):
			Ppos = chr(ord(f)+1)+chr(ord(r)-1)
			if(Ppos[0] in file and Ppos[1] in rank and chessboard[Ppos] == '♟'):
				pawn.append(Ppos)
			Ppos = chr(ord(f)-1)+chr(ord(r)-1)
			if(Ppos[0] in file and Ppos[1] in rank and chessboard[Ppos] == '♟'):
				pawn.append(Ppos)
		else: # not attack, just move
			# first move
			if(int(r) - 2 == 2):
				Ppos = chr(ord(f))+chr(ord(r)-2)
				if(Ppos[0] in file and Ppos[1] in rank and chessboard[Ppos] == '♟'):
					pawn.append(Ppos)
				Ppos = chr(ord(f))+chr(ord(r)-1)
				if(Ppos[0] in file and Ppos[1] in rank and chessboard[Ppos] == '♟'):
					pawn.append(Ppos)
			else:
				Ppos = chr(ord(f))+chr(ord(r)-1)
				if(Ppos[0] in file and Ppos[1] in rank and chessboard[Ppos] == '♟'):
					pawn.append(Ppos)
	else: # black
		if(attack):
			Ppos =  chr(ord(f)+1)+chr(ord(r)+1)
			if(Ppos[0] in file and Ppos[1] in rank and chessboard[Ppos] == '♟'):
				pawn.append(Ppos)
			Ppos = chr(ord(f)-1)+chr(ord(r)+1)
			if(Ppos[0] in file and Ppos[1] in rank and chessboard[Ppos] == '♟'):
				pawn.append(Ppos)
		else: # not attack, just move
			# first move
			if(int(r) + 2 == 7):
				Ppos = chr(ord(f))+chr(ord(r)+2)
				if(Ppos[0] in file and Ppos[1] in rank and chessboard[Ppos] == '♟'):
					pawn.append(Ppos)
				Ppos = chr(ord(f))+chr(ord(r)+1)
				if(Ppos[0] in file and Ppos[1] in rank and chessboard[Ppos] == '♟'):
					pawn.append(Ppos)
			else:
				Ppos = chr(ord(f))+chr(ord(r)+1)
				if(Ppos[0] in file and Ppos[1] in rank and chessboard[Ppos] == '♟'):
					pawn.append(Ppos)

	if(len(pawn) == 0):
		return False
	elif(len(pawn) == 1):
		tup = board_ref[pawn[0]]
		return (int(tup.real), int(tup.imag))
	else: # ambiguous case
		if(size == 2 or (size == 3 and attack)):
				print("This move is ambiguous.")
				return False
		else:
			if(size == 3): start = move[0] # file or rank
			elif(size == 4 and not attack): start = move[0:2] # file + rank
			elif(size == 4 and attack): start = move[0] # file or rank
			else: start = move[0:2] # file + rank
			check = 0
			result = ""
			for p in King:
				if(start in p):
					check += 1
					result = p
			if(check > 1): 
				print("This move is ambiguous.")
				return False
			else:
				tup = board_ref[result]
				return (int(tup.real), int(tup.imag))

def PlayGame():
	board= {'a8':'♜', 'b8':'♞', 'c8':'♝', 'd8':'♛', 'e8':'♚', 'f8':'♝', 'g8':'♞', 'h8':'♜',
        'a7':'♟', 'b7':'♟', 'c7':'♟', 'd7':'♟', 'e7':'♟', 'f7':'♟', 'g7':'♟', 'h7':'♟',
        'a6':' ', 'b6':' ', 'c6':' ', 'd6':' ', 'e6':' ', 'f6':' ', 'g6':' ', 'h6':' ',
        'a5':' ', 'b5':' ', 'c5':' ', 'd5':' ', 'e5':' ', 'f5':' ', 'g5':' ', 'h5':' ',
        'a4':' ', 'b4':' ', 'c4':' ', 'd4':' ', 'e4':' ', 'f4':' ', 'g4':' ', 'h4':' ',
        'a3':' ', 'b3':' ', 'c3':' ', 'd3':' ', 'e3':' ', 'f3':' ', 'g3':' ', 'h3':' ',
        'a2':'♟', 'b2':'♟', 'c2':'♟', 'd2':'♟', 'e2':'♟', 'f2':'♟', 'g2':'♟', 'h2':'♟',
        'a1':'♜', 'b1':'♞', 'c1':'♝', 'd1':'♛', 'e1':'♚', 'f1':'♝', 'g1':'♞', 'h1':'♜'}

	switch = 0 # white: 0, black: 1
	while(True):
		DrawABoard(wpos, **board)
		movement = ()
		movement = GetAMove(switch, *movement, **board)

		# update board
		bf = complex(movement[0][0],movement[0][1])
		aft = complex(movement[1][0],movement[1][1])
		for item in board_ref:
			if(board_ref[item] == bf):
				old = item
			if(board_ref[item] == aft):
				new = item

		board[new] = board[old]	
		board[old] = ' '
		if(switch == 0):
			wpos.remove(bf)
			wpos.append(aft)
		if(switch == 1):
			if(aft in wpos):
				wpos.remove(aft)

		switch = 1 - switch
if __name__ == "__main__":
	PlayGame()