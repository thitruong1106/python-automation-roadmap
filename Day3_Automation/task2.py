#11/09/2025

"""
    Write a scripts that prints "ALERT!" every 3 seoncds for 15 seconds
    in between alerts, print how many seconds remain until next alert. 
    """

import time 

cooldown = 3
last_alert = 0 
end = time.time() + 15 #end time, is 15 seconds
while time.time() <= end: 
    now = time.time() #get current time 
    if now - last_alert >= cooldown:
        print("Alert!")
        last_alert = now
    else:
        remaining = cooldown - (now - last_alert)
        print(f"{remaining:.1f} seconds till alert")
    time.sleep(1)
