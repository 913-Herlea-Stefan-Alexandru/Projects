#include "movieRepoCVS.h"
#include <iostream>
#include <fstream>

MovieRepoCSV::MovieRepoCSV(string file_name, string csv_file) : MovieRepo(file_name), csv_file{csv_file}
{
}

void MovieRepoCSV::save()
{
	if (this->file_name != "")
	{
		ofstream f(this->file_name);

		f << "";

		f.close();

		f.open(this->file_name, ios_base::app);

		for (Movie& m : this->arr)
		{
			f << m;
		}

		f.close();
	}

	if (this->csv_file != "")
	{
		ofstream f(this->csv_file);

		f << "";

		f.close();

		f.open(this->csv_file, ios_base::app);

		f << "Title,Genre,Year,Likes,Link,\n";

		for (Movie& m : this->arr)
		{
			f << m;
		}

		f.close();
	}
}

string MovieRepoCSV::write_list()
{
	this->save();
	if (this->csv_file != "")
	{
		string command = "start " + this->csv_file;
		system(command.c_str());
	}
	string str = "";
	for (Movie& m : this->arr)
	{
		//str += m.write_movie() + "\n";
		cout << m << '\n';
	}

	return str;
}

