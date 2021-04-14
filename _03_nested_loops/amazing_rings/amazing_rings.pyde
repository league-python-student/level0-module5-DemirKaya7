"""
Go to the recipe to run the demonstration before starting this program
"""

def setup():
    # Set the size of your sketch to be a rectangle like in the recipe demonstration
    size(800, 600)
    # Call the noFill() command so all the ellipses will be transparent
    noFill()
    
x = 250
y = 550
xSpeed = 0.5
ySpeed = -0.5
leftBounds = 250
rightBounds = 550

def draw():
    global x
    global y
    global xSpeed
    global ySpeed
    global leftBounds
    global rightBounds
    
    background(255, 255, 255)
    # Use a for loop to make the first set of rings that will start in the left half
    # of the window.
    for i in range(30):
        ellipse(x, 300, i*10, i*10)
    # Make this set of rings move across the sketch to the right 
    # Hint: Make two variables, one for x and another for the speed. 
    #       Then increase x by the amount in speed.
    x = x + xSpeed
    
    # When the rings reach the right side of the sketch, reverse the direction so
    # they move.
    # Hint: speed = -speed */
    if x > rightBounds:
        xSpeed = -xSpeed

    
    # When the rings reach the left side of the sketch, reverse the direction again
    if x < leftBounds:
        xSpeed = -xSpeed
        
    # CHALLENGE - to finish the Amazing Rings
     
    # Add another for loop to draw the second set of rings that will start in the
    # right half of the window
        
    # Make this set of rings move in the opposite direction to the other rings
    # These rings must also "bounce" off the sides of the window.
    for i in range(30):
        ellipse(y, 300, i*10, i*10)
    
    y = y + ySpeed
    
    if y < leftBounds:
        ySpeed = -ySpeed
    
    if y > rightBounds:
        ySpeed = - ySpeed
