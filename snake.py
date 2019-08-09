import turtle
import time
import random
delay=0.1
# score
score=0
high_score =0

# set up the screen
wn=turtle.Screen()
wn.title("snake game by aman kaushal")
wn.bgcolor("green")
wn.setup(width =580,height=580)
wn.tracer(0)
#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"
#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
segments=[]
# pen
pen=turtle.Turtle ()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 High Score:0",align="center",font=("courier",24,"normal"))
def go_up():
    if head.direction !='down':
     head.direction ="up"


def go_down():
    if head.direction !="up":
        head.direction = "down"


def go_right():
    if head.direction!="left":
        head.direction = "right"


def go_left():
    if head.direction!="right":
     head.direction = "left"


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety((y+20))
    if head.direction=="down":
        y=head.ycor()
        head.sety((y-20))
    if head.direction=="right":
        x=head.xcor()
        head.setx((x+20))
    if head.direction=="left":
        x=head.xcor()
        head.setx((x-20))
#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left ,"a")
wn.onkeypress(go_right ,"d")

#main game loop
while True:
  wn.update()
  # check for a collision with border
  # if head.xcor() >290 or head.xcor() <-290 or head.ycor()>290 or head.ycor()<-290 :
  #    time.sleep(0.1)
  #    head.goto(0,0)
  #    head.direction ="stop"
  #    for segment in segments:
  #        segment.goto(1000,1000)
  #    segments .clear()
  #    reset the score
  #    score=0
  #    update the score display
     # pen.clear()
     # pen.write(f"Score:{score} High Score:{high_score}", align="center", font=("courier", 24, "normal"))
  if head.xcor()>290:
      a=head.xcor()
      b=head.ycor()
      head.goto(-a,b)
  elif head.xcor()<-290:
      c=head.xcor()
      d=head.ycor()
      head.goto(-c,d)
  elif head.ycor()>290:
      e=head.xcor()
      f=head.ycor()
      head.goto(e,-f)
  elif head.ycor()<-290:
      g=head.xcor()
      h=head.ycor()
      head.goto(g,-h)

  #check for collision with food
  if head.distance(food)<20:
     #move the food to a random position
     x=random.randint(-280,290)
     y=random.randint(-280,280)
     food .goto(x,y)
     #add a segment
     new_segment=turtle .Turtle()
     new_segment .speed(0)
     new_segment.shape("square")
     new_segment.color("grey")
     new_segment.penup()
     segments .append(new_segment )
     delay=delay-0.001
  #    increase the score
     score+=1
     if score> high_score :
         high_score =score
     pen.clear()
     pen.write(f"Score:{score} High Score:{high_score}",align="center", font=("courier",24,"normal") )
     high_score=high_score

  for index in range(len(segments)-1,0,-1):
      x=segments[index-1].xcor()
      y=segments[index -1].ycor()
      segments[index].goto(x,y)
  if len(segments)>0:
      x=head.xcor()
      y=head.ycor()
      segments[0].goto(x,y)
  move()
  # check for head collisions with body segments
  for segment in segments :
      if segment.distance(head)<20:
       time.sleep(0.1)
       head.goto(0,0)
       head.direction ='stop'
       for segment in segments :
           segment .goto(1000,1000)
       segments .clear()

  time.sleep(delay)

wn.mainloop()


