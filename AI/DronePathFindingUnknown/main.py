from ui.UI import UI
from controller.controller import Controller
from model.Environment import Environment

if __name__ == '__main__':
    c = Controller(Environment())
    ui = UI(c)
    ui.start()
