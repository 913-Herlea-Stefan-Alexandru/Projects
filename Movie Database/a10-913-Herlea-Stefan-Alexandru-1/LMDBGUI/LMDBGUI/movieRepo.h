#pragma once

#include "movie.h"
#include "dynamic_array.h"

class MViterator;

class RepoException : public exception
{
private:
	string message;

public:
	RepoException(string message);

	const char* what() const noexcept override;
};

class MovieRepo
{
	friend class MViterator;

protected:

	DynamicArray<Movie> arr;
	string file_name = "";

public:

	MovieRepo(string file_name = "");
	
	//adds the given movie to the repo
	int add(Movie mv);

	//removes a movie with a given title(string) from the repo
	int remove(string title);

	int update(string title, Movie mv);

	//returns a movie with the given title(string) from the repo
	Movie getObj(string title);

	//returns the address of the movie with the given title
	Movie* getAddress(string title);

	int length() const;

	//fills the filtered repo with the movies with the given genre from the current repo, or with all of the movies
	//of the given repo if the genre string is empty
	void filterGenre(string genre, MovieRepo& filtered);

	//returns the iterator of the repo
	MViterator iterator() const;

	//returns a movie by its index in the array of the repo
	Movie getByIndex(int index);

	//empties the current repo
	void emptyRepo();

	virtual void save();

	void load();

	vector<Movie> getAll();

	//returns a readable string of the whole repo
	virtual string write_list();
};