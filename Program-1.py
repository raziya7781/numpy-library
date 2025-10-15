
class Car:
    
    def __init__(self, make, model, year):
        self.make = make      # Brand of the car (e.g., Toyota)
        self.model = model    # Model name (e.g., Corolla)
        self.year = year      # Year of manufacture
        self.running = False  # Car is initially off

   
    def start(self):
        print("Car is starting...")
        self.running = True

    
    def stop(self):
        print("Car is stopping...")
        self.running = False


my_car = Car("Honda", "Civic", 2022)

my_car.start()  # Output: Car is starting...
my_car.stop()   # Output: Car is stopping...
