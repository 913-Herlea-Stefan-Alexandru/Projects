#include "QtGui.h"

QtGui::QtGui(AdminService& admin, UserService& user) : admin{ admin }, user{ user }
{
	this->init();
	this->makeConnections();
}

QtGui::~QtGui()
{
}

void QtGui::init()
{
	this->setWindowTitle("Main menu");
	this->resize(400, 150);

	QVBoxLayout* layout = new QVBoxLayout(this);

	this->adminButton = new QPushButton("Admin");
	layout->addWidget(this->adminButton);

	this->userButton = new QPushButton("User");
	layout->addWidget(this->userButton);
}

void QtGui::makeConnections()
{
	QObject::connect(this->adminButton, &QPushButton::clicked, this, &QtGui::showAdmin);
	QObject::connect(this->userButton, &QPushButton::clicked, this, &QtGui::showUser);
}

void QtGui::showAdmin()
{
	this->adminGui = new QtAdmin(this->admin);
	this->adminGui->show();
}

void QtGui::showUser()
{
	this->userGui = new QtUser(this->user);
	this->userGui->show();
}
