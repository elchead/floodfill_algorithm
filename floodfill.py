from dataclasses import dataclass
import numpy as np
import copy

@dataclass
class Point:
    x : float
    y : float

@dataclass
class Image:
    """
    A helper class to handle pixel check and setting the color
    """
    def __init__(self,data,width,height):
        self._data = data 
        self.width = width
        self.height = height

    def is_valid_pixel(self,point):
        if(point.x < 0 or point.y < 0):
            return False
        if(point.x >= self.width or point.y >= self.height):
            return False
        return True

    def get_color(self,point : Point):
        color = self._data[point.y][point.x]
        return color
    
    def set_color(self,point,color):
        self._data[point.y][point.x] = color

@dataclass
class FloodFillHelper:
    """
    A helper class to check pixels and mark as visited
    """
    image : Image
    color : list
    prev_color : list
    visited : np.array = 0

    def __post_init__(self):
        self.visited = np.zeros([self.image.height,self.image.width,],dtype=bool)
        color = self.image.get_color(Point(0,0))

        # Make it work for BW and RGB checks:
        if(type(color) == int):
            self._is_same_color = lambda point: self.image.get_color(point) == self.prev_color
        else:
            self._is_same_color = lambda point: (self.image.get_color(point) == self.prev_color).all()

    def visit(self,point):
        self.visited[point.y,point.x] = True

    def _is_visited(self,point):
        return self.visited[point.y,point.x]

    def _is_same_color(self,point):
        pass # initialized in constructor

    def _is_valid(self,point):
        return self.image.is_valid_pixel(point) and not self._is_visited(point) and self._is_same_color(point)

    def check_point(self,point):
        if(self._is_valid(point)):
            self.visit(point)
            return True
        return False

def floodfill(data,width,height,point: Point,new_color):
    image = Image(data,width,height)
    prev_color = copy.copy(image.get_color(point))
    helper = FloodFillHelper(image, new_color, prev_color)
    helper.visit(point)
    queue = [point] # chosen point is set as initial
    while(queue):
        point = queue.pop(0)
        image.set_color(point,new_color)
        
        ## Check neighboring points
        up_point = copy.copy(point)
        up_point.y -= 1
        if(helper.check_point(up_point)):
            queue.append(up_point)

        
        down_point = copy.copy(point)
        down_point.y += 1
        if(helper.check_point(down_point)):
            queue.append(down_point)

        left_point = copy.copy(point)
        left_point.x -= 1
        if(helper.check_point(left_point)):
            queue.append(left_point)


        right_point = copy.copy(point)
        right_point.x += 1
        if(helper.check_point(right_point)):
            queue.append(right_point)

def floodfill_bw(data, width, height, u, v, sw_color: int):
    floodfill(data, width, height, Point(u, v), sw_color)

def floodfill_rgb(data,width,height,u,v,s_r, s_g, s_b):
    floodfill(data, width, height, Point(u,v),np.array([s_r, s_g, s_b]))

