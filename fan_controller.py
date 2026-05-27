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