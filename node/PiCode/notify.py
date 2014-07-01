import RPi.GPIO as GPIO
import time
import httplib, urllib

def notifyme():
	
	# Application specific variables
	application_token = "aMFAb84mCYHEVYNJDNATF8GceBLSQS"
	user_token = "uAiGD8V8fequ2KeDef946nQY9K474w"

	# Message specific variables
	title = "Let Me in !!"
	message = "Your Cat wants to enter the House | " + time.strftime("%d.%m.%Y %H:%M:%S", time.gmtime())



	# Start your connection with the Pushover API server
	conn = httplib.HTTPSConnection("api.pushover.net:443")

	# Send a POST request in urlencoded json
	conn.request("POST", "/1/messages.json",
	urllib.urlencode({
	"token": application_token,
	"user": user_token,
	"title": title,
	"message": message,
	}), { "Content-type": "application/x-www-form-urlencoded" })

	# Listen for any error messages or other responses
	conn.getresponse()

	time.sleep(300)




GPIO.setmode(GPIO.BCM)
PIR_PIN = 24
GPIO.setup(PIR_PIN, GPIO.IN)


time.sleep(2)
print "PIR Ready"
GPIOLast=GPIO.input(PIR_PIN)


while True:
	if GPIOLast!=GPIO.input(PIR_PIN) :

		Time=0

		GPIOLast=GPIO.input(PIR_PIN)

		while GPIO.input(PIR_PIN)==1:
			Time=Time+1
			time.sleep(1)
			if Time>=13:
				notifyme()
	else:
		time.sleep(0.1)
		pass









