#pragma once

#include "service.h"

class Ui
{
private:

	Service &service;

	void print_menu();

	void random_ui();

	void read_from_file_ui();

	void write_to_file_ui();

	void print_graph();

	void add_vertex_ui();

	void remove_vertex_ui();

	void add_edge_ui();

	void remove_edge_ui();

	void outbound();

	void inbound();

	void print_vertices();

	void modify();

	void vertex_number();

	void edge_number();

	void copy();

	void change_to_copy();

public:

	Ui(Service &service);

	void start();
};