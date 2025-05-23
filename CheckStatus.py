import os
import time


def select() -> int:
    check_one = os.system("powershell -Command Get-Service wuauserv >nul 2>&1")
    check_two = os.system("powershell -Command Get-Service wuauserv >nul 2>&1")
    check_tree = os.system("powershell -Command Get-Service wuauserv >nul 2>&1")
    check_four = os.system("powershell -Command Get-Service wuauserv >nul 2>&1")
    if check_one == 0 and check_two == 0 and check_tree == 0 and check_four == 0:
        return 0
    else:
        return 1

def check_status():
    time.sleep(60)
    result = select()
    if result == 0:
        return "Ok, services is all run."
    else:
        os.system("shutdown -r -t 30")