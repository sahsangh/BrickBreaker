from processing import *
r = 0
g = 0
b = 0
leng = 450
width = 400
count = 0
score = 0
brickList = []
levels = []
currentLevel = 0
gamePlay = False
def level1():
    bricks = []
    for row in range(3):
        for col in range(5):
            brick  = {'x': col *90 +15, 'y' : row * 40 + 40, 'w' : 60, 'h' : 20, 'color' : [18, 24, 255]}
            bricks.append(brick)
    levels.append(bricks)
def level2():
    bricks = []
    for r in range(4):
        start = 190 - 60*r
        for n in range(r+1):
            brick  = {'x': start+120*n,'y' : 30+50*r, 'w' : 60, 'h' : 20, 'color' : [213, 24, 88]}
            bricks.append(brick)
    levels.append(bricks)
def level3():
    bricks = []
    for r in range(5):
        start = 0 + 100*r
        for n in range(5-r):
            brick  = {'x': start+100*n,'y' : 30+50*r, 'w' : 60, 'h' : 20, 'color' : [88, 24, 88]}
            bricks.append(brick)
    levels.append(bricks)
def level4():
    bricks = []
    for r in range(5):
        start = 0 + 50*r
        for n in range(5-r):
            brick  = {'x': start+100*n,'y' : 30+30*r, 'w' : 60, 'h' : 20, 'color' : [0, 99, 254]}
            bricks.append(brick)
    levels.append(bricks)
def level5():
    bricks = []
    for r in range(3):
        start = 0 + 44*r
        for n in range(4):
            brick  = {'x': start+100*n,'y' : 30+30*r, 'w' : 60, 'h' : 20, 'color' : [15, 88, 150]}
            bricks.append(brick)
    levels.append(bricks)
ball = {'x': 25 , 'y':25, 'r' : 8, 'velX': 5,'velY':5}
paddle = { "x" : 225, 'y':370, 'l':150, 'w':20, 'move' : 0}
def setup():
    global brickList
    size(leng,width)
    background(r,g,b)
    level5()
    level1()
    level2()
    level3()
    level4()

    brickList = levels[currentLevel]

def draw():
    global brickList, gamePlay, currentLevel
    background(r,g,b)
    drawBricks()
    stroke (255, 255 ,255)
    fill (255, 255, 255)
    ellipse(ball['x'], ball['y'] ,ball['r']*2, ball['r']*2)
    moveBall(ball)
    rect(paddle['x'], paddle['y'], paddle['l'], paddle['w'])
    movePaddle()
    brickCollision()
    textSize(15)
    text("Level: " + str(currentLevel + 1), 200, 20)
    text("Score: " + str(score), 20 ,20)
    if gamePlay == False:
        textSize(50)
        text("Press Space to play", 0, 250)
    if len(brickList) == 0:
        if currentLevel < 4:
            currentLevel +=1 
            brickList = levels[currentLevel]
            gamePlay = False
        else :
            fill(0, 255,0)
            textSize(50)
            text("You Win", 100, 250)
            exitp()

def moveBall(x):
    if gamePlay == True:
        x['x'] += x['velX']
        x['y'] += x['velY']
    if gamePlay == False:
        ball['x'] = paddle['x']+ paddle['l']/2
        ball['y'] = paddle ['y'] - ball ['r'] - 5
    if x['x'] > leng-x['r'] or x['x'] < 0 + x['r']:
        x['velX'] = - x['velX']
    if ball['x'] > paddle['x'] and ball['x'] < paddle['x'] + paddle['l']:
        if ball['y'] + ball['r'] >= paddle['y'] and ball['y'] + ball['r'] < paddle['y'] + ball['velY']:
            ball['velY'] = - ball['velY']
    if  x['y'] < 0 + x['r']:
        x['velY'] = - x['velY']

    if ball['y'] + ball ['r'] > width:
        textSize(50)
        text("Game Over", 100, 200)
        exitp()
def drawBricks():
    for brick in brickList:
        r = brick['color'][0]
        g = brick['color'][1]
        b = brick['color'][2]
        fill (r,g,b)
        stroke(r,g,b)
        rect(brick['x'], brick['y'], brick['w'], brick['h'])
def movePaddle():
    paddle['x'] += paddle['move']
    if paddle['x'] < 0:
        paddle['x'] = 0
    if paddle['x'] + paddle['l'] > leng:
        paddle['x'] = leng - paddle['l']
def keyPressed():
    global gamePlay
    if keyboard.keyCode == LEFT and paddle['x'] > 0:
        paddle['move'] = -5
    if keyboard.keyCode == RIGHT and paddle['x'] < 350:
        paddle['move'] = 5
    if keyboard.keyCode == 32:
        gamePlay = True
def keyReleased():
        if keyboard.keyCode == LEFT or keyboard.keyCode == RIGHT:
            paddle['move'] = 0
def brickCollision():
    global score
    removeIndex = None
    for i in range(len(brickList)):
        brick = brickList[i]
        brickTop = brick['y']
        brickBottom = brick['y'] + brick['h']
        brickLeft = brick['x']
        brickRight = brick['x'] + brick['w']
        ballTop = ball['y'] - ball['r']
        ballBottom = ball['y'] + ball['r']
        ballLeft = ball['x'] - ball['r']
        ballRight = ball['x'] + ball['r']
        
        if ball['x'] > brickLeft and ball['x'] < brickRight:
            if ball['velY'] < 0:
                if ballTop <= brickBottom and ball['y'] > brickTop:
                    ball['velY'] = -ball['velY']
                    removeIndex = i
                    score += 1 
                    break
            if ball['velY'] > 0:
                if ballBottom >= brickTop and ball['y'] < brickBottom:
                    ball['velY'] = -ball['velY']
                    removeIndex = i
                    score += 1 
                    break
        if ball['y'] > brickTop and ball['y'] < brickBottom:
            if ball['velX'] > 0  and ball['x'] < brickRight:
                if ballRight >= brickLeft:
                    ball['velX'] = -ball['velX']
                    removeIndex = i
                    score += 1 
                    break  
            if ball['velX'] < 0 and ball['x'] > brickLeft:
                if ballLeft <= brickRight:
                    ball['velX'] = -ball['velX']
                    removeIndex = i
                    score += 1 
                    break  
    if removeIndex is not None:
        del brickList[removeIndex]
run( )