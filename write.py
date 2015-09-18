#make it easy to make the turtles write letters
#import write.py then call functions (write.A(Edna) or write.A(Edna, 10))
#size must be > 0
#assumes turtle is oriented pointing towards the direction you want to write

import turtle

def this(characters, t, size=1):
	'''eventually this function will allow you to type a word and it will create it'''
	return



def Space(t, size=1):
	t.pu()
	t.forward(25 * size)
	t.pd()
	return

def between_letters(t, size=1):
	t.pu()
	t.forward(5 * size)
	return

def Exclaim(t, size=1):
	t.pd()
	t.dot(size)
	t.pu()
	t.left(90)
	t.forward(10)
	t.pd()
	t.forward(25 * size)
	t.pu()
	t.left(180)
	t.forward(10 + 25 * size)
	t.left(90)
	between_letters(t, size)
	return

def A():
	return

def B():
	return

def C():
	return

def D():
	return

def E():
	return

def F():
	return

def G():
	return

def H():
	return

def I(t, size=1):
	t.pd()
	t.forward(6.25 * size)
	t.left(90)
	t.forward(25 * size)
	t.right(90)
	t.forward(6.25 * size)
	t.right(180)
	t.pu()
	t.forward(6.25 * size)
	t.pd()
	t.forward(6.25*size)
	t.left(90)
	t.pu()
	t.forward(25 * size)
	t.left(90)
	t.forward(6.25 * size)
	t.pd()
	t.forward(6.25 * size)
	between_letters(t, size)
	return

def J():
	return

def K():
	return

def L(t, size=1):
	t.pu()
	t.left(90)
	t.forward(25 * size)
	t.left(180)
	t.pd()
	t.forward(25 * size)
	t.left(90)
	t.forward(12.5 * size)
	between_letters(t, size)
	return

def M():
	return

def N():
	return

def O():
	return

def P():
	return

def Q():
	return

def R():
	return

def S():
	return

def T():
	return

def U():
	return

def V():
	return

def W():
	return

def X():
	return

def Y():
	return

def Z():
	return

def Zero():
	return

def One():
	return

def Two():
	return

def Three():
	return

def Four():
	return

def Five():
	return

def Six():
	return

def Seven():
	return

def Eight():
	return

def Nine():
	return
