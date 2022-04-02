from services.service import Service
from ui.ui import Ui

if __name__ == '__main__':
    s = Service()
    ui = Ui(s)
    ui.start()
