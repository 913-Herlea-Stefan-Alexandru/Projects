#pragma once
#include <qwidget.h>
#include <QListWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QTextEdit>
#include <QPushButton>
#include <QLabel>
#include <QTableWidget>
#include <QShortcut>
#include <QKeySequence>
#include "admin_service.h"

class QtAdmin : public QWidget
{
	Q_OBJECT

public:
	QtAdmin(AdminService& admin);
	~QtAdmin();

private:

	AdminService& admin;
	QTableWidget* table;
	QPushButton* addMovie;
	QPushButton* removeMovie;
	QPushButton* updateMovie;
	QPushButton* undo;
	QPushButton* redo;
	QLineEdit* title;
	QLineEdit* genre;
	QLineEdit* year;
	QLineEdit* likes;
	QLineEdit* link;
	QShortcut* undoShortcut;
	QShortcut* redoShortcut;

	void init();

	void makeConnections();

	void populateTable();

	void add();

	void remove();

	void update();

	void loadDetails();
};

