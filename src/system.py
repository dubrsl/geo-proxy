import RPi.GPIO as GPIO

KRAKEN_POWER_RELAY_PIN_BCM = 27

def turn_kraken_off():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(KRAKEN_POWER_RELAY_PIN_BCM, GPIO.OUT)
    GPIO.output(KRAKEN_POWER_RELAY_PIN_BCM, GPIO.HIGH)

def turn_kraken_on():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(KRAKEN_POWER_RELAY_PIN_BCM, GPIO.OUT)
    GPIO.output(KRAKEN_POWER_RELAY_PIN_BCM, GPIO.LOW)