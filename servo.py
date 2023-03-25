import RPi.GPIO as GPIO
import time

# Servo motorun bağlı olduğu GPIO pin numarası
servo_pin = 18

# GPIO pinlerini BCM modunda ayarla
GPIO.setmode(GPIO.BCM)

# Servo motorun bağlı olduğu pinin çıkış olarak ayarla
GPIO.setup(servo_pin, GPIO.OUT)

# PWM (Pulse-Width Modulation) nesnesi oluştur ve frekansı ayarla
pwm = GPIO.PWM(servo_pin, 50)

# PWM sinyalini başlat
pwm.start(0)

# Servo motoru 0 derece pozisyonda başlat
def set_servo_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

# Servo motoru 180 dereceye kadar döndür
set_servo_angle(0)
time.sleep(1)
set_servo_angle(180)
time.sleep(1)

# PWM sinyalini durdur ve GPIO pinlerini temizle
pwm.stop()
GPIO.cleanup()
