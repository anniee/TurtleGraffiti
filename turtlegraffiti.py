import turtle

# An art project by Anne Vetto, Edna Cao and Lindsey Simard.
# "Turle Graffiti" is a play on opensource, github hosting and collaboration in code.
# It is reminiscent of juvenile games involving chain-like evolution of words and
# drawings, and highlights its own ephemeral existence when it is inevitably changed or replaced
# by another contributor's work. Like the child's game "Telephone", turtle graffiti will
# begin in one form, and, through time, morph into the visions of the various contributors.
# Interestingly, the systems it plays on (git/github) allows its ephemeral history to persist
# and be viewable.

# Please contribute to "Turtle Graffiti" by changing, destroying, and creating whatever you want!!!

window = turtle.Screen()
Edna = turtle.Turtle()
Anne = turtle.Turtle()
Lindsey = turtle.Turtle()
window.bgcolor("lightgreen")
Anne.color("orange")
Anne.shape("turtle")
Edna.color("hotpink")
Edna.shape("turtle")
Lindsey.color("green")
Lindsey.shape("turtle")
Edna.left(35)
Anne.right(220)
Edna.forward(100)
Anne.forward(100)
def half_heart():
  for i in range(9):
    Edna.left(5)
    Edna.forward(5)
    Edna.left(5)
    Edna.forward(5)
    Edna.left(10)
    Edna.forward(5)
    Edna.left(5)
    Edna.forward(5)
half_heart()
def other_half():
  for i in range(9):
    Anne.right(5)
    Anne.forward(5)
    Anne.right(5)
    Anne.forward(5)
    Anne.right(10)
    Anne.forward(5)
    Anne.right(5)
    Anne.forward(5)
other_half()
def Linds_boogie():
  Lindsey.left(90)
  Lindsey.forward(30)
  for i in range(9):
    Lindsey.right(40)
    Lindsey.forward(30)
    Lindsey.left(80)
    Lindsey.forward(30)
Linds_boogie()

window.exitonclick()