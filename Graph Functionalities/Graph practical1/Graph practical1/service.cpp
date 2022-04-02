#include "service.h"
#include <fstream>

Service::Service(Graph& graph) : graph(graph)
{
}

int Service::vertices_number()
{
	return this->graph.get_vertex_count();
}

int Service::edges_number()
{
	return this->graph.get_edge_count();
}

vector<int> Service::parse_out(string x)
{
	int x_i = atoi(x.c_str());
	return this->graph.parseNOut(x_i);
}

vector<int> Service::parse_in(string x)
{
	int x_i = atoi(x.c_str());
	return this->graph.parseNIn(x_i);
}

vector<int> Service::parse_all()
{
	return this->graph.parseX();
}

int Service::add_edge(string x, string y, string val)
{
	int x_i = atoi(x.c_str());
	int y_i = atoi(y.c_str());
	int val_i = atoi(val.c_str());

	if (!this->graph.add_edge(x_i, y_i, val_i))
		return 1;

	return 0;
}

int Service::remove_edge(string x, string y)
{
	int x_i = atoi(x.c_str());
	int y_i = atoi(y.c_str());

	if (!this->graph.remove_edge(x_i, y_i))
		return 1;

	return 0;
}

int Service::add_vertex(string x)
{
	int x_i = atoi(x.c_str());

	if (!this->graph.add_vertex(x_i))
		return 1;

	return 0;
}

int Service::remove_vertex(string x)
{
	int x_i = atoi(x.c_str());

	if (!this->graph.remove_vertex(x_i))
		return 1;

	return 0;
}

int Service::modify_info(string x, string y, string val)
{
	int x_i = atoi(x.c_str());
	int y_i = atoi(y.c_str());
	int val_i = atoi(val.c_str());

	if (!this->graph.set_edge(x_i, y_i, val_i))
		return 1;

	return 0;
}

void Service::delete_graph()
{
	vector<int> ver = this->graph.parseX();
	for (int i = 0; i < ver.size(); i++)
	{
		this->graph.remove_vertex(ver[i]);
	}
}

void Service::copy_graph()
{
	this->copy_g = this->graph.copy_graph();
}

void Service::write_to_file(string file_name)
{
	ofstream f(file_name);

	f << this->graph.write_graph();

	f.close();
}

void Service::read_from_file(string file_name)
{
	ifstream f(file_name);

	string line;
	string delimiter = " ";
	string token;

	while (getline(f, line))
	{
		if (line == "\n")
			break;
		int pos = line.find(delimiter);
		if (pos == string::npos)
		{
			this->add_vertex(line.substr(0, line.find("\n")));
			continue;
		}

		string x = line.substr(0, pos);

		line.erase(0, pos + delimiter.length());

		pos = line.find(delimiter);
		if (pos == string::npos)
		{
			for (int i = 0; i < atoi(x.c_str()); i++)
			{
				this->graph.add_vertex(i);
			}
			continue;
		}

		string y = line.substr(0, pos);

		line.erase(0, pos + delimiter.length());

		string val = line.substr(0, line.find("\n"));

		this->add_vertex(x);
		this->add_vertex(y);
		this->add_edge(x, y, val);
	}

	f.close();
}

string Service::write_graph()
{
	return this->graph.write_graph();
}

int Service::generate_random(string n, string m)
{
	this->delete_graph();

	int n_i = atoi(n.c_str());
	int m_i = atoi(m.c_str());

	if (m_i > n_i * n_i)
		return 1;

	for (int i = 0; i < n_i; i++)
		this->graph.add_vertex(i);

	while (m_i > 0)
	{
		int x = rand() % n_i;
		int y = rand() % n_i;

		if (this->graph.check_edge(x, y) != -1)
			continue;

		int val = rand() % 1000;

		this->graph.add_edge(x, y, val);

		m_i--;
	}

	return 0;
}

void Service::change_to_copy()
{
	Graph temp;
	temp = this->graph;
	this->graph = this->copy_g;
	this->copy_g = temp;
}
