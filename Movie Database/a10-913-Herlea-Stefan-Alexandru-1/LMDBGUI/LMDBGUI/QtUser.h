#pragma once
#include <qwidget.h>
#include <QListWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QTextEdit>
#include <QPushButton>
#include <QLabel>
#include <QTableWidget>
#include <QDialog>
#include <QAbstractTableModel>
#include "user_service.h"

class TableModel : public QAbstractTableModel
{
	Q_OBJECT

private:

	UserService& user;

public:

	TableModel(UserService& user, QObject* parent = nullptr) : user{ user }, QAbstractTableModel(parent)
	{
	}
	~TableModel() {}

	int rowCount(const QModelIndex& parent = QModelIndex{}) const override
	{
		return this->user.getWatchList().size();
	}

	int columnCount(const QModelIndex& parent = QModelIndex{}) const override
	{
		return 5;
	}

	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override
	{
		int row = index.row();
		int column = index.column();

		vector<Movie> movies = this->user.getWatchList();

		Movie m = movies[row];

		if (role == 99)
		{
			return index.siblingAtColumn(0).data();
		}
		if (role == Qt::DisplayRole || role == Qt::EditRole)
		{
			switch (column)
			{
			case 0:
				return QString::fromStdString(m.getTitle());
			case 1:
				return QString::fromStdString(m.getGenre());
			case 2:
				return QString::fromStdString(to_string(m.getYear()));
			case 3:
				return QString::fromStdString(to_string(m.getLikes()));
			case 4:
				return QString::fromStdString(m.getLink());
			default:
				break;
			}
		}
		if (role == Qt::FontRole)
		{
			QFont font("Times", 15, 10, true);
			font.setItalic(false);
			return font;
		}
		if (role == Qt::BackgroundRole)
		{
			if (row % 2 == 1)
			{
				return QBrush{ QColor{0, 100, 250} };
			}
		}

		return QVariant();
	}

	QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override
	{
		if (role == Qt::DisplayRole)
		{
			if (orientation == Qt::Horizontal)
			{
				switch (section)
				{
				case 0:
					return QString{ "Title" };
				case 1:
					return QString{ "Genre" };
				case 2:
					return QString{ "Year" };
				case 3:
					return QString{ "Likes" };
				case 4:
					return QString{ "Link" };
				default:
					break;
				}
			}
		}
		if (role == Qt::FontRole)
		{
			QFont font("Times", 15, 10, true);
			font.setBold(true);
			font.setItalic(false);
			return font;
		}

		return QVariant{};
	}

	bool insertRows(int row, int count, const QModelIndex& parent = QModelIndex()) override
	{
		beginInsertRows(parent, row, row + count - 1);
		endInsertRows();
		return true;
	}

	bool removeRows(int row, int count, const QModelIndex& parent = QModelIndex()) override
	{
		beginRemoveRows(parent, row, row + count - 1);
		endRemoveRows();
		return true;
	}

	Qt::ItemFlags flags(const QModelIndex& index) const override
	{
		return Qt::ItemIsSelectable | Qt::ItemIsEnabled;
	}

};

class QtUser : public QWidget
{
	Q_OBJECT

public:
	QtUser(UserService& user);
	~QtUser();

private:

	UserService& user;
	QTableWidget* table;
	QPushButton* addMovie;
	QPushButton* removeMovie;
	QPushButton* nextMovie;
	QPushButton* viewTrailer;
	QPushButton* filterButton;
	QLineEdit* filter;
	QLineEdit* currentMovie;
	QDialog* dialog;

	TableModel* tableModel;
	QTableView* tableView;

	void init();

	void makeConnections();

	void populateTable();

	void filterF();

	void add();

	void next();

	void remove();

	void liked();

	void disliked();

	void trailer();
};

