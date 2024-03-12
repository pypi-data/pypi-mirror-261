import math


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        

    def get_coord(self):
        return (self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def getDistancePoint(self, point):
        # get the distance between a point and a segment
        x1, y1, x2, y2 = self.get_coord()
        x, y = point.x, point.y
        dx = x2 - x1
        dy = y2 - y1
        if dx == dy == 0:  # Si les points p1 et p2 sont les mêmes
            return math.sqrt((x - x1)**2 + (y - y1)**2)
        t = ((x - x1) * dx + (y - y1) * dy) / (dx**2 + dy**2)
        t = max(0, min(1, t))  # Limiter t entre 0 et 1 pour être sur le segment
        proj_x = x1 + t * dx
        proj_y = y1 + t * dy
        return math.sqrt((x - proj_x)**2 + (y - proj_y)**2)
    

    def getDistanceSegment(self, segment):
        # Calcul de la distance entre deux segments
        distances = [
            self.getDistancePoint(segment.p1),
            self.getDistancePoint(segment.p2),
            segment.getDistancePoint(self.p1),
            segment.getDistancePoint(self.p2)
        ]
        return min(distances)

    def getDistanceLine(self, line):
        # Calcul de la distance entre un segment et une droite
        return min(line.getDistancePoint(self.p1), line.getDistancePoint(self.p2))

    def getDistancePolygon(self, polygon):
        # Calcul de la distance entre un segment et un polygone
        distances = []
        for point in polygon.points:
            distances.append(self.getDistancePoint(point))
        return min(distances)

    def getDistanceCircle(self, circle):
        # Calcul de la distance entre un segment et un cercle
        return min(self.getDistancePoint(circle.centre), self.getDistanceLine(circle))


    


# Exemple d'utilisation
#segment1 = Segment(Point(0, 0), Point(1, 1))
#segment2 = Segment(Point(2, 0), Point(0, 2))

# Calculer la distance entre les deux segments
#distance = segment1.get_distance_segment(segment2)
#print("Distance entre les segments :", distance)