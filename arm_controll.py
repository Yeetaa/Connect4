from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

kit.servo[0].set_pulse_width_range(500, 2500)
kit.servo[1].set_pulse_width_range(1000, 2000)

kit.servo[1].angle = 90 #Greifer
#kit.servo[2].angle = 70 #Arm 2 15-75 °
#kit.servo[3].angle = 40 #Arm 1 0-40°
kit.servo[0].angle = 90 #Base 90° = gerade

time.sleep(0.5)


kit.servo[0].angle = None
kit.servo[1].angle = None
kit.servo[2].angle = None
kit.servo[3].angle = None