import math
class Coordinates :
     def polar_to_cartesian(self,r,theta,unit) :
          if unit == 'DEGREE':
               theta = math.radians(theta)
          elif unit != 'RADIAN' :
               print('Error: Unit must be either "degrees" or "radians".')
               return None
          x = r *math.cos(theta)
          y = r *math.sin(theta)
          return(x,y)
     def cartesian_to_polar(self,x,y):
          r = math.sqrt(x ** 2 + y ** 2)
          theta = math.atan2(y,x)
          theta = math.degrees(theta)
          return (r,theta)
     

        

        
        
