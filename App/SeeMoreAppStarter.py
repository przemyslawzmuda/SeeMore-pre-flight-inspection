from SeeMorePfiAppController import AppController


class PfiAppStarter:
    APP_NAME = "SeeMore v0.1"

    def __init__(self):
        AppController().main_app_controller()


if __name__ == "__main__":
    app_starter = PfiAppStarter()
