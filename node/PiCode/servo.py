from RPIO import PWM
import sys
import time
from sys import stdin,stdout

print "NewServoStarted"

print "ready"

pin=22

open=47
close=7


PWM.setup()
PWM.init_channel(14)
PWM.set_loglevel(PWM.LOG_LEVEL_ERRORS)


userinput = stdin.readline().rstrip('\n')

x=open
i=close+15

while i in range(close,open):
	i=i+1
	PWM.add_channel_pulse(14, pin , i, i)
	time.sleep(0.17)

PWM.clear_channel_gpio(14,pin)
time.sleep(int(userinput))

while x in range(close+15,open+1):
	x=x-1
	PWM.add_channel_pulse(14, pin , x, x)
	time.sleep(0.05)

PWM.clear_channel_gpio(14, pin)

print "ServoClosed"




