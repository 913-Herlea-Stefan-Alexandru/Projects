#include "movieRepoHTML.h"
#include <iostream>
#include <fstream>

MovieRepoHTML::MovieRepoHTML(string file_name, string html_file) : MovieRepo(file_name), html_file{html_file}
{
}

void MovieRepoHTML::save()
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

	if (this->html_file != "")
	{
		ofstream f(this->html_file);

		f << "";

		f.close();

		f.open(this->html_file, ios_base::app);

		f << "<!DOCTYPE html>\n";
		f << "<html>\n";
		f << "<head>\n";
		f << "	<title>Watch list</title>\n";
		f << "</head>\n";
		f << "<body>\n";
		f << "<table border=\"1\">\n";
		f << "	<tr>\n";
		f << "		<td>Movie</td>\n";
		f << "		<td>Genre</td>\n";
		f << "		<td>Year</td>\n";
		f << "		<td>Likes</td>\n";
		f << "		<td>Link</td>\n";
		f << "	</tr>\n";
		for (Movie& m : this->arr)
		{
			f << "	<tr>\n";
			f << "		<td>" << m.getTitle() << "</td>\n";
			f << "		<td>" << m.getGenre() << "</td>\n";
			f << "		<td>" << m.getYear() << "</td>\n";
			f << "		<td>" << m.getLikes() << "</td>\n";
			f << "		<td><a href=\"" << m.getLink() << "\">Youtube Link</a></td>\n";
			f << "	</tr>\n";
		}
		f << "</table>\n";
		f << "</body>\n";
		f << "</html>\n";
		f.close();
	}
}

string MovieRepoHTML::write_list()
{
	this->save();
	if (this->html_file != "")
	{
		string command = "start " + this->html_file;
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
