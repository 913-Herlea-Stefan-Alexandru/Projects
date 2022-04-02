#include "graph.h"

int Graph::get_in_pos(int x)
{
	for (int i = 0; i < this->vertex_dict_in.size(); i++)
	{
		DElem e = this->vertex_dict_in[i];
		if (e.first == x)
			return i;
	}
	return -1;
}

vector<int> Graph::parseX()
{
	vector<int> ver;
	for (int i = 0; i < this->vertex_dict_out.size(); i++)
	{
		DElem e = this->vertex_dict_out[i];
		ver.push_back(e.first);
	}
	return ver;
}

vector<int> Graph::parseNOut(int x)
{
	vector<int> ver;
	for (int i = 0; i < this->vertex_dict_out.size(); i++)
	{
		DElem e = this->vertex_dict_out[i];
		if (e.first == x)
		{
			for (int j = 0; j < e.second.size(); j++)
			{
				ver.push_back(e.second[j]);
			}
		}
	}
	return ver;
}

vector<int> Graph::parseNIn(int x)
{
	vector<int> ver;
	for (int i = 0; i < this->vertex_dict_in.size(); i++)
	{
		DElem e = this->vertex_dict_in[i];
		if (e.first == x)
		{
			for (int j = 0; j < e.second.size(); j++)
			{
				ver.push_back(e.second[j]);
			}
		}
	}
	return ver;
}

int Graph::check_edge(int x, int y)
{
	for (int i = 0; i < this->edge_dict.size(); i++)
	{
		DEdge e = this->edge_dict[i];
		if (e.first.first == x && e.first.second == y)
			return i;
	}
	return -1;
}

int Graph::check_vertex(int x)
{
	for (int i = 0; i < this->vertex_dict_out.size(); i++)
	{
		DElem e = this->vertex_dict_out[i];
		if (e.first == x)
			return i;
	}
	return -1;
}

bool Graph::add_edge(int x, int y, int val)
{
	if (this->check_edge(x, y) != -1 || this->check_vertex(x) == -1 || this->check_vertex(y) == -1)
		return false;

	DEdge e;
	e.first.first = x;
	e.first.second = y;
	e.second = val;

	this->edge_dict.push_back(e);

	int pos = this->check_vertex(x);

	this->vertex_dict_out[pos].second.push_back(y);

	pos = this->get_in_pos(y);

	this->vertex_dict_in[pos].second.push_back(x);

	return true;
}

bool Graph::remove_edge(int x, int y)
{
	int pos = this->check_edge(x, y);
	if (pos == -1)
		return false;

	this->edge_dict.erase(this->edge_dict.begin() + pos);

	pos = this->check_vertex(x);
	for (int i = 0; i < this->vertex_dict_out[pos].second.size(); i++)
	{
		if (y == this->vertex_dict_out[pos].second[i])
		{
			this->vertex_dict_out[pos].second.erase(this->vertex_dict_out[pos].second.begin() + i);
			break;
		}
	}

	pos = this->get_in_pos(y);
	for (int i = 0; i < this->vertex_dict_in[pos].second.size(); i++)
	{
		if (x == this->vertex_dict_in[pos].second[i])
		{
			this->vertex_dict_in[pos].second.erase(this->vertex_dict_in[pos].second.begin() + i);
			break;
		}
	}

	return true;
}

bool Graph::add_vertex(int x)
{
	if (this->check_vertex(x) != -1)
		return false;

	DElem e;
	e.first = x;

	this->vertex_dict_out.push_back(e);
	this->vertex_dict_in.push_back(e);

	this->vertexes++;

	return true;
}

bool Graph::remove_vertex(int x)
{
	int pos = this->check_vertex(x);
	if (pos == -1)
		return false;

	for (int i = 0; i < this->vertex_dict_out[pos].second.size(); i++)
	{
		int y = this->vertex_dict_out[pos].second[i];
		this->remove_edge(x, y);
		i--;
	}

	this->vertex_dict_out.erase(this->vertex_dict_out.begin() + pos);

	pos = this->get_in_pos(x);
	for (int i = 0; i < this->vertex_dict_in[pos].second.size(); i++)
	{
		int y = this->vertex_dict_in[pos].second[i];
		this->remove_edge(y, x);
		i--;
	}

	this->vertex_dict_in.erase(this->vertex_dict_in.begin() + pos);

	this->vertexes--;

	return true;
}

int Graph::get_info(int x, int y)
{
	int pos = this->check_edge(x, y);
	if (pos == -1)
		return NULL_VAL;
	return this->edge_dict[pos].second;
}

bool Graph::set_edge(int x, int y, int val)
{
	int pos = this->check_edge(x, y);
	if (pos == -1)
		return false;
	this->edge_dict[pos].second = val;
	return true;
}

int Graph::in_degree(int x)
{
	int pos = this->get_in_pos(x);
	if (pos == -1)
		return NULL_VAL;
	return this->vertex_dict_in[pos].second.size();
}

int Graph::out_degree(int x)
{
	int pos = this->check_vertex(x);
	if (pos == -1)
		return NULL_VAL;
	return this->vertex_dict_out[pos].second.size();
}

Graph Graph::copy_graph()
{
	Graph g_copy;
	for (int i = 0; i < this->vertex_dict_out.size(); i++)
	{
		g_copy.add_vertex(this->vertex_dict_out[i].first);
	}
	for (int i = 0; i < this->edge_dict.size(); i++)
	{
		DEdge e = this->edge_dict[i];
		g_copy.add_edge(e.first.first, e.first.second, e.second);
	}
	return g_copy;
}

int Graph::get_vertex_count()
{
	return this->vertexes;
}

int Graph::get_edge_count()
{
	return this->edge_dict.size();
}

string Graph::write_graph()
{
	string str = "";

	vector<int> ver_x = this->parseX();

	for (int i = 0; i < ver_x.size(); i++)
	{
		int x = ver_x[i];
		vector<int> ver_y = this->parseNOut(x);

		if (ver_y.size() == 0 && this->parseNIn(x).size() == 0)
		{
			str += to_string(x) + '\n';
			continue;
		}

		for (int j = 0; j < ver_y.size(); j++)
		{
			int y = ver_y[j];
			str += to_string(x) + ' ' + to_string(y) + ' ' + to_string(this->get_info(x, y)) + '\n';
		}
	}

	return str;
}
