class Point():
    
    x = None
    y = None
    w = None
    h = None
    colour = None
    
    g = None
    heuristic = 0
    
    wall = False
    neighbours = []
    
    previous = None
    
    def __init__(self, i, j, pwidth, pheight, colour=None):
        self.width = pwidth
        self.height = pheight
        self.i = i
        self.j = j
        self.colour = colour
        self.g = 0
        self.h = 0
        self.wall = False
        self.neighbours = []
        self.previous = None
       
    def addNeighbours(self, grid, gw, gh):
        #ignore all norths if j -1 < 0
        if self.j - 1 >= 0:
            # north west
            if self.i - 1 >= 0:
                p = grid[self.i - 1 ][self.j - 1]
                self.neighbours.append(p)
            # north
            p = grid[self.i][self.j - 1]
            self.neighbours.append(p)
            # north east
            if self.i + 1 < gw:
                p = grid[self.i + 1 ][self.j - 1]
                self.neighbours.append(p)

        # east
        if self.i + 1 < gw:
            p = grid[self.i + 1][self.j]
            self.neighbours.append(p)
                
        #ignore all souths if j is > grid height
        if self.j + 1 < gh:
            #south west
            if self.i + 1 < len(grid):
                p = grid[self.i + 1 ][self.j + 1]
                self.neighbours.append(p)
            #south
            p = grid[self.i][self.j + 1]
            self.neighbours.append(p)
            #south east
            if self.i - 1 >= 0:
                p = grid[self.i - 1 ][self.j + 1]
                self.neighbours.append(p)
            
        # west
        if self.i - 1 >= 0:
            p = grid[self.i - 1][self.j]
            self.neighbours.append(p)
    
    def show(self, colour=None):
        sx, sy = self.getCenter()
        if self.wall:
            fill(0)
            noStroke()
            ellipse(sx, sy, self.width/2, self.height/2)
            stroke(0)
            strokeWeight(self.width/2)
            for n in self.neighbours:
                if n.wall and ((n.i > self.i and n.j == self.j) or (n.i == self.i and n.j > self.j)):
                    nx, ny = n.getCenter()
                    line(sx, sy,  nx, ny)
        elif colour:
            fill(colour)
            noStroke()
            rect(self.i * self.width, self.j * self.height, self.width, self.height)
        #fill(0)
        #textSize(10)
        #text("%s" % len(self.neighbours), self.x + self.width/2-5, self.y + self.height/2)
        #text("g: %s" % self.g, self.x+1, self.y + 20)
        #text("h: %s" % self.heuristic, self.x+1, self.y + 30)

    def getCenter(self):
        return self.i * self.width + self.width/2, self.j * self.height + self.height/2            
    
    def inspect(self):
        outlist = {}
        outlist['i'] = self.i
        outlist['j'] = self.j
        outlist['g'] = self.g
        outlist['#neighbours'] = len(self.neighbours)
        return outlist
        