import pygame
from vec2D import Vec2d
from abc import ABC, abstractmethod
import math
class Base(ABC):
    def __init__(self, surface, steps = 35, points = None, speed = None):
        self.surface = surface
        self.steps = steps

    @classmethod
    def add_points(self, points, speed):
        pass

    @classmethod
    def draw_points(self, style ="points", width = 3, color = (255, 215, 0)):
        pass

class Polyline(Base):

    
    def __add__(self, points, speed):
        if points == None:
            self.points = []
        else:
            self.points = points
        
        if speed == None:
            self.speed = []
        else:
            self.speed = speed
    
    def add_points(self, points, speed):
        self.points.append(points)
        self.speed.append(speed)

    def set_points(self):
        for i in range(len(self.points)):
            self.points[i] = self.speed[i] + self.points[i]
            if self.points[i].x > self.surface.get_width() or self.points[i].x < 0:
                self.speeds[i] = Vec2d(-self.speeds[i].x, self.speeds[i].y)
            if self.points[i].y > self.surface.get_height() or self.points[i].y < 0:
                self.speeds[i] = Vec2d(self.speeds[i].x, -self.speeds[i].y)

    def draw_points(self, style ="points", width = 3, color = (255, 255, 255)):
        for i in self.points:
            if style == "points":
                for p in self.points:
                    pygame.draw.circle(self.surface, color, i.int_pair(), width)
            if style == "line":
                k = Knot(self.surface).get_knot(self.points, self.steps)
                for j in range(-1, len(k) - 1):
                    pygame.draw.line(self.surface, color, k[j].int_pair(), k[j + 1].int_pair(), width)


class Knot(Polyline):
    def get_knot(self, points, n):
        if len(points) < 3:
            return []
        result = []
        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append((points[i]+points[i+1]) * 0.5)
            ptn.append(points[i+1])
            ptn.append((points[i+1]+points[i+2]) * 0.5)

            result.extend(self.get_points(ptn, n))
        return result

    def get_points(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg]*alpha + self.get_point(points, alpha, deg-1)*(1-alpha)

    def get_points(self, base_points, n):
        alpha = 1 / n
        result = []
        for i in range(n):
            result.append(self.get_point(base_points, i * alpha))
        return result