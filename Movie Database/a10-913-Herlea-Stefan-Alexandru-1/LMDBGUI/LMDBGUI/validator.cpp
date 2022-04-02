#include "validator.h"

bool Validator::validate_integer(string integer)
{
	string::const_iterator it = integer.begin();
	while (it != integer.end() && isdigit(*it))
		it++;
	return (!integer.empty() && it == integer.end());
}

int Validator::validate_title(string title)
{
	if (title == "")
		throw ValidatorException("Title must not be empty\n");
	return 0;
}

int Validator::validate_genre(string genre)
{
	if (genre == "")
		throw ValidatorException("Genre must not be empty\n");
	return 0;
}

int Validator::validate_year(string year)
{
	if (!this->validate_integer(year) || atoi(year.c_str()) < 0)
		throw ValidatorException("Year must be a greater than 0 integer\n");
	return 0;
}

int Validator::validate_likes(string likes)
{
	if (!this->validate_integer(likes) || atoi(likes.c_str()) < 0)
		throw ValidatorException("Likes must be a greater than 0 integer\n");
	return 0;
}

int Validator::validate_link(string link)
{
	if (link == "")
		throw ValidatorException("Link must not be empty\n");
	if (link[0] != 'h' || link[1] != 't' || link[2] != 't' || link[3] != 'p' || link[4] != 's' || link[5] != ':')
		throw ValidatorException("Link must be of format: https:....\n");
	return 0;
}

ValidatorException::ValidatorException(string message) : message{message}
{
}

const char* ValidatorException::what() const noexcept
{
	return this->message.c_str();
}
