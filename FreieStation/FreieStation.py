import math as math

RHO = 200 / math.pi

X0 = 0
Y0 = 0 
Ori0 = 0
Liste = []
class Punkt(object):
       def __init__(self, nr, x, y, ri, s):
           self.X = x
           self.Y = y
           self.RI = ri
           self.S = s
           #self.SI0 = si0
           #self.TI0 = ti0
           #self.L = s-si0
           
      
           

           arc = math.atan2(self.Y - Y0, self.X - X0) * RHO
           self.ti = arc + 400
           print(self.ti)

           self.si = math.sqrt((X0 - self.X)*(X0 - self.X) + (Y0 - self.Y)*(Y0 - self.Y))
           print(self.si)

p1 = Punkt(1,10.40542579,-36.6353169,317.617764,38.084)

p1.ti 
p2 = Punkt(2,40.37045579,-18.48286088,372.666897,44.40033612)
p2.ti
p3 = Punkt(3,25.77614967,-35.403,340.063612,43.7927985)
p3.ti
Liste.append(p1)
Liste.append(p2)
Liste.append(p3)

