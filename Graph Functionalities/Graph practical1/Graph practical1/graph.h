#pragma once

#include <vector>
#include <string>

using namespace std;

#define NULL_VAL -111111 

typedef pair<int, vector<int>> DElem;
typedef pair<pair<int, int>, int> DEdge;

class Graph
{
private:

	int vertexes = 0;
	vector<DElem> vertex_dict_out;
	vector<DElem> vertex_dict_in;
	vector<DEdge> edge_dict;

	int get_in_pos(int x);

public:

	vector<int> parseX();

	vector<int> parseNOut(int x);

	vector<int> parseNIn(int x);

	int check_edge(int x, int y);

	int check_vertex(int x);

	bool add_edge(int x, int y, int val = 0);

	bool remove_edge(int x, int y);

	bool add_vertex(int x);

	bool remove_vertex(int x);

	int get_info(int x, int y);

	bool set_edge(int x, int y, int val);

	int in_degree(int x);

	int out_degree(int x);

	Graph copy_graph();

	int get_vertex_count();

	int get_edge_count();

	string write_graph();
};