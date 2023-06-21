import RPi.GPIO as GPIO

# Define GPIO pins
RED_PIN = 12
GREEN_PIN = 40
BLUE_PIN = 33

# Set up the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set up the pins as output
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Set up PWM on pins
red_pwm = GPIO.PWM(RED_PIN, 1000) 
green_pwm = GPIO.PWM(GREEN_PIN, 1000)
blue_pwm = GPIO.PWM(BLUE_PIN, 1000)

# Start PWM on each pin
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

def set_rgb(r, g, b):
    """Set RGB LED color.

    Args:
    r, g, b: Red, green and blue values (0-255).
    """
    red_pwm.ChangeDutyCycle(r / 255 * 100)
    green_pwm.ChangeDutyCycle(g / 255 * 100)
    blue_pwm.ChangeDutyCycle(b / 255 * 100)

def cleanup():
    # Stop PWM on each pin
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    # Reset GPIO settings
    GPIO.cleanup()
