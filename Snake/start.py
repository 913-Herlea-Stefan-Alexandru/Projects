from UI.ui import Ui
from entities.board import Board
from services.settings import Settings

if __name__ == '__main__':
    st = Settings()
    size = st.dim
    apples = st.apples
    board = Board(size, apples)
    ui = Ui(board)
    ui.start()