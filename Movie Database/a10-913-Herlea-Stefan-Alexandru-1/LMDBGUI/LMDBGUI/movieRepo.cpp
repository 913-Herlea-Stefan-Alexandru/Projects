#include "movieRepo.h"
#include "movieIterator.h"
#include <fstream>

MovieRepo::MovieRepo(string file_name) : file_name{file_name}
{
	if (file_name != "")
		this->load();
}

int MovieRepo::add(Movie mv)
{
	int poz = -1;

	for (int i = 0; i < this->arr.length(); i++)
	{
		Movie mv_temp = this->arr[i];
		if (mv_temp.getTitle() == mv.getTitle())
		{
			poz = i;
			break;
		}
	}

	if (poz != -1)
	{
		throw RepoException("Movie already in list\n");
	}

	this->arr.add(mv);

	this->save();

	return 0;
}

int MovieRepo::remove(string title)
{
	int poz = -1;

	for (int i = 0; i < this->arr.length(); i++)
	{
		Movie mv_temp = this->arr[i];
		if (mv_temp.getTitle() == title)
		{
			poz = i;
			break;
		}
	}

	if (poz == -1)
	{
		throw RepoException("Movie not found\n");
	}

	this->arr.remove(poz);

	this->save();

	return 0;
}

int MovieRepo::update(string title, Movie mv)
{
	Movie* m = this->getAddress(title);
	
	if (mv.getTitle() != "")
		m->setTitle(mv.getTitle());
	if (mv.getGenre() != "")
		m->setGenre(mv.getGenre());
	if (mv.getYear() != 0)
		m->setYear(mv.getYear());
	if (mv.getLikes() != 0)
		m->setLikes(mv.getLikes());
	if (mv.getLink() != "")
		m->setLink(mv.getLink());

	this->save();

	return 0;
}

Movie MovieRepo::getObj(string title)
{
	for (Movie& m : this->arr)
	{
		if (m.getTitle() == title)
			return m;
	}
	throw RepoException("Movie not found\n");
}

Movie* MovieRepo::getAddress(string title)
{
	for (Movie& m : this->arr)
	{
		if (m.getTitle() == title)
			return &m;
	}
	throw RepoException("Movie not found\n");
}

int MovieRepo::length() const
{
	return this->arr.length();
}

void MovieRepo::filterGenre(string genre, MovieRepo& filtered)
{
	vector<Movie> filt = this->arr.filter([genre](Movie m)->bool { return (m.getGenre() == genre || genre == ""); });
	
	for (const Movie& m : filt)
	{
		filtered.add(m);
	}
}

MViterator MovieRepo::iterator() const
{
	return MViterator(*this);
}

Movie MovieRepo::getByIndex(int index)
{
	return this->arr[index];
}

void MovieRepo::emptyRepo()
{
	this->arr.clear();
}

void MovieRepo::save()
{
	if (this->file_name != "")
	{
		ofstream f(this->file_name);

		f << "";

		f.close();

		f.open(this->file_name, ios_base::app);

		for (Movie& m : this->arr)
		{
			f << m;
		}

		f.close();
	}
}

void MovieRepo::load()
{
	ifstream f(this->file_name);

	if (!f.is_open())
		return;

	Movie m;

	while (f >> m)
	{
		this->arr.add(m);
	}

	f.close();
}

vector<Movie> MovieRepo::getAll()
{
	vector<Movie> vec;
	copy(this->arr.begin(), this->arr.end(), back_inserter(vec));
	return vec;
}

string MovieRepo::write_list()
{
	string str = "";
	for (Movie& m : this->arr)
	{
		//str += m.write_movie() + "\n";
		cout << m << '\n';
	}

	return str;
}

RepoException::RepoException(string message) : message{message}
{
}

const char* RepoException::what() const noexcept
{
	return this->message.c_str();
}
