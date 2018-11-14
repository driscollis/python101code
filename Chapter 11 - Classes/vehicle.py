class Vehicle(object):
    """docstring"""

    
    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

        
    def brake(self):
        """
        Stop the car
        """
        return "Braking"
    
    
    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"
    
    
if __name__ == "__main__":
    car = Vehicle("blue", 5, 4)
    print(car.color)
    truck = Vehicle("red", 3, 6)
    print(truck.color)