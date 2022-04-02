#include "movie.h"
#include "admin_service.h"
#include <exception>

AdminService::AdminService(MovieRepo &repo)
: repo(repo)
{

}

AdminService::~AdminService()
{

}

int AdminService::add_movie(string title, string genre, string year, string likes, string link)
{
	int year_i = 0, likes_i = 0;

	if (this->val.validate_year(year) || this->val.validate_likes(likes))
		return 2;

	if (this->val.validate_title(title) == 1)
		return 3;

	if (this->val.validate_genre(genre) == 1)
		return 4;

	if (this->val.validate_link(link) == 1)
		return 5;

	if (year != "")
	{
		year_i = atoi(year.c_str());
	}
	if (likes != "")
	{
		likes_i = atoi(likes.c_str());
	}

	Movie mv(title, genre, year_i, likes_i, link);

	int r = 0;
	r = this->repo.add(mv);

	if (r == 0)
	{
		this->undo.push_back(make_unique<UndoAdd>(this->repo, mv));
		this->redo.clear();
	}
	return r;
}

int AdminService::remove_movie(string title)
{
	if (this->val.validate_title(title) == 1)
		return 3;

	int r = 0;

	Movie m = this->repo.getObj(title);
	r = this->repo.remove(title);

	if (r == 0)
	{
		this->undo.push_back(make_unique<UndoDelete>(this->repo, m));
		this->redo.clear();
	}

	return r;
}

int AdminService::update_movie(string title, string new_title, string new_genre, string new_year, string new_likes, string new_link)
{
	int year_i = 0, likes_i = 0;
	if (new_year != "")
	{
		if (this->val.validate_year(new_year))
			return 2;
		year_i = atoi(new_year.c_str());
	}
	if (new_likes != "")
	{
		if (this->val.validate_likes(new_likes))
			return 2;
		likes_i = atoi(new_likes.c_str());
	}

	Movie m;

	if (new_title != "")
		m.setTitle(new_title);
	if (new_genre != "")
		m.setGenre(new_genre);
	if (new_year != "")
		m.setYear(year_i);
	if (new_likes != "")
		m.setLikes(likes_i);
	if (new_link != "")
	{
		if (this->val.validate_link(new_link) == 1)
			return 5;
		m.setLink(new_link);
	}

	Movie mv = this->repo.getObj(title);

	this->repo.update(title, m);

	this->undo.push_back(make_unique<UndoUpdate>(this->repo, title, m, mv));
	this->redo.clear();

	return 0;
}

vector<Movie> AdminService::getAll()
{
	return this->repo.getAll();
}

string AdminService::write_list()
{
	return this->repo.write_list();
}

void AdminService::Undo()
{
	if (undo.size() == 0)
	{
		throw RepoException("Nothing to undo");
	}
	undo.back()->DoUndo();
	redo.push_back(move(undo.back()));
	undo.pop_back();
}

void AdminService::Redo()
{
	if (redo.size() == 0)
	{
		throw RepoException("Nothing to redo");
	}
	redo.back()->DoRedo();
	undo.push_back(move(redo.back()));
	redo.pop_back();
}
