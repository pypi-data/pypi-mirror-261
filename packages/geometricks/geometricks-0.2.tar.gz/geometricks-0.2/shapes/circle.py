import math

class Circle:
    def __init__(self, p1, r):
        self.centre = p1
        self.rayon = r

    def get_coord(self):
        return (self.centre.x, self.centre.y)

    def getDistancePoint(self, point):
        # Distance entre le centre du cercle et le point
        distance = math.sqrt((self.centre.x - point.x) ** 2 + (self.centre.y - point.y) ** 2)
        # Distance est la différence entre le rayon et la distance
        distance = abs(distance - self.rayon)
        return distance

    def getDistanceLine(self, droite):
        # Calcul de la distance entre le centre du cercle et la droite (avec a b et c)
        # prend en compte le cas de la division par 0
        if droite.b == 0:
            distance = abs(droite.c - self.centre.y)
        else:
            distance = abs(droite.a * self.centre.x + droite.b * self.centre.y + droite.c) / math.sqrt(droite.a ** 2 + droite.b ** 2)

        distance = abs(distance - self.rayon)   

        return distance

    def getDistanceSegment(self, segment):
        # si le segment traverse, est dans ou touche un bord du cercle alors la distance est 0
        if segment.p1.x <= self.centre.x <= segment.p2.x and segment.p1.y <= self.centre.y <= segment.p2.y:
            return 0

        # Calcul de la distance entre le centre du cercle et le segment
        AB = segment.p2.x - segment.p1.x
        AC = segment.p2.y - segment.p1.y
        BC = math.sqrt(AB ** 2 + AC ** 2)
        # Calcul de la distance entre le centre et le point projeté sur la droite du segment
        distance = abs((AC * self.centre.x - AB * self.centre.y + segment.p2.x * segment.p1.y - segment.p2.y * segment.p1.x) / BC)
        distance = abs(distance - self.rayon)
        return distance

    def getDistancePolygon(self, polygon):
        distances = []
        for point in polygon.points:
            distances.append(self.getDistancePoint(point))
        return min(distances)

    def getDistanceCircle(self, circle):
        # Calcul de la distance entre deux cercles
        distance = math.sqrt((self.centre.x - circle.centre.x) ** 2 + (self.centre.y - circle.centre.y) ** 2)
        distance = abs(distance - self.rayon - circle.rayon)
        return distance

