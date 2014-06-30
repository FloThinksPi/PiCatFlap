import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 24
GPIO.setup(PIR_PIN, GPIO.IN)

try:
	print "PIR Module Test (CTRL+C to exit)"
	time.sleep(2)
	print "Ready"
	GPIOLast=GPIO.input(PIR_PIN)
	start=time.clock()
	while True:
		if GPIOLast!=GPIO.input(PIR_PIN):
			end=time.clock()
			print end - start 
			print "---------------------"
			print GPIO.input(PIR_PIN)
			GPIOLast=GPIO.input(PIR_PIN)
			start=time.clock()


except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()
