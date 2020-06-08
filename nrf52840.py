from board import *
import pulseio

#control the built in RGB LED
class builtin_led:
    """
    Controls the builtin RGB LED
    
    .set_rgb(red, green, blue) / values must be between 0 - 255
    """
    def __init__(self):
        self.pwm_led_red = pulseio.PWMOut(LED_RED, duty_cycle=65535)
        self.pwm_led_green = pulseio.PWMOut(LED_GREEN, duty_cycle=65535)
        self.pwm_led_blue = pulseio.PWMOut(LED_BLUE, duty_cycle=65535)
    
    def set_rgb(self, red, green, blue):
        """set_rgb(red, green, blue); Values must be between 0-255"""
        try:
            self.pwm_led_red.duty_cycle = (255 - red) * 257 if red < 256 else 0
            self.pwm_led_green.duty_cycle = (255 - green) * 257 if green < 256 else 0
            self.pwm_led_blue.duty_cycle = (255 - blue) * 257 if blue < 256 else 0
        except:
            print("All values must be integers between 0-255")