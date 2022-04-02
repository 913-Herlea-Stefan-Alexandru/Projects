#pragma once

#include "movieRepo.h"
#include "movieIterator.h"
#include "validator.h"

class UserService
{
private:

	MovieRepo& database;
	MovieRepo& watch_list;
	MovieRepo& filtered;

	MViterator it = this->filtered.iterator();

	Validator val;

public:
	UserService();

	UserService(MovieRepo& db, MovieRepo& wl, MovieRepo& fl);

	~UserService();

	//empties the filtered repo and fills it with the movies from the database repo that have the given genre(string), or all of them
	//if the genre is empty
	bool getGenre(std::string genre);

	//resets the iterator for the filtered repo
	void startOver();

	//returns the movie on the current position of the repo
	Movie getCurrent();

	//adds the movie on the current position of the iterator in the watch list repo
	int addCurrent();

	//gets to the next position of the iterator
	void cont();

	//removes the movie with the given title from the watch list while adding to it a like or not (y/n)
	int remove(std::string title, std::string like);

	vector<Movie> getWatchList();

	//returns a readable string of the watch list
	std::string writeWatchList();
};