import os
from datetime import datetime

path_write_file = r"C:\LogReload"
log_name = "log.txt"
statusLog = True


def statusServices(service, status):
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(os.path.join(path_write_file, log_name), 'a', encoding='utf-8') as file:
        file.write(f"{now}\tСлужба: {service}\tСтатус перезапуска: {status}" + "\n")


def statusClearCache(file, status):
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(os.path.join(path_write_file, log_name), 'a', encoding='utf-8') as file:
        file.write(f"{now}\tФайл: {file}\tСтатус удаления: {status}" + "\n")


def checkPath():
    try:
        if not os.path.exists(path_write_file):
            os.mkdir(path_write_file)
        if not os.path.exists(log_name):
            with open(log_name, 'w') as file:
                pass
        statusLog = True
    except Exception as e:
        statusLog = False
        print(f"Ошибка создания файла {e}")


def writeLog(type_write, name, status):
    checkPath()
    if statusLog is True:
        if type_write == "service":
            statusServices(name, status)
        elif type_write == "file":
            statusClearCache(name, status)
        else:
            print("Ошибка вводных данных")
    else:
        print("Ошибка проверки пути/файла")

writeLog("service", "Test", "testing")