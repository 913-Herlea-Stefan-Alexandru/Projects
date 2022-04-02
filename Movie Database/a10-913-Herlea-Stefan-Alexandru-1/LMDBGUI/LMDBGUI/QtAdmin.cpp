#include "QtAdmin.h"

QtAdmin::QtAdmin(AdminService& admin) : admin{ admin }
{
	this->init();
	this->makeConnections();
	this->populateTable();
}

QtAdmin::~QtAdmin()
{
}

void QtAdmin::init()
{
	this->setWindowTitle("Admin Menu");

	this->undoShortcut = new QShortcut(QKeySequence(tr("Ctrl+Z")), this);
	this->redoShortcut = new QShortcut(QKeySequence(tr("Ctrl+Y")), this);

	QHBoxLayout* layout = new QHBoxLayout(this);

	this->table = new QTableWidget();
	layout->addWidget(this->table);

	QWidget* topRightW = new QWidget();
	QVBoxLayout* topRightL = new QVBoxLayout(topRightW);

	QWidget* form = new QWidget();
	QFormLayout* fLayout = new QFormLayout(form);

	this->title = new QLineEdit();
	QLabel* titleL = new QLabel("&Title");
	this->genre = new QLineEdit();
	QLabel* genreL = new QLabel("&Genre");
	this->year = new QLineEdit();
	QLabel* yearL = new QLabel("&Year");
	this->likes = new QLineEdit();
	QLabel* likesL = new QLabel("&Likes");
	this->link = new QLineEdit();
	QLabel* linkL = new QLabel("&Link");

	titleL->setBuddy(this->title);
	genreL->setBuddy(this->genre);
	yearL->setBuddy(this->year);
	likesL->setBuddy(this->likes);
	linkL->setBuddy(this->link);

	fLayout->addRow(titleL, this->title);
	fLayout->addRow(genreL, this->genre);
	fLayout->addRow(yearL, this->year);
	fLayout->addRow(likesL, this->likes);
	fLayout->addRow(linkL, this->link);

	topRightL->addWidget(form);

	QWidget* buttonsWidget = new QWidget();
	QVBoxLayout* buttons = new QVBoxLayout(buttonsWidget);

	this->addMovie = new QPushButton("Add Movie");
	this->removeMovie = new QPushButton("Remove Movie");
	this->updateMovie = new QPushButton("Update Movie");
	this->undo = new QPushButton("Undo");
	this->redo = new QPushButton("Redo");
	buttons->addWidget(this->addMovie);
	buttons->addWidget(this->removeMovie);
	buttons->addWidget(this->updateMovie);
	buttons->addWidget(this->undo);
	buttons->addWidget(this->redo);

	topRightL->addWidget(buttonsWidget);

	layout->addWidget(topRightW);
}

void QtAdmin::makeConnections()
{
	QObject::connect(this->addMovie, &QPushButton::clicked, this, &QtAdmin::add);
	QObject::connect(this->removeMovie, &QPushButton::clicked, this, &QtAdmin::remove);
	QObject::connect(this->updateMovie, &QPushButton::clicked, this, &QtAdmin::update);
	QObject::connect(this->undo, &QPushButton::clicked, [=]() { try { this->admin.Undo(); this->populateTable(); } catch (...) {} });
	QObject::connect(this->redo, &QPushButton::clicked, [=]() { try { this->admin.Redo(); this->populateTable(); } catch (...) {} });

	QObject::connect(this->table, &QTableWidget::itemSelectionChanged, this, &QtAdmin::loadDetails);
	QObject::connect(this->table, &QTableWidget::cellDoubleClicked, this, &QtAdmin::loadDetails);

	QObject::connect(this->undoShortcut, &QShortcut::activated, [=]() { try { this->admin.Undo(); this->populateTable(); } catch (...) {} });
	QObject::connect(this->redoShortcut, &QShortcut::activated, [=]() { try { this->admin.Redo(); this->populateTable(); } catch (...) {} });
}

void QtAdmin::populateTable()
{
	this->table->clear();
	this->table->setColumnCount(5);
	this->table->setRowCount(this->admin.getAll().size());
	this->table->setHorizontalHeaderLabels({ "Title", "Genre", "Year", "Likes", "Link" });
	this->table->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents);
	int currentRow = 0;
	for (Movie& m : this->admin.getAll())
	{
		QTableWidgetItem* title = new QTableWidgetItem(QString::fromStdString(m.getTitle()));
		//title->setText(QString::fromStdString(m.getTitle()));
		//title->setAlignment(Qt::AlignCenter);
		this->table->setItem(currentRow, 0, title);

		QTableWidgetItem* genre = new QTableWidgetItem(QString::fromStdString(m.getGenre()));
		//genre->setText(QString::fromStdString(m.getGenre()));
		//genre->setAlignment(Qt::AlignCenter);
		this->table->setItem(currentRow, 1, genre);

		QTableWidgetItem* year = new QTableWidgetItem(QString::fromStdString(std::to_string(m.getYear())));
		//year->setText(QString::fromStdString(std::to_string(m.getYear())));
		//year->setAlignment(Qt::AlignCenter);
		this->table->setItem(currentRow, 2, year);

		QTableWidgetItem* likes = new QTableWidgetItem(QString::fromStdString(std::to_string(m.getLikes())));
		//likes->setText(QString::fromStdString(std::to_string(m.getLikes())));
		//likes->setAlignment(Qt::AlignCenter);
		this->table->setItem(currentRow, 3, likes);

		QTableWidgetItem* link = new QTableWidgetItem(QString::fromStdString(m.getLink()));
		//link->setText(QString::fromStdString(m.getLink()));
		//link->setAlignment(Qt::AlignCenter);
		this->table->setItem(currentRow, 4, link);

		currentRow++;
	}
}

void QtAdmin::add()
{
	string t = this->title->text().toStdString();
	string g = this->genre->text().toStdString();
	string y = this->year->text().toStdString();
	string li = this->likes->text().toStdString();
	string lk = this->link->text().toStdString();

	try
	{
		this->admin.add_movie(t, g, y, li, lk);
		this->populateTable();
	}
	catch (...)
	{

	}
}

void QtAdmin::remove()
{
	if (!this->table->selectedItems().isEmpty())
	{
		QTableWidgetItem* item = this->table->item(this->table->currentRow(), 0);
		try
		{
			this->admin.remove_movie(item->text().toStdString());
			this->populateTable();
		}
		catch (...)
		{

		}
	}
}

void QtAdmin::update()
{
	if (!this->table->selectedItems().isEmpty())
	{
		QTableWidgetItem* item = this->table->item(this->table->currentRow(), 0);
		string t = this->title->text().toStdString();
		string g = this->genre->text().toStdString();
		string y = this->year->text().toStdString();
		string li = this->likes->text().toStdString();
		string lk = this->link->text().toStdString();
		try
		{
			this->admin.update_movie(item->text().toStdString(), t, g, y, li, lk);
			this->populateTable();
		}
		catch (...)
		{

		}
	}
}

void QtAdmin::loadDetails()
{
	if (this->table->selectedItems().isEmpty())
	{
		this->title->setText("");
		this->genre->setText("");
		this->likes->setText("");
		this->link->setText("");
	}
	else
	{
		QTableWidgetItem* item = this->table->item(this->table->currentRow(), 0);
		this->title->setText(item->text());
		item = this->table->item(this->table->currentRow(), 1);
		this->genre->setText(item->text());
		item = this->table->item(this->table->currentRow(), 2);
		this->year->setText(item->text());
		item = this->table->item(this->table->currentRow(), 3);
		this->likes->setText(item->text());
		item = this->table->item(this->table->currentRow(), 4);
		this->link->setText(item->text());
	}
}
