import os
import time

import ReloadedServices

def select() -> int:
    services = ReloadedServices.servicesName
    status = 0
    for service in services:
        print(f"Check status {service}")
        check = os.system(f"powershell -Command Get-Service {service} >nul 2>&1")
        if check != 0:
            status = check
    return status

def check_status():
    time.sleep(60)
    result = select()
    if result == 0:
        return "Ok, services is all run."
    else:
        os.system("shutdown -r -t 30")
