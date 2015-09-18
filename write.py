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

def B(t, size=1):
	return

def C(t, size=1):
	return

def D(t, size=1):
	return

def E(t, size=1):
	return

def F(t, size=1):
	return

def G(t, size=1):
	return

def H(t, size=1):
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

def J(t, size=1):
	return

def K(t, size=1):
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

def M(t, size=1):
	return

def N(t, size=1):
	return

def O(t, size=1):
	return

def P(t, size=1):
	return

def Q(t, size=1):
	return

def R(t, size=1):
	return

def S(t, size=1):
	return

def T(t, size=1):
	return

def U(t, size=1):
	return

def V(t, size=1):
	return

def W(t, size=1):
	return

def X(t, size=1):
	return

def Y(t, size=1):
	return

def Z(t, size=1):
	return

def Zero(t, size=1):
	return

def One(t, size=1):
	return

def Two(t, size=1):
	return

def Three(t, size=1):
	return

def Four(t, size=1):
	return

def Five(t, size=1):
	return

def Six(t, size=1):
	return

def Seven(t, size=1):
	return

def Eight(t, size=1):
	return

def Nine(t, size=1):
	return
