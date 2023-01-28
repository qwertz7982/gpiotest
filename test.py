import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
GPIO.setup (4, GPIO.OUT)

while:
  GPIO.output(4, True)
  print("on")
  time.sleep(5)
  GPIO.output(4, False)
  print("off")
