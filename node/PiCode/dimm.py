from RPIO import PWM
from sys import stdin,stdout

pin=18

PWM.setup()
PWM.init_channel(13)
PWM.add_channel_pulse(13, pin ,0,0)
while True:
	userinput = stdin.readline().rstrip('\n')

	if userinput == 'quit':
		break
	else:
		stdout.write("LightValue: " + userinput)
		PWM.clear_channel_gpio(13, pin)
		PWM.add_channel_pulse(13, pin ,999,int(userinput))


