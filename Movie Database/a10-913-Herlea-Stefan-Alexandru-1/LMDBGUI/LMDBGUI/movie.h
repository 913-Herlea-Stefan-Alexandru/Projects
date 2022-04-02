#pragma once
#include <vector>
#include <sstream>
#include <string>
#include <iostream>

using namespace std;

class Movie
{
private:
	
	string title;
	string genre;
	string link;
	int year = 0, likes = 0;

public:

	Movie();

	Movie(string title, string genre, int year, int likes, string link);

	~Movie();

	string getTitle() const;

	string getGenre() const;

	int getYear() const;

	int getLikes() const;

	string getLink() const;

	void setTitle(string newTitle);

	void setGenre(string newGenre);

	void setYear(int newYear);

	void setLikes(int newLikes);

	void setLink(string newLink);

	void runLink();

	string write_movie();

	friend ostream& operator<<(ostream& output, const Movie& m);

	friend istream& operator>>(istream& input, Movie& m);
};