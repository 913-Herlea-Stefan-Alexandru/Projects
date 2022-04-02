#include <iostream>
#include "graph.h"
#include "service.h"
#include "ui.h"

int main()
{
	Graph graph;
	Service service(graph);
	Ui ui(service);
	ui.start();

	return 0;
}