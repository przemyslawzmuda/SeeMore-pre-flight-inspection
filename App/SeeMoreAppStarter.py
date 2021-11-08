from SeeMorePfiAppController import AppController


class PfiAppStarter:
    appName = "SeeMore v0.1"

    def __init__(self):
        AppController().mainAppController()


if __name__ == "__main__":
    appStarter = PfiAppStarter()

