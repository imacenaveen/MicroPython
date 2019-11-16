
# import library to deal with pins:
from machine import Pin
from time import sleep
# define pin 0 as output
m1_1 = Pin(16, Pin.OUT) # Motor 1 , pin1
m1_2 = Pin(5, Pin.OUT) # Motor 2 , pin2
m2_1 = Pin(4, Pin.OUT) # Motor 2 , pin1
m2_2 = Pin(0, Pin.OUT) # Motor 1 , pin1

m1_1.value(1)
m1_1.value(0)
m1_2.value(1)
m1_2.value(0)

m2_1.value(1)
m2_1.value(0)
m2_2.value(1)
m2_2.value(0)

for _ in range(5):
    m1_1.on();m1_2.off()
    m2_1.on();m2_2.off()
    sleep(5)
    m1_1.off();m1_2.on()
    m2_1.off();m2_2.on()
    sleep(5)
    m1_1.on();m1_2.on()
    m2_1.on();m2_2.on()
    sleep(5)
