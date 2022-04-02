#include "user_service.h"

UserService::UserService(MovieRepo& db, MovieRepo& wl, MovieRepo& fl) : database{db}, watch_list{wl}, filtered{fl}
{

}

UserService::~UserService()
{
	
}


bool UserService::getGenre(std::string genre)
{
	this->database.filterGenre(genre, this->filtered);

	if (this->filtered.length() == 0)
		return false;

	return true;
}

void UserService::startOver()
{
	this->filtered.emptyRepo();
	this->it.first();
}

Movie UserService::getCurrent()
{
	int pos = this->it.getPos();

	Movie mv = this->filtered.getByIndex(pos);

	return mv;
}

int UserService::addCurrent()
{
	int pos = this->it.getPos();

	if (pos == -1)
		throw RepoException("");

	Movie mv = this->filtered.getByIndex(pos);

	return this->watch_list.add(mv);
}

void UserService::cont()
{
	if (!this->it.next())
	{
		this->it.first();
	}
}

int UserService::remove(std::string title, std::string like)
{
	if (this->val.validate_title(title) == 1)
		return 1;
	if (like == "y" || like == "Y")
	{
		Movie* mv = this->database.getAddress(title);
		if (mv != NULL)
			mv->setLikes(mv->getLikes() + 1);
	}
	else if (like != "n" && like != "N")
		return 2;
	return this->watch_list.remove(title);
}

vector<Movie> UserService::getWatchList()
{
	return this->watch_list.getAll();
}

std::string UserService::writeWatchList()
{
	return this->watch_list.write_list();
}
