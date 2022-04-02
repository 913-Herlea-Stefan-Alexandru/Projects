from ui.ui import Ui
from services.service import Service
from domain.graph import Graph

if __name__ == '__main__':
    graph = Graph()
    service = Service(graph)
    ui = Ui(service)
    ui.start()