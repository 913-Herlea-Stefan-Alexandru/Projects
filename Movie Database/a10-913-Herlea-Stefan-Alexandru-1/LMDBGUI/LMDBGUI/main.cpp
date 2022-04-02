#include "QtGui.h"
#include "movieRepo.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MovieRepo database("database.txt");
    AdminService admin(database);
    MovieRepo watchList("watch_list.txt");
    MovieRepo filtered;
    UserService user(database, watchList, filtered);
    QtGui w(admin, user);
    w.show();
    return a.exec();
}
