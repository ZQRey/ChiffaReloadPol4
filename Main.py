from ReloadedServices import work
from WriteFileLog import checkPath
from CheckStatus import check_status


def StartUp():
    checkPath()
    work()
    check_status()


if __name__ == "__main__":
    StartUp()
