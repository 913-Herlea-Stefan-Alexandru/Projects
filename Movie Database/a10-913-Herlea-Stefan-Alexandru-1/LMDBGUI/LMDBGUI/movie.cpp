#include "movie.h"
#include <Windows.h>
#include <shellapi.h>

Movie::Movie()
{
	this->year = 0;
	this->likes = 0;
}

Movie::Movie(string title, string genre, int year, int likes, string link)
: title(title), genre(genre), year(year), likes(likes), link(link)
{

}

Movie::~Movie()
{

}

string Movie::getTitle() const
{
	return this->title;
}

string Movie::getGenre() const
{
	return this->genre;
}

int Movie::getYear() const
{
	return this->year;
}

int Movie::getLikes() const
{
	return this->likes;
}

string Movie::getLink() const
{
	return this->link;
}

void Movie::setTitle(string newTitle)
{
	this->title = newTitle;
}

void Movie::setGenre(string newGenre)
{
	this->genre = newGenre;
}

void Movie::setYear(int newYear)
{
	this->year = newYear;
}

void Movie::setLikes(int newLikes)
{
	this->likes = newLikes;
}

void Movie::setLink(string newLink)
{
	this->link = newLink;
}

void Movie::runLink()
{
	ShellExecuteA(0, 0, this->link.c_str(), 0, 0, SW_SHOW);
}

string Movie::write_movie()
{
	string str = "";

	str += "\nTITLE: " + this->title + "\n" + "GENRE: " + this->genre + "\n" + "YEAR: " + to_string(this->year) + "\n" + "LIKES: " 
		+ to_string(this->likes) + "\n" + "TRAILER: " + this->link + "\n";

	return str;
}

vector<string> tokenize(string str, char delimiter)
{
	vector<string> result;
	stringstream ss(str);
	string token;
	while (getline(ss, token, delimiter))
		result.push_back(token);

	return result;
}

ostream& operator<<(ostream& output, const Movie& m) {
	output << m.title << "," << m.genre << "," << m.year << "," << m.likes << "," << m.link << '\n';
	return output;
}

istream& operator>>(istream& input, Movie& m) {
	string line;
	getline(input, line);

	vector<string> tokens = tokenize(line, ',');
	if (tokens.size() != 5)
		return input;

	m.title = tokens[0];
	m.genre = tokens[1];
	m.year = atoi(tokens[2].c_str());
	m.likes = atoi(tokens[3].c_str());
	m.link = tokens[4];

	return input;
}