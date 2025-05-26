import os
from WriteFileLog import writeLog

# Пути удаления файлов в папке
foldersToClear = (r"C:\LIS\Manager\Logs"
                  , r"C:\LIS2\Manager\Logs"
                  , r"C:\LIS3\Manager\Logs"
                  , r"C:\LIS4\Manager\Logs")
errorFiles = (r"C:\LIS\Manager\error.xml"
              , r"C:\LIS2\Manager\errors.xml"
              , r"C:\LIS3\Manager\errors.xml"
              , r"C:\LIS4\Manager\errors.xml")


def clear_folder(folderPath):
    # Проверка пути
    if not os.path.exists(folderPath):
        writeLog("file", folderPath, f"Папка '{folderPath}' не существует.")
        print(f"Папка '{folderPath}' не существует.")
        return

    # Удаление всех файлов и папок внутри директории
    for item in os.listdir(folderPath):
        item_path = os.path.join(folderPath, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)  # Удаляем файл или символическую ссылку
                print(f"Файл удален: {item_path}")
        except Exception as e:
            writeLog("file", item_path, f"Ошибка при удалении '{item_path}': {e}")
            print(f"Ошибка при удалении '{item_path}': {e}")

    print(f"Все содержимое папки '{folderPath}' удалено.")


# Удаление файла ошибок
def clear_error_file(path_error_file):
    # Проверка существования файла
    if os.path.exists(path_error_file):
        os.remove(path_error_file)
        print(f"Файл '{path_error_file}' успешно удален.")
    else:
        writeLog("file", path_error_file, f"Файл '{path_error_file}' не найден.")
        print(f"Файл '{path_error_file}' не найден.")


def startClear():
    # Чистка кэша
    for folder in foldersToClear:
        clear_folder(folder)

    # Чистка файла ошибок
    for err_file in errorFiles:
        clear_error_file(err_file)