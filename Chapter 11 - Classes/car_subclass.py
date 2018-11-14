class Car(Vehicle):
    """
    The Car class
    """
    
    
    def brake(self):
        """
        Override brake method
        """
        return "The car class is breaking slowly!"
    
    
if __name__ == "__main__":
    car = Car("yellow", 2, 4, "car")
    car.brake()
    'The car class is breaking slowly!'
    car.drive()
    "I'm driving a yellow car!"