

class Ui:
    def __init__(self, service):
        self._service = service

    def _print_menu(self):
        print("Menu")
        print("1. Generate random graph")
        print("2. Read from file")
        print("3. Write to file directed")
        print("4. Print directed graph")
        print("5. Add vertex")
        print("6. Remove vertex")
        print("7. Add edge directed")
        print("8. Remove edge directed")
        print("9. In degree")
        print("10. Out degree")
        print("11. Outbound vertices")
        print("12. Inbound vertices")
        print("13. Parse vertices")
        print("14. Modify information")
        print('15. Vertex number')
        print('16. Edge number')
        print('17. Copy graph')
        print('18. Print graph as tree')
        print('19. Change to copy')
        print('20. Dijkstra')
        print('21. Add undirected edge')
        print('22. Remove undirected edge')
        print('23. Read undirected from file')
        print('24. Print undirected graph')
        print('25. BFS connected')
        print('26. Generate random undirected graph')
        print('27. Write to file undirected')
        print('28. Lowest cost walk between 2 vertices (Floyd Warshall)')
        print('29. Maximum clique')
        print("0. Exit")

    def _in_degree(self):
        x = input("\nEnter the vertex number: ")

        print(self._service.in_degree(x))

    def _out_degree(self):
        x = input("\nEnter the vertex number: ")

        print(self._service.out_degree(x))

    def _random_ui(self):
        n = input("\nEnter the number of vertices: ")
        m = input("Enter the number of edges: ")

        self._service.generate_random(n, m)

    def _read_from_file(self):
        file_name = input("\nEnter the file name: ")

        self._service.read_from_file(file_name)

    def _write_to_file(self):
        file_name = input("\nEnter the file name: ")

        self._service.write_to_file(file_name)

    def _print_graph(self):
        print(self._service.readable_graph())

    def _add_vertex_ui(self):
        x = input("\nEnter the vertex number: ")

        self._service.add_vertex(x)

    def _remove_vertex_ui(self):
        x = input("\nEnter the vertex number: ")

        self._service.remove_vertex(x)

    def _add_edge_ui(self):
        x = input("\nEnter the source vertex: ")
        y = input("Enter the destination vertex: ")
        val = input("Enter the information on the edge: ")

        self._service.add_edge(x, y, val)

    def _remove_edge_ui(self):
        x = input("\nEnter the source vertex: ")
        y = input("Enter the destination vertex: ")

        self._service.remove_edge(x, y)

    def _outbound(self):
        x = input("\nEnter the source vertex: ")

        string = str(x) + ': '
        for y in self._service.parse_out(x):
            string += str(y) + ' '
        print(string)

    def _inbound(self):
        x = input("\nEnter the destination vertex: ")

        string = str(x) + ': '
        for y in self._service.parse_in(x):
            string += str(y) + ' '
        print(string)

    def _print_vertices(self):
        string = ''
        for x in self._service.parse_all():
            string += str(x) + ' '
        print(string)

    def _modify(self):
        x = input("\nEnter the source vertex: ")
        y = input("Enter the destination vertex: ")
        val = input("Enter the information on the edge: ")

        self._service.modify_info(x, y, val)

    def _vertex_number(self):
        print(self._service.vertices_number())

    def _edge_number(self):
        print(self._service.edges_number())

    def _copy(self):
        self._service.copy_graph()

    def _print_tree(self):
        print(self._service.get_graph())

    def _change_copy(self):
        self._service.change_to_copy()

    def _dijkstra(self):
        x = int(input("Enter the beginning vertex: "))
        prev = self._service.dijkstra(x)

    def _addU(self):
        x = input("\nEnter the source vertex: ")
        y = input("Enter the destination vertex: ")
        val = input("Enter the information on the edge: ")

        self._service.add_edge_undirected(x, y)

    def _removeU(self):
        x = input("\nEnter the source vertex: ")
        y = input("Enter the destination vertex: ")

        self._service.remove_edge_undirected(x, y)

    def _readU(self):
        file_name = input("\nEnter the file name: ")

        self._service.read_from_file_undirected(file_name)

    def _printU(self):
        print(self._service.readable_undirected())

    def _BFSconnected(self):
        cc = self._service.connected()
        for g in cc:
            print(g.parseX())
            print(g.print_undirected(), '\n')

    def _random_undir(self):
        n = input("\nEnter the number of vertices: ")
        m = input("Enter the number of edges: ")

        self._service.generate_random_undirected(n, m)

    def _write_undirected(self):
        fn = input("Enter file name: ")
        self._service.write_to_file_undirected(fn)

    def _Floyd_Warshall(self):
        x = input("\nEnter source vertex: ")
        y = input("Enter destination vertex: ")
        path, cost = self._service.Floyd_Warshall(x, y)
        print('cost = ' + str(cost))
        print('path = ' + ' -> '.join(str(i) for i in path))

    def _max_clique(self):
        print(" ".join(str(v) for v in self._service.max_clique()))

    def start(self):
        is_running = True

        command_dict = {'1': self._random_ui, '2': self._read_from_file, '3': self._write_to_file,
                        '4': self._print_graph, '5': self._add_vertex_ui, '6': self._remove_vertex_ui,
                        '7': self._add_edge_ui, '8': self._remove_edge_ui, '9': self._in_degree, '10': self._out_degree,
                        '11': self._outbound, '12': self._inbound, '13': self._print_vertices, '14': self._modify,
                        '15': self._vertex_number, '16': self._edge_number, '17': self._copy, '18': self._print_tree,
                        '19': self._change_copy, '20': self._dijkstra, '21': self._addU, '22': self._removeU,
                        '23': self._readU, '24': self._printU, '25': self._BFSconnected, '26': self._random_undir,
                        '27': self._write_undirected, '28': self._Floyd_Warshall, '29': self._max_clique}

        while is_running:
            self._print_menu()

            command = input(">> ")
            try:
                if command in command_dict:
                    command_dict[command]()
                elif command == '0':
                    is_running = False
                else:
                    print("\nInvalid command\n")
            except Exception as ex:
                print(str(ex))
