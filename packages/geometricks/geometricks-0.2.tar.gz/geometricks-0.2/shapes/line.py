import math

class Line:
    def __init__(self, p1, p2, p3):
        self.a = p1
        self.b = p2
        self.c = p3
    
    def get_coord(self):
        return (self.a, self.b, self.c)
    
    def getDistancePoint(self, point):
        # get the distance between a line and a point
        x, y = point.get_coord()
        
        if self.b == 0:
            distance = abs(self.c - point.y)
        else:
            distance = abs((self.a * point.x + self.b * point.y + self.c) / math.sqrt(self.a**2 + self.b**2))
        
        return distance
    
    def getDistanceLine(self, line):
        # get the distance between a line and a line
        return abs(self.c - line.c) / math.sqrt(self.a**2 + self.b**2)
    
    def getDistanceSegment(self, segment):
        # get the distance between a line and a segment
        # get the distance between the line and the two points of the segment
        distance1 = self.getDistancePoint(segment.p1)
        distance2 = self.getDistancePoint(segment.p2)
        # the distance between the line and the segment is the minimum distance between the line and the two points of the segment
        return min(distance1, distance2)
    
    def getDistancePolygon(self, polygon):
        # get the distance between a line and a polygon
        # get the distance between the line and the points of the polygon
        distances = []
        for i in range(len(polygon.points)):
            distances.append(self.getDistancePoint(polygon.points[i]))
        # the distance between the line and the polygon is the minimum distance between the line and the points of the polygon
        return min(distances)
    
    def getDistanceCircle(self, circle):
        # get the distance between a line and a circle
        return abs(self.c - circle.centre.x * self.a - circle.centre.y * self.b) / math.sqrt(self.a**2 + self.b**2)
    
    