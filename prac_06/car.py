"""CP1404/CP5632 Practical - Car class example."""

class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.
        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of a Car object."""
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odometer)