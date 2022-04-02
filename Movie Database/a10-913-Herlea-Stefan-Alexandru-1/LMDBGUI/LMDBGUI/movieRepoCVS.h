#pragma once
#include "movieRepo.h"


class MovieRepoCSV : public MovieRepo
{
private:
	string csv_file;

public:
	MovieRepoCSV(string file_name = "", string csv_file = "");

	void save() override;

	string write_list() override;
};