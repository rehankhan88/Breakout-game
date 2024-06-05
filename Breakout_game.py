from ursina import *

app = Ursina()

# Initial movement speed of the ball
dx = 0.05
dy = 0.05

# Initial score and game state
score = 0 
dead = False

# Update function is called every frame
def update():
    global dx, dy, score, dead 
    
    if not dead:  
        # Move the board (paddle) based on user input
        if held_keys['right arrow']:
            board.x += 0.11
        if held_keys['left arrow']:
            board.x -= 0.11
        
        # Move the ball
        ball.x += dx    
        ball.y += dy
    
        # Bounce the ball off the walls
        if ball.x >= 7 or ball.x <= -7:
            dx *= -1
        
        # Check if the ball has fallen off the bottom of the screen
        if ball.y <= -4:
            dead = True
    
        # Check for collisions with other entities
        hit_info = ball.intersects()
        if hit_info.hit:
            dy *= -1  # Reverse the vertical direction of the ball
            if hit_info.entity in boxes:
                destroy(hit_info.entity)  # Destroy the hit box
                score += 1  # Increase score
        
        # Display the current score on the screen
        print_on_screen("Rehan Khan Score: " + str(score), position=(-0.8, 0.5))         
    else:
        # Game over: destroy all entities and display final score
        destroy(board)
        destroy(ball)
        for box in boxes:
            destroy(box)
        print_on_screen("Game Over", position=(-0.05, 0.2)) 
        print_on_screen("Final Score: " + str(score), position=(-0.07, 0.15))

# Create a template box entity
box1 = Entity(model="cube", color=color.cyan, texture="rrrr.jpg", scale=(1, 0.5, 0.5), position=(-10, 4, 0), collider="box")

# Create a grid of boxes
boxes = []
for i in range(6, -7, -1):
    for j in range(1, 7):
        boxes.append(duplicate(box1, x=i, y=j/2 + 0.5, color=color.random_color()))

# Create the paddle (board) entity
board = Entity(model="cube", color=color.orange, texture="brick", scale=(4, 0.5, 0.5), position=(0, -3.5, 0), collider="box")

# Create the ball entity
ball = Entity(model="sphere", color=color.orange, scale=0.5, position=(0, -2, 0), collider="box")

app.run()
