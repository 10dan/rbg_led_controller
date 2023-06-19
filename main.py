import os
from time import sleep

class GPIO_Pin:
    def __init__(self, num, mode):
        gpio_mapping = {
            # Add the GPIO mapping from the RockPi 4 here
            71: 2, # GPIO2_A7
            72: 3, # GPIO2_B0
            75: 7, # GPIO2_B3
            # ... continue with the rest of the mapping
        }
        if num not in gpio_mapping:
            raise ValueError('Invalid Pin Number -> Enter a valid GPIO number')
        self.num = gpio_mapping[num]
        if mode not in ['out', 'write', 'in', 'read']:
            raise ValueError('Invalid Pin Mode -> Enter "out" or "write" for output, "in" or "read" for input')
        self.mode = 'out' if mode in ['out', 'write'] else 'in'
        os.system(f'echo {str(self.num)} > /sys/class/gpio/export')
        sleep(0.05)
        os.system(f'echo {self.mode} > /sys/class/gpio/gpio{str(self.num)}/direction')

    def reset(self):
        os.system(f'echo 0 > /sys/class/gpio/gpio{str(self.num)}/value')
        os.system(f'echo in > /sys/class/gpio/gpio{str(self.num)}/direction')

    def write(self, value):
        if value not in [0, 1, 'LOW', 'HIGH']:
            raise ValueError('Invalid value -> Enter 1 or "HIGH" for HIGH, 0 or "LOW" for LOW')
        value = '1' if value in [1, 'HIGH'] else '0'
        os.system(f'echo {value} > /sys/class/gpio/gpio{str(self.num)}/value')

    def __del__(self):
        self.reset()
        os.system(f'echo {str(self.num)} > /sys/class/gpio/unexport')

    def set_mode(self, mode):
        if mode not in ['out', 'write', 'in', 'read']:
            raise ValueError('Invalid Pin Mode -> Enter "out" or "write" for output, "in" or "read" for input')
        self.mode = 'out' if mode in ['out', 'write'] else 'in'
        os.system(f'echo {str(self.mode)} > /sys/class/gpio/gpio{str(self.num)}/direction')

class PWM_Pin:
    def __init__(self, num):
        self.num = num
        os.system(f'echo {self.num} > /sys/class/pwm/pwmchip0/export')
        sleep(0.1)
        self.set_period(20000)  # set period to 20000 us = 20 ms
        self.set_duty_cycle(0)  # initially set duty cycle to 0%

    def set_period(self, period_us):
        os.system(f'echo {period_us} > /sys/class/pwm/pwmchip0/pwm{self.num}/period')

    def set_duty_cycle(self, duty_cycle_percent):
        period_us = int(open(f'/sys/class/pwm/pwmchip0/pwm{self.num}/period').read())
        duty_cycle_us = period_us * duty_cycle_percent // 100
        os.system(f'echo {duty_cycle_us} > /sys/class/pwm/pwmchip0/pwm{self.num}/duty_cycle')

    def enable(self):
        os.system(f'echo 1 > /sys/class/pwm/pwmchip0/pwm{self.num}/enable')

    def disable(self):
        os.system(f'echo 0 > /sys/class/pwm/pwmchip0/pwm{self.num}/enable')

    def __del__(self):
        self.disable()
        os.system(f'echo {self.num} > /sys/class/pwm/pwmchip0/unexport')


r = PWM_Pin(0)
g = PWM_Pin(1)
b = PWM_Pin(2)

# Now you can control the intensity of each color with set_duty_cycle:
r.set_duty_cycle(50)  # 50% intensity for red
g.set_duty_cycle(25)  # 25% intensity for green
b.set_duty_cycle(75)  # 75% intensity for blue

r = GPIO_Pin(71, 'out')
g = GPIO_Pin(72, 'out')
b = GPIO_Pin(75, 'out')

# all_cols = [
#     [0,0,0],
#     [0,0,1],
#     [0,1,0],
#     [0,1,1],
#     [1,0,0],
#     [1,0,1],
#     [1,1,0],
#     [1,1,1]]
all_cols = [
    [0,0,1],
    [0,1,0],
    [1,0,0]]

import random
def main():
    # d =0.3
    # for i in range(1000):
    #     sleep(d)
    #     # rand = random.randint(0, 7)
    #     # color = all_cols[rand]
    #     # set_light(r, color[0])
    #     # set_light(g, color[1])
    #     # set_light(b, color[2])
    #     # sleep(d)
    #     for color in all_cols:
    #         set_light(r, color[0])
    #         set_light(g, color[1])
    #         set_light(b, color[2])
    #         sleep(100)
    print("test")
    set_light(r, 0)
    set_light(g, 1)
    set_light(b, 0)
    sleep(100)

def set_light(light, color):
    if color == 1:
        light.write('HIGH')
    else:
        light.write('LOW')

if __name__ == '__main__':
    print("1")
    set_light(r, 0)
    print("2")
    set_light(g, 1)
    print("3")
    set_light(b, 0)
    sleep(1000)
    # main()
