import math

class AngleMode:
   
    def __init__(self):
        self._mode = 'DEG' # default is degrees
    
    def set_mode(self, mode):
        mode = mode.upper()
        if mode in ['DEG', 'RAD']:
            self._mode = mode
        else:
            raise ValueError("Mode must be 'DEG' or 'RAD'")
    
    def get_mode(self):
        return self._mode
    
    def to_radians(self, angle):
        if self._mode == 'DEG':
            return math.radians(angle)
        else:
            return angle  
    def from_radians(self, angle):
        if self._mode == 'DEG':
            return math.degrees(angle)
        else:
            return angle  

angle_mode = AngleMode()