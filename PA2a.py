#!/usr/bin/python
#coding:utf-8
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

def FillInASquare(r,x,w,c):
    s=""
    pcol=[DonB,WonB,DonR,WonR]
    rcol=[GonB,GonB,BonR,GonR]
    if c==1 and r==0:s+="   ▌"
    elif c==1:s+="   "+GonR+"▌"
    elif r: s+=RonB+"▐"
    s+=pcol[w+r+r]+x
    if c!=8 and r == 0: return s
    s+=rcol[(c==8)+r+r]+"▐"+rcol[r+(c<8)]
    if c==8: s+="\n"
    return s

def top():
    return "   "+GonB+"▄"*17+"\n"

def bot():
    return "   "+"▀"*17+GonR[:5]+"\n"
