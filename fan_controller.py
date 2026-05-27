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
    
    # Part 4: Ito naman yung setters natin. Para kung gusto natin baguhin yung speed o kulay, dadaan muna dito, safe ang data modification natin.
    def set_speed(self, fan_speed):
        self.__speed = fan_speed
        
    def set_radius(self, fan_radius):
        self.__radius = float(fan_radius)
        
    def set_color(self, fan_color):
        self.__color = fan_color
        
    def set_on(self, fan_power_status):
        self.__on = fan_power_status

    # Part 5: Dito ko nilagay yung funny dashboard natin. Print statements na may konting sass para hindi boring yung terminal output natin mamaya kapag ni-run na.
    def display_fan_dashboard(self, fan_personality):
        power_state_message = "🟢 ON (Prepare to be blown away!)" if self.__on else "🔴 OFF (Just collecting dust...)"
        print(f"==== 🌬️ {fan_personality.upper()} DASHBOARD ====")
        print(f"| Life Status  : {power_state_message}")
        print(f"| Velocity     : Level {self.__speed} (1=Breeze, 3=Tornado)")
        print(f"| Aesthetics   : {self.__color.capitalize()} (Very fashionable)")
        print(f"| Girth/Radius : {self.__radius} inches of pure wind power")
        print("==================================================\n")

    # Part 6: Simulan na natin i-test. Ginawa ko muna yung first object natin, yung yellow na fan na naka-max speed at buhay na buhay para mag-mala-bagyo sa kwarto.
def test_fan_program():
    print("\n[ INITIATING GLOBAL COOLING PROTOCOL... ]\n")
    
    hurricane_mode_fan = Fan()
    hurricane_mode_fan.set_speed(Fan.FAST)
    hurricane_mode_fan.set_radius(10.0)
    hurricane_mode_fan.set_color("yellow")
    hurricane_mode_fan.set_on(True)