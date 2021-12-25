import math

class Point2D(object):
  
  def __init__(self, x, y) -> None:
      self.x = x
      self.y = y

  def __str__(self):
    return f"Point({self.x},{self.y})"

  def getX(self):
    return self.x

  def getY(self):
    return self.x

  def coords(self):
    return tuple(self.x, self.y)

  def distnace(self, p):
    dx = self.x - p.x
    dy = self.y - p.y
    return math.hypot(dx,dy)


class Point3D(object):
  
  def __init__(self, x, y, z) -> None:
      self.x = x
      self.y = y
      self.z = z

  def __str__(self):
    return f"Point({self.x},{self.y},{self.z})"

  def getX(self):
    return self.x

  def getY(self):
    return self.x

  def getZ(self):
    return self.z

  def coords(self):
    return tuple(self.x, self.y, self.z)

  def distnace(self, p):
    dx = self.x - p.x
    dy = self.y - p.y
    dz = self.z  - p.z
    return math.hypot(dx,dy,dz)