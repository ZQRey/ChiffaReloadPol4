
from ReloadedServices import work
from WriteFileLog import checkPath


def StartUp():
    checkPath()
    work()


if __name__ == "__main__":
    StartUp()
