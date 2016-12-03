#!/usr/bin/python3


from getpass import getpass


ans = {  "hi!" : 'Hi too' , "How are yoy"  : 'Fun' , "good bye" : 'See later' }
inp = input ( "HI" )
def get_answer (inp) :
  return  ans.get(inp)

print ( get_answer(inp)) 
