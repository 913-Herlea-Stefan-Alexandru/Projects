from ui.ui import Ui
from service.service import Service

if __name__ == '__main__':
    s = Service()
    u = Ui(s)
    u.start()
