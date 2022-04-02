#pragma once
#include <qwidget.h>
#include <QListWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QTextEdit>
#include <QPushButton>
#include <QLabel>
#include "QtAdmin.h"
#include "QtUser.h"

class QtGui : public QWidget
{
	Q_OBJECT

public:

	QtGui(AdminService& admin, UserService& user);
	~QtGui();

private:

	UserService& user;
	AdminService& admin;
	QPushButton* adminButton;
	QPushButton* userButton;
	QtAdmin* adminGui;
	QtUser* userGui;

	void init();

	void makeConnections();

	void showAdmin();

	void showUser();
};