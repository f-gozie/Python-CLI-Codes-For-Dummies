import turtle

turtle.pencolor('red')  # Set pen color to red
turtle.forward(200)		# Move pen forward 200 units, create bottom of the rectangle
turtle.left(90)			# Turn pen by 90 degrees
turtle.pencolor('blue')	# Change pen color to blue
turtle.forward(150)		# Move pen forward 150 units, create right wall
turtle.left(90)			# Turn pen by 90 degrees
turtle.pencolor("green")# Change pen color to green
turtle.forward(200) 	# Move pen forward to 200 units, create top
turtle.left(90)			# Turn pen by 90 degrees
turtle.pencolor("black")# Change pen color to black
turtle.forward(150)		# Move pen 150 units, create left wall
turtle.hideturtle()		# Make the pen invisible
turtle.exitonclick()	# Wait for user input