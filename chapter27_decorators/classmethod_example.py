class Time:
    """an example 24-hour time class"""
    
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    
    def __repr__(self):
        return "Time(%d, %d)" % (self.hour, self.minute)
    
    @classmethod
    def from_float(cls, moment):
        """2.5 == 2 hours, 30 minutes, 0 seconds, 0 microseconds"""
        hours = int(moment)
        if hours:
            moment = moment % hours
        minutes = int(moment * 60)
        return cls(hours, minutes)
    
    def to_float(self):
        """return self as a floating point number"""
        return self.hour + self.minute / 60

Time(7, 30)
Time.from_float(5.75)
t = Time(10, 15)
t.to_float()