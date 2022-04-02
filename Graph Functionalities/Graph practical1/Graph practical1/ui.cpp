#include "ui.h"
#include <iostream>

void Ui::print_menu()
{
	cout << "Menu\n";
	cout << "1. Generate random graph\n";
	cout << "2. Read from file\n";
	cout << "3. Write to file\n";
	cout << "4. Print graph\n";
	cout << "5. Add vertex\n";
	cout << "6. Remove vertex\n";
	cout << "7. Add edge\n";
	cout << "8. Remove edge\n";
	cout << "9. Outbound vertices\n";
	cout << "10. Inbound vertices\n";
	cout << "11. Parse vertices\n";
	cout << "12. Modify information\n";
	cout << "13. Vertex number\n";
	cout << "14. Edge number\n";
	cout << "15. Copy graph\n";
	cout << "16. Change to copy graph\n";
	cout << ">> ";
}

void Ui::random_ui()
{
	cin.get();
	char n[255], m[255];

	cout << "\nEnter the number of vertices: ";
	cin.getline(n, 255);

	cout << "\nEnter the number of edges: ";
	cin.getline(m, 255);

	string n_s(n);
	string m_s(m);

	this->service.generate_random(n_s, m_s);
}

void Ui::read_from_file_ui()
{
	cin.get();
	char file_name[255];

	cout << "\nEnter file name: ";
	cin.getline(file_name, 255);

	string fn(file_name);

	this->service.read_from_file(fn);
}

void Ui::write_to_file_ui()
{
	cin.get();
	char file_name[255];

	cout << "\nEnter file name: ";
	cin.getline(file_name, 255);

	string fn(file_name);

	this->service.write_to_file(fn);
}

void Ui::print_graph()
{
	cout << this->service.write_graph();
}

void Ui::add_vertex_ui()
{
	cin.get();
	char x[255];

	cout << "\nEnter the vertex: ";
	cin.getline(x, 255);

	string x_s(x);

	int r = this->service.add_vertex(x_s);

	if (r == 1)
		cout << "\nVertex already exists\n";
}

void Ui::remove_vertex_ui()
{
	cin.get();
	char x[255];

	cout << "\nEnter the vertex: ";
	cin.getline(x, 255);

	string x_s(x);

	int r = this->service.remove_vertex(x_s);

	if (r == 1)
		cout << "\nVertex not found\n";
}

void Ui::add_edge_ui()
{
	cin.get();
	char x[255], y[255], val[255];

	cout << "\nEnter the source vertex: ";
	cin.getline(x, 255);

	cout << "\nEnter the destination vertex: ";
	cin.getline(y, 255);

	cout << "\nEnter the value: ";
	cin.getline(val, 255);

	string x_s(x);
	string y_s(y);
	string val_s(val);

	int r = this->service.add_edge(x_s, y_s, val_s);

	if (r == 1)
		cout << "\nEdge already exists or vertices not found\n";
}

void Ui::remove_edge_ui()
{
	cin.get();
	char x[255], y[255];

	cout << "\nEnter the source vertex: ";
	cin.getline(x, 255);

	cout << "\nEnter the destination vertex: ";
	cin.getline(y, 255);

	string x_s(x);
	string y_s(y);

	int r = this->service.remove_edge(x_s, y_s);

	if (r == 1)
		cout << "\nEdge does not exist\n";
}

void Ui::outbound()
{
	cin.get();
	char x[255];

	cout << "\nEnter the source vertex: ";
	cin.getline(x, 255);

	string x_s(x);

	vector<int> ver = this->service.parse_out(x_s);

	string str = x_s + ": ";

	for (int i = 0; i < ver.size(); i++)
		str += " " + to_string(ver[i]);

	cout << str << '\n';
}

void Ui::inbound()
{
	cin.get();
	char x[255];

	cout << "\nEnter the destination vertex: ";
	cin.getline(x, 255);

	string x_s(x);

	vector<int> ver = this->service.parse_in(x_s);

	string str = x_s + ": ";

	for (int i = 0; i < ver.size(); i++)
		str += " " + to_string(ver[i]);

	cout << str << '\n';
}

void Ui::print_vertices()
{
	cin.get();

	vector<int> ver = this->service.parse_all();

	for (int i = 0; i < ver.size(); i++)
		cout << ver[i] << ' ';

	cout << '\n';
}

void Ui::modify()
{
	cin.get();
	char x[255], y[255], val[255];

	cout << "\nEnter the source vertex: ";
	cin.getline(x, 255);

	cout << "\nEnter the destination vertex: ";
	cin.getline(y, 255);

	cout << "\nEnter the new value: ";
	cin.getline(val, 255);

	string x_s(x);
	string y_s(y);
	string val_s(val);

	int r = this->service.modify_info(x_s, y_s, val_s);

	if (r == 1)
		cout << "\nEdge does not exist\n";
}

void Ui::vertex_number()
{
	cout << this->service.vertices_number();
}

void Ui::edge_number()
{
	cout << this->service.edges_number();
}

void Ui::copy()
{
	this->service.copy_graph();
}

void Ui::change_to_copy()
{
	this->service.change_to_copy();
}

Ui::Ui(Service& service) : service(service)
{
}

void Ui::start()
{
	bool is_runing = true;
	int command;

	while (is_runing)
	{
		this->print_menu();

		cin >> command;

		switch (command)
		{
		case 0:
			is_runing = false;
			break;
		case 1:
			this->random_ui();
			break;

		case 2:
			this->read_from_file_ui();
			break;

		case 3:
			this->write_to_file_ui();
			break;

		case 4:
			this->print_graph();
			break;

		case 5:
			this->add_vertex_ui();
			break;

		case 6:
			this->remove_vertex_ui();
			break;

		case 7:
			this->add_edge_ui();
			break;

		case 8:
			this->remove_edge_ui();
			break;

		case 9:
			this->outbound();
			break;

		case 10:
			this->inbound();
			break;

		case 11:
			this->print_vertices();
			break;

		case 12:
			this->modify();
			break;

		case 13:
			this->vertex_number();
			break;

		case 14:
			this->edge_number();
			break;

		case 15:
			this->copy();
			break;

		case 16:
			this->change_to_copy();
			break;

		default:
			cout << "\nInvalid command\n";
			break;
		}
	}
}
