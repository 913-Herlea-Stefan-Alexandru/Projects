from src.validators.validator import ValidationError

class MenuUI:
    def __init__(self, service):
        self._service = service
        self._is_running = True

    def _main_menu(self):
        print('\n1. Manage students and disciplines')
        print('2. Manage grades')
        print('3. Search')
        print('4. Statistics')
        print('5. Undo')
        print('6. Redo')
        print('x. Exit program')
        print()

    def _manage_menu(self):
        print('\n1. Add student')
        print('2. Remove student')
        print('3. Update a student')
        print('4. List all students')
        print('5. Add discipline')
        print('6. Remove discipline')
        print('7. Update a discipline')
        print('8. List all disciplines')
        print('0. Previous menu')
        print()

    def _grade_menu(self):
        print('\n1. Add grade')
        print('2. List all grades')
        print('0. Previous menu')

    def _search_menu(self):
        print('\n1. Search for student')
        print('2. Search for discipline')
        print('0. Previous menu')

    def _statistics_menu(self):
        print('\n1. All students failing at one or more disciplines')
        print('2. Students with the best school situation, '
              '\n  sorted in descending order of their aggregated average')
        print('3. All disciplines at which there is at least one grade, '
              '\n  sorted in descending order of the average grade received '
              '\n  by all students enrolled at that discipline')
        print('0. Previous menu')

    def _write_student(self, student):
        return str(student)

    def _write_discipline(self, discipline):
        return str(discipline)

    def _write_grade(self, grade):
        return str(grade)

    def _grade(self):
        is_grading = True
        grade_dict = {'1': self._grade_student_ui, '2': self._list_all_grades_ui}
        while is_grading:
            self._grade_menu()
            grade_command = input('Command: ')
            if grade_command in grade_dict:
                try:
                    grade_dict[grade_command]()
                except ValidationError as ve:
                    print(str(ve))
            elif grade_command == '0':
                is_grading = False
            else:
                print('\nInvalid command')

    def _manage(self):
        is_managing = True
        manage_dict = {'1': self._add_student_ui, '2': self._remove_student_ui, '3': self._update_student_ui,
                       '4': self._list_all_students_ui, '5': self._add_discipline_ui,
                       '6': self._remove_discipline_ui, '7': self._update_discipline_ui,
                       '8': self._list_all_disciplines_ui}
        while is_managing:
            self._manage_menu()
            manage_command = input('Command: ')
            if manage_command in manage_dict:
                try:
                    manage_dict[manage_command]()
                except ValidationError as ve:
                    print(str(ve))
            elif manage_command == '0':
                is_managing = False
            else:
                print('\nInvalid command')

    def _search(self):
        is_searching = True
        search_dict = {'1': self._search_student, '2': self._search_discipline}
        while is_searching:
            self._search_menu()
            search_command = input('Command: ')
            if search_command in search_dict:
                try:
                    search_dict[search_command]()
                except ValidationError as ve:
                    print(str(ve))
            elif search_command == '0':
                is_searching = False
            else:
                print('\nInvalid command')

    def _statistics(self):
        is_creating_stats = True
        stats_dict = {'1': self._failing_students, '2': self._top_students, '3': self._top_disciplines}
        while is_creating_stats:
            self._statistics_menu()
            stat_command = input('Command: ')
            if stat_command in stats_dict:
                try:
                    stats_dict[stat_command]()
                except ValidationError as ve:
                    print(str(ve))
            elif stat_command == '0':
                is_creating_stats = False
            else:
                print('\nInvalid command')

    def _undo(self):
        if self._service.undo():
            print('\nUndo successful')
        else:
            print('\nNothing to undo')

    def _redo(self):
        if self._service.redo():
            print('\nRedo successful')
        else:
            print('\nNothing to redo')

    def _failing_students(self):
        for student in self._service.failing_students():
            print(self._write_student(student))

    def _top_students(self):
        for student_top in self._service.top_students():
            print(self._write_student(student_top.student) + ' - ' + str(student_top.aggregated_avg))

    def _top_disciplines(self):
        for discipline_top in self._service.top_disciplines():
            print(self._write_discipline(discipline_top.discipline) + ' - ' + str(discipline_top.avg))

    def _search_student(self):
        search_str = input('Search by id or name: ')
        found_list = self._service.search_students(search_str)
        for student in found_list:
            print(self._write_student(student))

    def _search_discipline(self):
        search_str = input('Search by id or discipline name: ')
        found_list = self._service.search_disciplines(search_str)
        for discipline in found_list:
            print(self._write_discipline(discipline))

    def _list_all_disciplines_ui(self):
        discipline_list = self._service.list_all_disciplines()
        for discipline in discipline_list:
            print(self._write_discipline(discipline))

    def _read_discipline(self):
        discipline_id = input('Enter discipline id: ')
        name = input('Enter discipline name: ')
        return discipline_id, name

    def _add_discipline_ui(self):
        discipline_id, name = self._read_discipline()
        self._service.add_discipline(discipline_id, name)
        print('\nDiscipline added successfully')

    def _remove_discipline_ui(self):
        discipline_id = input('Enter discipline id: ')
        self._service.remove_discipline(discipline_id)
        print('\nDiscipline removed successfully')

    def _update_discipline_ui(self):
        discipline_id = input('Enter discipline id: ')
        new_name = input('Enter the new name for the given discipline: ')
        self._service.update_discipline(discipline_id, new_name)
        print('\nDiscipline updated successfully')

    def _list_all_students_ui(self):
        student_list = self._service.list_all_students()
        for student in student_list:
            print(self._write_student(student))

    def _read_student(self):
        student_id = input('Enter student id: ')
        name = input('Enter student name: ')
        return student_id, name

    def _add_student_ui(self):
        student_id, name = self._read_student()
        self._service.add_student(student_id, name)
        print('\nStudent added successfully')

    def _remove_student_ui(self):
        student_id = input('Enter student id: ')
        self._service.remove_student(student_id)
        print('\nStudent removed successfully')

    def _update_student_ui(self):
        student_id = input('Enter student id: ')
        new_name = input('Enter new name for the given student: ')
        self._service.update_student(student_id, new_name)
        print('\nStudent name updated successfully')

    def _grade_student_ui(self):
        grade_id = input('Enter the grade\'s id: ')
        discipline_id = input('Enter the discipline\'s id: ')
        student_id = input('Enter the student\'s id: ')
        grade_value = input('Enter the grade: ')
        self._service.add_grade(grade_id, discipline_id, student_id, grade_value)
        print('\nGrade added successfully')

    def _list_all_grades_ui(self):
        grade_list = self._service.list_all_grades()
        for grade in grade_list:
            print(self._write_grade(grade))

    def start(self):
        command_dict = {'1': self._manage, '2': self._grade, '3': self._search, '4': self._statistics, '5': self._undo,
                        '6': self._redo}
        while self._is_running:
            self._main_menu()
            command = input('Command: ')
            if command in command_dict:
                try:
                    command_dict[command]()
                except ValidationError as ve:
                    print(str(ve))
            elif command == 'x':
                self._is_running = False
            else:
                print('\nInvalid command')
