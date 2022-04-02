import PySimpleGUI as sg
from src.validators.validator import ValidationError

class GUI:
    def __init__(self, service):
        self._service = service
        sg.theme('Python')

    def make_main_window(self):
        layout = [
            [sg.Text('          Select an option', font=('Arial', 15))],
            [sg.Text(size=(100, 1), font=('Arial', 10), key='-OUTPUT-')],
            [sg.Button('Manage students/disciplines', size=(35, 2))],
            [sg.Button('Manage grades', size=(35, 2))],
            [sg.Button('Search', size=(35, 2))],
            [sg.Button('Statistics', size=(35, 2))],
            [sg.Button('Undo', size=(35, 2))],
            [sg.Button('Redo', size=(35, 2))],
            [sg.Button('Exit', size=(35, 2))]
        ]
        return sg.Window('Main Menu', layout, size=(300, 420), finalize=True)

    def make_manage_sd_window(self):
        student_column = [
            [sg.Text('Student management', font=('Arial', 15))],
            [sg.Text('   '), sg.Button('Add', size=(17, 2), key='ADD STUD')],
            [sg.Text('   '), sg.Button('Remove', size=(17, 2), key='REM STUD')],
            [sg.Text('   '), sg.Button('Change', size=(17, 2), key='CHG STUD')],
            [sg.Text('   '), sg.Button('List all', size=(17, 2), key='LIST STUDENTS')]
        ]

        discipline_column = [
            [sg.Text('Discipline management', font=('Arial', 15))],
            [sg.Text('      '), sg.Button('Add', size=(17, 2), key='ADD DISC')],
            [sg.Text('      '), sg.Button('Remove', size=(17, 2), key='REM DISC')],
            [sg.Text('      '), sg.Button('Change', size=(17, 2), key='CHG DISC')],
            [sg.Text('      '), sg.Button('List all', size=(17, 2), key='LIST DISCIPLINES')]
        ]

        layout = [
            [sg.Column(student_column),
            sg.VSeparator(),
            sg.Column(discipline_column)],
            [sg.Text('                               '), sg.Button('Back', size=(17, 2))]
        ]
        return sg.Window('Manage Students/Disciplines', layout, finalize=True)

    def make_manage_grades_window(self):
        layout = [
            [sg.Text('    Grade management', font=('Arial', 15))],
            [sg.Text('')],
            [sg.Text('      '), sg.Button('Add', size=(17, 2))],
            [sg.Text('      '), sg.Button('List all', size=(17, 2))],
            [sg.Text('      '), sg.Button('Back', size=(17, 2))]
        ]
        return sg.Window('Manage Grades', layout, finalize=True, size=(250, 270))

    def make_search_window(self):
        student_column = [
            [sg.Text('            Search for students', font=('Arial', 15))],
            [sg.Input(enable_events=True, key='-STUD-')],
            [sg.Listbox(values=self._service.search_students(''), key='-STUD LIST-', size=(43, 12))]
        ]

        discipline_column = [
            [sg.Text('            Search for disciplines', font=('Arial', 15))],
            [sg.Input(enable_events=True, key='-DISC-')],
            [sg.Listbox(values=self._service.search_disciplines(''), key='-DISC LIST-', size=(43, 12))]
        ]

        layout = [
            [sg.Column(student_column),
             sg.VSeparator(),
             sg.Column(discipline_column)],
            [sg.Text('                                                               '), sg.Button('Back', size=(17, 2))]
        ]
        return sg.Window('Search', layout, finalize=True)

    def make_statistics_window(self):
        layout = [
            [sg.Combo(values=['Failing Students', 'Students with the best school situation', 'All disciplines with grades'], enable_events=True,  key='STAT')],
            [sg.Listbox(values=[], size=(40, 12), key="-LIST-")],
            [sg.Text('            '), sg.Button('Back', size=(17, 2))]
        ]
        return sg.Window('Statistics', layout, finalize=True, size=(300, 300))

    def list_students_window(self):
        student_list = self._service.list_all_students()
        layout = [
            [sg.Text('            The list of students', font=('Arial', 15))],
            [sg.Listbox(values=['ID           Name']+self._service.list_all_students(), size=(40, 12), key='STUD LIST')]
        ]
        return sg.Window('Student list', layout, finalize=True)

    def list_disciplines_window(self):
        discipline_list = self._service.list_all_disciplines()
        layout = [
            [sg.Text('          The list of disciplines', font=('Arial', 15))],
            [sg.Listbox(values=['ID           Discipline']+self._service.list_all_disciplines(), size=(40, 12), key='DISC LIST')]
        ]
        return sg.Window('Student list', layout, finalize=True)

    def list_grades_window(self):
        grade_list = self._service.list_all_grades()
        layout = [
            [sg.Text('          The list of disciplines', font=('Arial', 15))],
            [sg.Listbox(values=['StudentID           DisciplineID           Grade']+self._service.list_all_grades(), size=(40, 12), key='GRADE LIST')]
        ]
        return sg.Window('Student list', layout, finalize=True)

    def add_stud_window(self):
        layout = [
            [sg.Text('                         Add Student', font=('Arial', 15))],
            [sg.Text('   Student id:    ', font=('Arial', 10)), sg.Input(key='ID IN')],
            [sg.Text('Student name: ', font=('Arial', 10)), sg.Input(key='NAME IN')],
            [sg.Button('Submit', size=(17, 2))]
        ]
        return sg.Window('Add student', layout, finalize=True)

    def add_disc_window(self):
        layout = [
            [sg.Text('                         Add Discipline', font=('Arial', 15))],
            [sg.Text('   Discipline id:    ', font=('Arial', 10)), sg.Input(key='ID IN')],
            [sg.Text('Discipline name: ', font=('Arial', 10)), sg.Input(key='NAME IN')],
            [sg.Button('Submit', size=(17, 2))]
        ]
        return sg.Window('Add discipline', layout, finalize=True)

    def add_grade_window(self):
        layout = [
            [sg.Text('                         Add Grade', font=('Arial', 15))],
            [sg.Text('      Grade id:     ', font=('Arial', 10)), sg.Input(key='ID GR')],
            [sg.Text('    Student id:    ', font=('Arial', 10)), sg.Input(key='ID STUD')],
            [sg.Text('     Discipline id: ', font=('Arial', 10)), sg.Input(key='ID DISC')],
            [sg.Text('   Grade value:   ', font=('Arial', 10)), sg.Input(key='GRADE')],
            [sg.Button('Submit', size=(17, 2))]
        ]
        return sg.Window('Add grade', layout, finalize=True)

    def remove_stud_window(self):
        layout = [
            [sg.Text('                       Remove Student', font=('Arial', 15))],
            [sg.Text('   Student id:    ', font=('Arial', 10)), sg.Input(key='ID IN')],
            [sg.Button('Delete', size=(17, 2))]
        ]
        return sg.Window('Remove student', layout, finalize=True)

    def remove_disc_window(self):
        layout = [
            [sg.Text('                       Remove Discipline', font=('Arial', 15))],
            [sg.Text('   Discipline id:    ', font=('Arial', 10)), sg.Input(key='ID IN')],
            [sg.Button('Delete', size=(17, 2))]
        ]
        return sg.Window('Remove discipline', layout, finalize=True)

    def change_stud_window(self):
        layout = [
            [sg.Text('                       Change Student', font=('Arial', 15))],
            [sg.Text('   Student id:    ', font=('Arial', 10)), sg.Input(key='ID IN')],
            [sg.Text('Student name: ', font=('Arial', 10)), sg.Input(key='NAME IN')],
            [sg.Button('Change', size=(17, 2))]
        ]
        return sg.Window('Change student', layout, finalize=True)

    def change_disc_window(self):
        layout = [
            [sg.Text('                       Change Discipline', font=('Arial', 15))],
            [sg.Text('   Discipline id:    ', font=('Arial', 10)), sg.Input(key='ID IN')],
            [sg.Text('Discipline name: ', font=('Arial', 10)), sg.Input(key='NAME IN')],
            [sg.Button('Change', size=(17, 2))]
        ]
        return sg.Window('Change discipline', layout, finalize=True)

    def start(self):
        temp_window_list = [None for i in range(6)]
        main_window, manage_sd, manage_gr, search, statistics, list_stud, list_disc, list_grades = self.make_main_window(), None, None, None, None, None, None, None
        while True:
            window, event, values = sg.read_all_windows()
            if window == main_window and event in (sg.WIN_CLOSED, 'Exit'):
                break

            if window == main_window:
                if event == 'Manage students/disciplines':
                    main_window.hide()
                    manage_sd = self.make_manage_sd_window()
                elif event == 'Manage grades':
                    main_window.hide()
                    manage_gr = self.make_manage_grades_window()
                elif event == 'Search':
                    main_window.hide()
                    search = self.make_search_window()
                elif event == 'Statistics':
                    main_window.hide()
                    statistics = self.make_statistics_window()
                elif event == 'Undo':
                    changes = False
                    if self._service.undo():
                        window['-OUTPUT-'].update('                      Undo successful')
                        changes = True
                    else:
                        window['-OUTPUT-'].update('                      Nothing to undo')
                    if changes:
                        if temp_window_list[0] != None:
                            window1 = temp_window_list[0]
                            window1['STUD LIST'].update(['ID           Name'] + self._service.list_all_students())
                        if temp_window_list[1] != None:
                            window1 = temp_window_list[1]
                            window1['DISC LIST'].update(['ID           Discipline'] + self._service.list_all_disciplines())
                        if temp_window_list[2] != None:
                            window2 = temp_window_list[2]
                            window2['GRADE LIST'].update(['StudentID           DisciplineID           Grade'] + self._service.list_all_grades())
                elif event == 'Redo':
                    changes = False
                    if self._service.redo():
                        window['-OUTPUT-'].update('                      Redo successful')
                        changes = True
                    else:
                        window['-OUTPUT-'].update('                      Nothing to redo')
                    if changes:
                        if temp_window_list[0] != None:
                            window1 = temp_window_list[0]
                            window1['STUD LIST'].update(['ID           Name'] + self._service.list_all_students())
                        if temp_window_list[1] != None:
                            window1 = temp_window_list[1]
                            window1['DISC LIST'].update(['ID           Discipline'] + self._service.list_all_disciplines())
                        if temp_window_list[2] != None:
                            window2 = temp_window_list[2]
                            window2['GRADE LIST'].update(['StudentID           DisciplineID           Grade'] + self._service.list_all_grades())
            if window == temp_window_list[0]:
                if event == sg.WIN_CLOSED:
                    window.close()
                    temp_window_list[0] = None
            elif window == temp_window_list[1]:
                if event == sg.WIN_CLOSED:
                    window.close()
                    temp_window_list[1] = None
            elif window == temp_window_list[2]:
                if event == sg.WIN_CLOSED:
                    window.close()
                    temp_window_list[2] = None
            elif window == temp_window_list[3]:
                if event == sg.WIN_CLOSED:
                    window.close()
                    temp_window_list[3] = None
                changes = False
                if event == 'Submit':
                    try:
                        self._service.add_student(values['ID IN'], values['NAME IN'])
                        window.close()
                        temp_window_list[3] = None
                        sg.popup('Student added successfully')
                        changes = True
                    except ValidationError as ve:
                        sg.popup('     ' + str(ve) + '     ', title='Error')
                if event == 'Delete':
                    try:
                        self._service.remove_student(values['ID IN'])
                        window.close()
                        temp_window_list[3] = None
                        sg.popup('Student removed successfully')
                        changes = True
                    except ValidationError as ve:
                        sg.popup('     ' + str(ve) + '     ', title='Error')
                if event == 'Change':
                    try:
                        self._service.update_student(values['ID IN'], values['NAME IN'])
                        window.close()
                        temp_window_list[3] = None
                        sg.popup('Student name changed successfully')
                        changes = True
                    except ValidationError as ve:
                        sg.popup('     ' + str(ve) + '     ', title='Error')
                if changes:
                    if temp_window_list[0] != None:
                        window1 = temp_window_list[0]
                        window1['STUD LIST'].update(['ID           Name']+self._service.list_all_students())
            elif window == temp_window_list[4]:
                if event == sg.WIN_CLOSED:
                    window.close()
                    temp_window_list[4] = None
                changes = False
                if event == 'Submit':
                    try:
                        self._service.add_discipline(values['ID IN'], values['NAME IN'])
                        window.close()
                        temp_window_list[4] = None
                        sg.popup('Discipline added successfully')
                        changes = True
                    except ValidationError as ve:
                        sg.popup('     ' + str(ve) + '     ', title='Error')
                if event == 'Delete':
                    try:
                        self._service.remove_discipline(values['ID IN'])
                        window.close()
                        temp_window_list[4] = None
                        sg.popup('Discipline removed successfully')
                        changes = True
                    except ValidationError as ve:
                        sg.popup('     ' + str(ve) + '     ', title='Error')
                if event == 'Change':
                    try:
                        self._service.update_discipline(values['ID IN'], values['NAME IN'])
                        window.close()
                        temp_window_list[4] = None
                        sg.popup('Discipline name changed successfully')
                        changes = True
                    except ValidationError as ve:
                        sg.popup('     ' + str(ve) + '     ', title='Error')
                if changes:
                    if temp_window_list[1] != None:
                        window1 = temp_window_list[1]
                        window1['DISC LIST'].update(['ID           Discipline']+self._service.list_all_disciplines())
            elif window == temp_window_list[5]:
                if event == sg.WIN_CLOSED:
                    window.close()
                    temp_window_list[5] = None
                changes = False
                if event == 'Submit':
                    try:
                        self._service.add_grade(values['ID GR'], values['ID DISC'], values['ID STUD'], values['GRADE'])
                        window.close()
                        temp_window_list[5] = None
                        sg.popup('Grade added successfully')
                        changes = True
                    except ValidationError as ve:
                        sg.popup('     ' + str(ve) + '     ', title='Error')
                if changes:
                    if temp_window_list[2] != None:
                        window2 = temp_window_list[2]
                        window2['GRADE LIST'].update(['StudentID           DisciplineID           Grade']+self._service.list_all_grades())
            elif window == manage_sd:
                if event == sg.WIN_CLOSED or event == 'Back':
                    window.close()
                    manage_sd = None
                    main_window.un_hide()
                if event == 'ADD STUD':
                    if temp_window_list[3] == None:
                        temp_window_list[3] = self.add_stud_window()
                if event == 'REM STUD':
                    if temp_window_list[3] == None:
                        temp_window_list[3] = self.remove_stud_window()
                if event == 'CHG STUD':
                    if temp_window_list[3] == None:
                        temp_window_list[3] = self.change_stud_window()
                if event == 'ADD DISC':
                    if temp_window_list[4] == None:
                        temp_window_list[4] = self.add_disc_window()
                if event == 'REM DISC':
                    if temp_window_list[4] == None:
                        temp_window_list[4] = self.remove_disc_window()
                if event == 'CHG DISC':
                    if temp_window_list[4] == None:
                        temp_window_list[4] = self.change_disc_window()
                if event == 'LIST STUDENTS':
                    if temp_window_list[0] == None:
                        temp_window_list[0] = self.list_students_window()
                if event == 'LIST DISCIPLINES':
                    if temp_window_list[1] == None:
                        temp_window_list[1] = self.list_disciplines_window()
            elif window == manage_gr:
                if event == sg.WIN_CLOSED or event == 'Back':
                    window.close()
                    manage_gr = None
                    main_window.un_hide()
                if event == 'Add':
                    if temp_window_list[5] == None:
                        temp_window_list[5] = self.add_grade_window()
                if event == 'List all':
                    if temp_window_list[2] == None:
                        temp_window_list[2] = self.list_grades_window()
            elif window == search:
                if event == sg.WIN_CLOSED or event == 'Back':
                    window.close()
                    search = None
                    main_window.un_hide()
                if event == '-STUD-':
                    try:
                        window['-STUD LIST-'].update(self._service.search_students(values['-STUD-']))
                    except ValidationError as ve:
                        window['-STUD LIST-'].update([str(ve)])
                if event == '-DISC-':
                    try:
                        window['-DISC LIST-'].update(self._service.search_disciplines(values['-DISC-']))
                    except ValidationError as ve:
                        window['-DISC LIST-'].update([str(ve)])
            elif window == statistics:
                if event == sg.WIN_CLOSED or event == 'Back':
                    window.close()
                    statistics = None
                    main_window.un_hide()
                if event == 'STAT':
                    if values['STAT'] == 'Failing Students':
                        window['-LIST-'].update(self._service.failing_students())
                    if values['STAT'] == 'Students with the best school situation':
                        window['-LIST-'].update(self._service.top_students())
                    if values['STAT'] == 'All disciplines with grades':
                        window['-LIST-'].update(self._service.top_disciplines())

        main_window.close()