#pragma once
#include "movieRepo.h"


class MovieRepoHTML : public MovieRepo
{
private:
	string html_file;

public:
	MovieRepoHTML(string file_name = "", string html_file = "");

	void save() override;

	string write_list() override;
};