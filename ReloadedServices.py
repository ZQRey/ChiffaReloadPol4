import win32serviceutil
import time
from ClearCache import startClear
from WriteFileLog import writeLog

servicesName = ("ChiffaDriverService"
                , "DriverManager2"
                , "DriverManager3"
                , "DriverManager4")


# Останавливаем службы
def stop_service(service):
    try:
        win32serviceutil.StopService(service)
        print(f"Service '{service}' stopped successfully.")
    except Exception as e:
        writeLog("service", service, f"Error stopping service '{service}': {e}")
        print(f"Error stopping service '{service}': {e}")


# Запускаем службы
def start_service(service):
    try:
        win32serviceutil.StartService(service)
        print(f"Service '{service}' started successfully.")
    except Exception as e:
        writeLog("service", service, f"Error starting service '{service}': {e}")
        print(f"Error starting service '{service}': {e}")


# Проверка статуса службы
def check_status(service):
    try:
        status = win32serviceutil.QueryServiceStatus(service)
        status_dict = {
            1: "Stopped",
            2: "Starting",
            3: "Stopping",
            4: "Running",
            5: "Continue Pending",
            6: "Pause Pending",
            7: "Paused"
        }
        print(f"Service '{service}' status: {status_dict.get(status[1], 'Unknown')}")
    except Exception as e:
        writeLog("service", service, f"Error checking status of service '{service}': {e}")
        print(f"Error checking status of service '{service}': {e}")


def work():
    for service in servicesName:
        stop_service(service)
    time.sleep(5)
    startClear()
    time.sleep(5)
    for service in servicesName:
        start_service(service)
