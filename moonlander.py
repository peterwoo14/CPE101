"""
CPE 101
Section 6
Project 1 (Moonlander)
Pete Woo
pswoo@calpoly.edu

"""

class Moonlander:
    """Moonlander
    Attributes:
        altitude(float): The distance from the surface of the moon.
        fuel(int): The fuel
        velocity(float): It is positive when the Moonlander is moving away from the moon.
        acceleration(float): It is positive when the Moonlander is moving away from the moon
    """
    def __init__(self, altitude, fuel, velocity, acceleration):
        self.altitude = altitude
        self.fuel = fuel
        self.velocity = velocity
        self.acceleration = acceleration

def show_welcome():
    """This function displays the welcome message.
    """
    print("Welcome to Moonlander")

def get_fuel():
    """This function asks the user for a positive integer.
    Returns:
        fuel(int): Initial fuel
    """
    fuel = int(input("Please enter initial fuel amount [a positive integer]. "))
    while fuel <= 0:
        print("Error, try again.")
        fuel = int(input("Please enter initial fuel amount [a positive integer]. "))
    return fuel

def get_altitude():
    """This function asks the user for an integer input from 1-9999.
    Args:
        None
    Returns:
        altitude(int): Altitude value
    """
    altitude = int(input("Please enter initial altitude a number from 1-9999. "))
    while altitude < 1 or altitude > 9999:
        print("Error, try again.")
        altitude = int(input("Please enter initial altitude a number from 1-9999. "))
    return altitude

def display_state(time, altitude, velocity, fuel, fuel_rate):
    """This function displays variables.
    Args:
        time(int): The time
        altitude(float): The altitude
        velocity(float): The velocity
        fuel(float): The fuel amount
        fuel_rate(int): The fuel rate
    """
    name = ("time={time}, altitude={altitude}, velocity={velocity}, fuel={fuel}, "
            + "fuel rate={fuel_rate}").format(time=time, altitude=altitude, \
            velocity=velocity, fuel=fuel, fuel_rate=fuel_rate)
    print(name)

def get_fuel_rate(fuel):
    """This function asks the user for an integer from 0-9.
    Args:
        fuel(int): Amount of remaining fuel
    Returns:
        int: Fuel rate
    """
    fuel_rate = int(input("Please enter a number from [0-9] "))
    while fuel_rate < 0 or fuel_rate > 9:
        print("Error, try again.")
        fuel_rate = int(input("Please enter the fuel rate [from 0-9] "))
    return min(fuel_rate, fuel)

def display_landing_status(velocity):
    """This function displays the status of the LM upon landing>
    Args:
        velocity(float): Landing velocity of the LM
    """
    if 0 >= velocity >= -1:
        print("Status at landing - The eagle has landed!")
    elif -10 < velocity < -1:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    elif velocity <= -10:
        print("Status at landing - Ouch - that hurt!")

def update_acceleration(gravity, fuel_rate):
    """This function updates the acceleration value.
    Args:
        gravity(float): Gravity constant value
        fuel_rate(int): Fuel rate
    Returns:
        Float: Updated acceleration
    """
    updated_acceleration = gravity * ((fuel_rate / 5) - 1)
    return round(updated_acceleration, 2)

def update_altitude(altitude, velocity, acceleration):
    """This function updats the altitude value.
    Args:
        altitude(float): Current altitude
        velocity(float): Current velocity of LM
        acceleration(float): Current acceleration of LM
    Returns:
        Float: Updated altitude of LM
    """
    updated_altitude = altitude + velocity + (acceleration / 2)
    return round(updated_altitude, 2)

def update_velocity(velocity, acceleration):
    """This function updates the velocity of the LM.
    Args:
        velocity(float): Current velocity of LM
        acceleration(float): Current acceleration of LM
    Returns:
        Float: Updated velocity of LM
    """
    updated_velocity = velocity + acceleration
    return round(updated_velocity, 2)

def update_fuel(fuel, fuel_rate):
    """This function updates the amount of fuel remaining.
    Args:
        fuel(int): Amount of remaining fuel in LM
        fuel_rate: The rate the LM is using fuel
    Returns:
        Int: Updated fuel amount
    """
    updated_fuel = (fuel - fuel_rate)
    return updated_fuel

def main():
    """This function runs the Moonlander program.
    """
    show_welcome() 
    altitude = get_altitude()
    fuel = get_fuel()
    rocket = Moonlander(altitude, fuel, 0, 0)
    fuel_rate = 0
    time = 0
    display_state(time, rocket.altitude, rocket.velocity, rocket.fuel, fuel_rate)
    while rocket.altitude > 0:
        if rocket.fuel == 0:
            fuel_rate = 0
        else:
            fuel_rate = get_fuel_rate(rocket.fuel)
        rocket.fuel = update_fuel(rocket.fuel, fuel_rate)
        rocket.acceleration = update_acceleration(1.62, fuel_rate)
        rocket.altitude = update_altitude(rocket.altitude, rocket.velocity, rocket.acceleration)
        rocket.velocity = update_velocity(rocket.velocity, rocket.acceleration)
        if rocket.altitude < 0:
            rocket.altitude = 0
        time += 1
        display_state(time, rocket.altitude, rocket.velocity, rocket.fuel, fuel_rate)
    display_landing_status(rocket.velocity)

if __name__ == '__main__':
    main()
