#pragma once
#include <string>
#include "movieRepo.h"
#include "validator.h"

using namespace std;

class Undo {
public:
	virtual void DoUndo() = 0;
	virtual void DoRedo() = 0;
	virtual ~Undo() = default;
};

class UndoAdd : public Undo {
	Movie m;
	MovieRepo& repo;
public:
	UndoAdd(MovieRepo& repo, const Movie& m) : repo{ repo }, m{ m } {}
	void DoUndo() override {
		repo.remove(m.getTitle());
	}
	void DoRedo() override {
		repo.add(m);
	}
};

class UndoDelete : public Undo {
	Movie m;
	MovieRepo& repo;
public:
	UndoDelete(MovieRepo& repo, const Movie& m) noexcept : repo{ repo }, m{ m } {}
	void DoUndo() override {
		repo.add(m);
	}
	void DoRedo() override {
		repo.remove(m.getTitle());
	}
};

class UndoUpdate : public Undo {
	Movie m;
	Movie mv;
	std::string title;
	MovieRepo& repo;
public:
	UndoUpdate(MovieRepo& repo, std::string title, const Movie& m, const Movie& mv) : repo{ repo }, title{ title }, m{ m }, mv{ mv } {};
	void DoUndo() override {
		repo.update(title, m);
	}
	void DoRedo() override {
		repo.update(m.getTitle(), mv);
	}
};

class AdminService
{
private:

	MovieRepo &repo;
	Validator val;

	vector<unique_ptr<Undo>> undo;
	vector<unique_ptr<Undo>> redo;

public:

	//the constructor of the admin service class
	//it passes the given repo to this class's instance of a repo
	AdminService(MovieRepo &repo);

	//the destructor of the class
	~AdminService();

	//adds a movie with a given title(string), genre(string), year(int), likes(int) and link(string) to the current repo
	int add_movie(string title, string genre, string year, string likes, string link);

	//deletes a movie with the given title(string) from the current repo
	int remove_movie(string title);

	//updates the movie with the given title(string) from the current repo with the given new_title(string), 
	//new_genre(string), new_year(int), new_likes(int) and new_link(string)
	//if any of those fields contain an empty string, then the program doesn't change the coresponding variable
	int update_movie(string title, string new_title, string new_genre, string new_year, string new_likes, string new_link);

	vector<Movie> getAll();

	//returns a readable version of the current repo
	string write_list();

	void Undo();

	void Redo();
};