import Point

grid_cols = 50
grid_rows = 50
grid = [[i for i in range(grid_rows)] for j in range(grid_cols)]

closedSet = set()
openSet = set()

istart = (0, 0)
iend = (grid_cols - 1, grid_rows -1)
pstart = None
goal = None
iterations = 0
colourise = False

def heuristic(pstart, goal):
    sx, sy = pstart.getCenter()
    gx, gy = goal.getCenter()
    distance = dist(sx,sy,gx,gy)
    return distance

def tuple_to_point(grid, index):
    return grid[index[0]][index[1]]

def setup():
    global pstart, goal
    size(600,600)
    print "A*!"
    for i in range(grid_cols):
        for j in range(grid_rows):
            grid[i][j] = Point.Point(i,j,width/grid_cols, width/grid_rows, color(255))
            if random(1.0) <= 0.4:
                grid[i][j].wall = True
    # start and end are never walls
    pstart = tuple_to_point(grid, istart)
    goal = tuple_to_point(grid, iend)
    pstart.wall = False
    goal.wall = False
    for i in range(grid_cols):
        for j in range(grid_rows):
            grid[i][j].addNeighbours(grid, grid_cols, grid_rows)
    openSet.add(pstart)
    pstart.g = 0
    pstart.h = heuristic(pstart, goal)
    frameRate(200)
    
def draw():
    global openSet, closedSet, iterations, colourise
    if openSet:
        winner = min(openSet, key=lambda o:o.g + o.h)
        for p in openSet:
            if p.g  + p.h == winner.g + winner.h:
                if p.g > winner.g:
                    winner = p
        current = winner
        if current == goal:
            finished(True)
        openSet.remove(current)
        closedSet.add(current)
        for n in current.neighbours:
            if n in closedSet or n.wall:
                continue
            elif n in openSet:
                new_g = current.g + heuristic(current, n)
                if n.g > new_g:
                    n.g = new_g
                    n.previous = current
            else:
                n.g = current.g + heuristic(current, n)
                n.h = heuristic(n, goal)
                n.previous = current
                openSet.add(n)
        iterations += 1
            
    else:
        finished(False)
        return
    
    background(255)
    showAll()
    path = []
    temp = current
    path.append(temp)
    while temp.previous:
        path.append(temp.previous)
        temp = temp.previous
    noFill()
    stroke(255,0,200)
    strokeWeight(2)
    beginShape()
    for p in path:
        px, py = p.getCenter()
        vertex(px, py)
    endShape()
    frame.setTitle("%s fps" % frameRate);
    
def finished(solved):
    if solved:
        print "Solved in %s iterations!" % iterations
    else:
        print "No solution :("
    noLoop()
    
def colourise():
    for i in range(grid_cols):
        for j in range(grid_rows):
            c = grid[i][j]
            #if c in openSet:
            #    c.colour = color(0,0,255)
            if c in closedSet:
                cx, cy = c.getCenter()
                sx, sy = pstart.getCenter()
                gx,gy = goal.getCenter()
                goaldist = dist(cx,cy,gx,gy)
                totaldist = dist(sx, sy, gx,gy)
                green = map(goaldist,0,totaldist,255,0)
                red = map(goaldist,0,totaldist,0,255)
                c.colour = color(red,green,0)
        
def showAll():
    noStroke()
    for x in range(grid_cols):
        for y in range(grid_rows):
            if grid[x][y].wall:
                grid[x][y].show()
            elif grid[x][y] in openSet:
                grid[x][y].show(color(0, 255, 0, 50))
            elif grid[x][y] in closedSet:
                grid[x][y].show(color(255, 0, 0, 50))