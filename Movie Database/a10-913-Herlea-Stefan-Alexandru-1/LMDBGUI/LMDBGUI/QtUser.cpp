#include "QtUser.h"

QtUser::QtUser(UserService& user) : user{ user }
{
	this->init();
	this->makeConnections();
	//this->populateTable();
}

QtUser::~QtUser()
{
}

void QtUser::init()
{
	this->setWindowTitle("User Menu");
	this->resize(1500, 500);

	QHBoxLayout* layout = new QHBoxLayout(this);

	QWidget* leftSide = new QWidget();
	QVBoxLayout* vLayout = new QVBoxLayout(leftSide);

	//this->table = new QTableWidget();
	//vLayout->addWidget(this->table);

	//table view
	this->tableModel = new TableModel(this->user);
	QWidget* tableViewWidget = new QWidget();
	this->tableView = new QTableView(tableViewWidget);
	this->tableView->setModel(tableModel);
	this->tableView->setSortingEnabled(true);
	this->tableView->resizeColumnsToContents();
	vLayout->addWidget(this->tableView);

	this->removeMovie = new QPushButton("Remove Movie");
	vLayout->addWidget(this->removeMovie);

	layout->addWidget(leftSide);

	QWidget* rightSide = new QWidget();
	vLayout = new QVBoxLayout(rightSide);

	QWidget* topRight = new QWidget();
	QFormLayout* fLayout = new QFormLayout(topRight);

	this->filter = new QLineEdit();
	QLabel* filterLabel = new QLabel("&Filter Genre:");
	filterLabel->setBuddy(this->filter);
	fLayout->addRow(filterLabel, this->filter);

	vLayout->addWidget(topRight);

	this->filterButton = new QPushButton("Filter");
	vLayout->addWidget(this->filterButton);

	this->currentMovie = new QLineEdit();
	this->currentMovie->setReadOnly(true);
	QPalette* palette = new QPalette();
	this->currentMovie->setPalette(*palette);
	vLayout->addWidget(this->currentMovie);

	this->addMovie = new QPushButton("Add to watch list");
	vLayout->addWidget(this->addMovie);

	this->viewTrailer = new QPushButton("View Trailer");
	vLayout->addWidget(this->viewTrailer);

	this->nextMovie = new QPushButton("Next Movie");
	vLayout->addWidget(this->nextMovie);

	layout->addWidget(rightSide);

	//dialog box
	this->dialog = new QDialog(this);

	QVBoxLayout* diagLayout = new QVBoxLayout(dialog);

	QLabel* question = new QLabel("Did you like the movie?");

	diagLayout->addWidget(question);

	QWidget* buttonsWidget = new QWidget();
	QHBoxLayout* buttons = new QHBoxLayout(buttonsWidget);

	QPushButton* yes = new QPushButton("Yes");
	QPushButton* no = new QPushButton("No");

	buttons->addWidget(yes);
	buttons->addWidget(no);

	diagLayout->addWidget(buttonsWidget);

	QObject::connect(yes, &QPushButton::clicked, [=]() { this->dialog->accept(); });
	QObject::connect(no, &QPushButton::clicked, [=]() { this->dialog->reject(); });
}

void QtUser::makeConnections()
{
	QObject::connect(this->filterButton, &QPushButton::clicked, this, &QtUser::filterF);
	QObject::connect(this->addMovie, &QPushButton::clicked, this, &QtUser::add);
	QObject::connect(this->addMovie, &QPushButton::clicked, this, &QtUser::add);
	QObject::connect(this->nextMovie, &QPushButton::clicked, this, &QtUser::next);
	QObject::connect(this->removeMovie, &QPushButton::clicked, this, &QtUser::remove);
	QObject::connect(this->viewTrailer, &QPushButton::clicked, this, &QtUser::trailer);

	QObject::connect(this->dialog, &QDialog::accepted, this, &QtUser::liked);
	QObject::connect(this->dialog, &QDialog::rejected, this, &QtUser::disliked);
}

void QtUser::populateTable()
{
	this->table->clear();
	this->table->setColumnCount(5);
	this->table->setRowCount(this->user.getWatchList().size());
	this->table->setHorizontalHeaderLabels({ "Title", "Genre", "Year", "Likes", "Link" });
	this->table->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents);
	int currentRow = 0;
	for (Movie& m : this->user.getWatchList())
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

void QtUser::filterF()
{
	this->user.startOver();
	if (this->user.getGenre(this->filter->text().toStdString()))
	{
		Movie m = this->user.getCurrent();
		this->currentMovie->setText(QString::fromStdString(m.getTitle()));
	}
}

void QtUser::add()
{
	try
	{
		this->user.addCurrent();
		this->tableModel->insertRow(this->tableModel->rowCount());
		//this->populateTable();
	}
	catch (...)
	{

	}
}

void QtUser::next()
{
	this->user.cont();
	Movie m = this->user.getCurrent();
	this->currentMovie->setText(QString::fromStdString(m.getTitle()));
}

void QtUser::remove()
{
	dialog->exec();
}

void QtUser::liked()
{
	//QTableWidgetItem* item = this->table->item(this->table->currentRow(), 0);
	//this->user.remove(item->text().toStdString(), "y");
	QModelIndex ind = this->tableView->currentIndex();
	this->user.remove(this->tableModel->data(ind, 99).toString().toStdString(), "y");
	//this->tableModel->removeRows(ind.row(), 1, QModelIndex());
	//this->tableModel->removeRow(this->tableModel->rowCount());
	//this->populateTable();
}

void QtUser::disliked()
{
	//QTableWidgetItem* item = this->table->item(this->table->currentRow(), 0);
	//this->user.remove(item->text().toStdString(), "n");
	QModelIndex ind = this->tableView->currentIndex();
	this->user.remove(this->tableModel->data(ind, 99).toString().toStdString(), "n");
	//this->tableModel->removeRow(ind.row());
	//this->populateTable();
}

void QtUser::trailer()
{
	Movie m = this->user.getCurrent();
	m.runLink();
}
