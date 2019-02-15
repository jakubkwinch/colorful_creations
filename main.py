from turtle import *

screen = Screen()
screen.setup(400,400)

colors = {
  'veryblack': '#191919',
  'reallyred': '#CA3E3E'
}

screen.bgcolor(colors['veryblack'])

color(colors['reallyred'])
style = ('Arial', 48, 'bold')
write('Hello, World', font=style, align='center')
hideturtle()
