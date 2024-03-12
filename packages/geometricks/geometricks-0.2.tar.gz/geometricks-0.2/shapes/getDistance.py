from shapes.circle import Circle
from shapes.line import Line
from shapes.point import Point
from shapes.polygon import Polygon
from shapes.segment import Segment

def getDistance(arg1, arg2):
    if type(arg1) == Polygon:
        if type(arg2) == Point:
            return arg1.getDistancePoint(arg2)
        elif type(arg2) == Circle:
            return arg1.getDistanceCircle(arg2)
        elif type(arg2) == Line:
            return arg1.getDistanceLine(arg2)
        elif type(arg2) == Segment:
            return arg1.getDistanceSegment(arg2)
        elif type(arg2) == Polygon:
            return arg1.getDistancePolygon(arg2)
    elif type(arg1) == Point:
        if type(arg2) == Point:
            return arg1.getDistancePoint(arg2)
        elif type(arg2) == Circle:
            return arg1.getDistanceCircle(arg2)
        elif type(arg2) == Line:
            return arg1.getDistanceLine(arg2)
        elif type(arg2) == Segment:
            return arg1.getDistanceSegment(arg2)
        elif type(arg2) == Polygon:
            return arg1.getDistancePolygon(arg2)
    elif type(arg1) == Circle:
        if type(arg2) == Point:
            return arg1.getDistancePoint(arg2)
        elif type(arg2) == Circle:
            return arg1.getDistanceCircle(arg2)
        elif type(arg2) == Line:
            return arg1.getDistanceLine(arg2)
        elif type(arg2) == Segment:
            return arg1.getDistanceSegment(arg2)
        elif type(arg2) == Polygon:
            return arg1.getDistancePolygon(arg2)
    elif type(arg1) == Line:
        if type(arg2) == Point:
            return arg1.getDistancePoint(arg2)
        elif type(arg2) == Circle:
            return arg1.getDistanceCircle(arg2)
        elif type(arg2) == Line:
            return arg1.getDistanceLine(arg2)
        elif type(arg2) == Segment:
            return arg1.getDistanceSegment(arg2)
        elif type(arg2) == Polygon:
            return arg1.getDistancePolygon(arg2)
    elif type(arg1) == Segment:
        if type(arg2) == Point:
            return arg1.getDistancePoint(arg2)
        elif type(arg2) == Circle:
            return arg1.getDistanceCircle(arg2)
        elif type(arg2) == Line:
            return arg1.getDistanceLine(arg2)
        elif type(arg2) == Segment:
            return arg1.getDistanceSegment(arg2)
        elif type(arg2) == Polygon:
            return arg1.getDistancePolygon(arg2)
