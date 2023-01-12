import time


t= int(input('Hello, I am a countdown timer. Please choose a time to countdown from (secs): '))
print('Ready') 
time.sleep(1)
print('Set') 
time.sleep(1)
print('Go!')
while t > 0:
    time.sleep(1)
    print(t)
    t -= 1
time.sleep(1)
print(0)
