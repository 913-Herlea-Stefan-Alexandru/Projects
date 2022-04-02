#pragma once

#include "graph.h"

class Service
{
private:

	Graph &graph;
	Graph copy_g;

public:

	Service(Graph &graph);

	int vertices_number();

	int edges_number();

	vector<int> parse_out(string x);

	vector<int> parse_in(string x);

	vector<int> parse_all();

	int add_edge(string x, string y, string val);

	int remove_edge(string x, string y);

	int add_vertex(string x);

	int remove_vertex(string x);

	int modify_info(string x, string y, string val);

	void delete_graph();

	void copy_graph();

	void write_to_file(string file_name);

	void read_from_file(string file_name);

	string write_graph();

	int generate_random(string n, string m);

	void change_to_copy();
};