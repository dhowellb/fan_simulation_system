# Part 1: Gawa muna tayo ng blueprint ng Fan natin. Nag-set din ako ng constants para sa speed levels para madali tandaan.
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Part 2: Dito na papasok yung constructor. Sinunod ko yung strict encapsulation gamit yung double underscores (__) para hidden at safe yung data natin.
    def __init__(self, fan_speed=SLOW, fan_radius=5.0, fan_color="blue", fan_power_status=False):
        self.__speed = fan_speed
        self.__radius = float(fan_radius)
        self.__color = fan_color
        self.__on = fan_power_status
    
    # Part 3: Gumawa ako ng getters. Kasi nga naka-private yung variables natin, kailangan natin ng paraan para masilip sila sa labas nang hindi nasisira yung rules ng OOP.
    def get_speed(self):
        return self.__speed
        
    def get_radius(self):
        return self.__radius
        
    def get_color(self):
        return self.__color
        
    def get_on(self):
        return self.__on