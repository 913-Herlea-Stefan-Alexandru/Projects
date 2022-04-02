#pragma once

#include <string>
#include <exception>
#include "movie.h"

using namespace std;

class ValidatorException : public exception
{
private:
	string message;

public:
	ValidatorException(string message);

	const char* what() const noexcept override;
};

class Validator
{
private:

public:

	bool validate_integer(string integer);

	int validate_title(string title);

	int validate_genre(string genre);

	int validate_year(string year);

	int validate_likes(string likes);

	int validate_link(string link);
};