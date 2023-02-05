# Requirements
1. Add multiple *undo* and *redo* functionality for the `add`, `remove`, and `update` operations. Implement this 
functionality using inheritance and polymorphism. You will have **Undo** and **Redo** buttons on the GUI, as well 
as a key combination to undo and redo the operations (e.g. `Ctrl+Z`, `Ctrl+Y`).

2. Show the contents of the `adoption list` / `movie watch list` / `shopping basket` / `tutorial watch list` using 
a table view. You must use the [Qt View/Model](https://doc.qt.io/qt-5/modelview.html) components (`QTableView`). 
Create your own model – a class which inherits from [`QAbstractTableModel`](https://doc.qt.io/qt-5/qabstracttablemodel.html).
