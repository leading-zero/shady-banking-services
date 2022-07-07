import backend
import frontend


class Application:
    def __init__(self):
        self.__backend = backend.BackEnd("data.csv")
        self.__frontend = frontend.FrontEnd(self.__backend)


app = Application()
