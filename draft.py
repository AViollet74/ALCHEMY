import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

GPIO.setwarnings(False) #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM) #BCM = Broadcom chip-specific pin numbers
GPIO.setup(21, GPIO.OUT) #setup([pin], [GPIO.IN, GPIO.OUT]), set pin 21 as an output

pin21 = GPIO.PWM(21, 100) #GPIO.PWR([pin][frequency]), analogue output, initialize PWM pin up with 100Hz frequency
pin21.start(50) #start([duty cycle]) set initil value / output to a 50% duty cycle


#GPIO.output(16, GPIO.HIGH) #GPIO.output([pin][GPIO.HIGH]), digital output, set pin 16 high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1
#GPIO.output(21, GPIO.HIGH) #GPIO.output([pin][GPIO.HIGH]), digital output, set pin 21 high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1

#pin16 = GPIO.PWM(16, 100) #GPIO.PWR([pin][frequency]), analogue output, initialize PWM pin up with 100Hz frequency
#pin16.start(50) #start([duty cycle]) set initil value / output to a 50% duty cycle
#pin21 = GPIO.PWM(21, 100) #GPIO.PWR([pin][frequency]), analogue output, initialize PWM pin up with 100Hz frequency
#pin21.start(50) #start([duty cycle]) set initil value / output to a 50% duty cycle

#pin14 = 14
#pin16 = 16
#pin21 = 21
#pins=[pin14,pin16, pin21]

#GPIO.setup(14, GPIO.OUT)                    #setup([pin], [GPIO.IN, GPIO.OUT]), set pin 14 as an output
#GPIO.setup(16, GPIO.OUT) 
#GPIO.setup(21, GPIO.OUT) 


notes=[262,294,330,262,262,294,330]
duration=[0.5,0.5,0.5,0.5,0.5,0.5,0.5]

def play(notes, duration):
    """Method for plazing cool songs
    Args:   notes: Array of frequencies
            duration: Array of durations
    """
    for n,d in zip(notes, duration):
        pin21.ChangeFrequency(n)
        sleep(d)
        
        return()

play(notes, duration)


##########################################################################

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin21 = 21
GPIO.setup(pin21, GPIO.OUT)


def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for i in range(waves):
       GPIO.output(pin21, True) #True = GPIO.HIGH
       sleep(halveWaveTime)
       GPIO.output(pin21, False) #False = GPIO.LOW
       sleep(halveWaveTime)

def play():
    t=0
    notes=[262,294,330,262,262,294,330]
    duration=[0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    
    for n in notes:
        buzz(n, duration[t])
        sleep(duration[t] *0.1)
        t+=1


#buzz(262, 0.5)
play()

##########################################################################

#led = LED(2)                                #Grove_electromagnet as a LED on pin 2
#time = 5                                    #rest time 5 seconds


def setup_magnet(magnets):
    """Set the pins present in the magnets list as LED outputs
    and initialize the led list"""
    
    Led=[]

    for m in magnets:
        Led.append(LED(m))
    return(Led)


def coil(Led, t1, t2):
    """Actuation of the coil
    Args:   led: list of LED(GPIO.BCM pin number)
            t1, t2: int of time on/off  
    """
    for l in Led:
        l.on()
        print("Magnet", l ,"on for", t1, "sec")
        sleep(t1)
        l.off()
        print("Magnet", l ,"off for", t2, "sec")
        sleep(t2)
    
    return() 

##################################################################################################################

GPIO.setwarnings(False) #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM) #BCM = Broadcom chip-specific pin numbers
GPIO.setup(21, GPIO.OUT) #setup([pin], [GPIO.IN, GPIO.OUT]), set pin 21 as an output

pin21 = GPIO.PWM(21, 100) #GPIO.PWR([pin][frequency]), analogue output, initialize PWM pin up with 100Hz frequency
pin21.start(50) #start([duty cycle]) set initil value / output to a 50% duty cycle


while True:
  GPIO.output(21, GPIO.HIGH) #GPIO.output([pin][GPIO.HIGH]), digital output, set pin 21 high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1
  pin21.ChangeFrequency(16.35) # C0
  sleep(1) #time.sleep([seconds])
  pin21.ChangeFrequency(261.63) # C4
  sleep(1)
  GPIO.output(21, GPIO.LOW) #GPIO.output([pin][GPIO.LOW]), digital output, set pin 21 high, GPIO.LOW will drive it to 0V, equivalent GPIO.LOW = Fase = 0
  sleep(1)


################################################################################################################