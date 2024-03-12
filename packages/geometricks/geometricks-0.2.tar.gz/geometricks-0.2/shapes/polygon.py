import math

class Polygon:
    def __init__(self, points):
        if len(points) < 3:
            raise ValueError("Un polygone doit avoir au moins 3 points.")
        self.points = points
    
    def get_coord(self):
        return self.points
    
    def distance_point_segment(self, point, segment):
        # Calcule la distance entre un point et un segment
        x, y = point.x, point.y
        x1, y1 = segment.p1.x, segment.p1.y
        x2, y2 = segment.p2.x, segment.p2.y

        dx = x2 - x1
        dy = y2 - y1

        if dx == dy == 0:  # Le segment est un point
            return math.hypot(x - x1, y - y1)

        t = ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)

        if t < 0:
            px, py = x1, y1
        elif t > 1:
            px, py = x2, y2
        else:
            px, py = x1 + t * dx, y1 + t * dy

        return math.hypot(x - px, y - py)

    def distance_point_line(self, point, line):
        # Calcule la distance entre un point et une droite
        return abs(line.a * point.x + line.b * point.y + line.c) / math.sqrt(line.a ** 2 + line.b ** 2)

    def distance_point_circle(self, point, circle):
        # Calcule la distance entre un point et un cercle
        return abs(math.sqrt((point.x - circle.centre.x) ** 2 + (point.y - circle.centre.y) ** 2) - circle.rayon)

    def distance_point_polygon(self, point):
        # Calcule la distance entre un point et un polygone (si le point est à l'intérieur du polygone, la distance est 0)
        # le calcul de isInside ne sera pas fait dans point mais bien ici 
        n = len(self.points)
        inside = False
        x, y = point.x, point.y
        p1x, p1y = self.points[0].x, self.points[0].y
        for i in range(n + 1):
            p2x, p2y = self.points[i % n].x, self.points[i % n].y
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        if inside:
            return 0
        else:
            distances = [math.hypot(point.x - p.x, point.y - p.y) for p in self.points]
            return min(distances)
        

    def getDistanceSegment(self, segment):
        # Calcule la distance entre le polygone et un segment
        distances = [self.distance_point_segment(p, segment) for p in self.points]
        return min(distances)

    def getDistanceLine(self, line):
        # Calcule la distance entre le polygone et une droite
        distances = [self.distance_point_line(p, line) for p in self.points]
        return min(distances)

    def getDistanceCircle(self, circle):
        # Calcule la distance entre le polygone et un cercle
        distances = [self.distance_point_circle(p, circle) for p in self.points]
        return min(distances)

    def getDistancePoint(self, point):
        # Calcule la distance entre le polygone et un point
        return self.distance_point_polygon(point)

    def getDistancePolygon(self, polygon):
        # Calcule la distance entre le polygone et un autre polygone
        distances = [polygon.getDistancePoint(p) for p in self.points]
        return min(distances)

