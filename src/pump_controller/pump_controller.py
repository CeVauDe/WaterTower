
import time
import RPi.GPIO as GPIO

class PumpController:
    ''' Class providing all functionalities to controll the water pump.
    
    Motor driver board details see:
    https://www.waveshare.com/wiki/RPi_Motor_Driver_Board
    '''

    def __init__(self, duty_cycle: int = 75):
        self._PIN_M1 = 20
        self._PIN_M2 = 21
        self._PWM_A = 26
        self._PWM_FREQUENCY_HZ = 150

        self.pwm_duty_cycle = duty_cycle


        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self._PIN_M1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self._PIN_M2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self._PWM_A, GPIO.OUT)
        self.pump = GPIO.PWM(self._PWM_A, self._PWM_FREQUENCY_HZ)
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        GPIO.cleanup()

    def	set_motor(self, M1, M2):
        print("Motor set")
        GPIO.output(self._PIN_M1, M1)
        GPIO.output(self._PIN_M2, M2)
	
    def run(self, duration_s: float):
        self.pump.start(self.pwm_duty_cycle)
        self.set_motor(GPIO.HIGH, GPIO.LOW)
        time.sleep(duration_s)
        self.pump.stop()
        