import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(35, GPIO.OUT)# luz

GPIO.output(35, 1)
