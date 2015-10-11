#This file is for emojis. Import emo.py then emo.Eggplant(turtle_name) to try it out!

def Eggplant(t):

	t.color("purple")
	t.fill(True)
	t.forward(30)
	for j in range(5):
		t.left(6)
		t.forward(6)

	t.forward(100)
	t.circle(80, 100)
	for k in range(10):
		t.left(10)
		t.forward(5)
	t.forward(165)

	for y in range(7):
		t.left(5)
		t.forward(6)
	t.forward(8)
	t.fill(False)

	t.color("green")
	t.right(180)
	t.forward(10)

	for x in range (10):
		if x%2 != 0:
			t.fill(True)
			t.forward(20)
			t.left(160)
			t.forward(20)
			t.right(320)
			t.forward(20)
			t.fill(False)
		else:
			t.pu()
			t.forward(20)
			t.left(160)
			t.forward(20)
			t.right(320)
			t.forward(20)
			t.pd()
	t.pu()
	t.forward(10)
	return
