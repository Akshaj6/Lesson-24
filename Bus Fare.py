class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
class Bus(Vehicle):
    def __init__(self, name, seating_capacity):
        self.name = name
        super().__init__(seating_capacity)
    def fare(self):
        bus_fare = self.seating_capacity * 100
        maintenance_charge = bus_fare * 0.10
        final_fare = bus_fare + maintenance_charge
        return final_fare
school_bus = Bus("School Bus", 50)
fare_bus = school_bus.fare()
print("The final fare for the bus ride is :\n ₹", fare_bus)