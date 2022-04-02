from src.validators.validator import ValidationError

class DisciplineRepository:
    def __init__(self):
        self._discipline_list = []

    def __len__(self):
        return len(self._discipline_list)

    def add(self, discipline):
        '''
        Adds the given discipline to the discipline list
        :param discipline: The given discipline (Discipline object)
        :return: -
        Raises ValidationError if a discipline with the same id is already in the list
        '''
        if discipline.id in [disc.id for disc in self._discipline_list]:
            raise ValidationError('\nDiscipline with given id is already in data base\n')
        self._discipline_list.append(discipline)

    def __getitem__(self, given_id):
        '''
        Returns the discipline found with the given id
        :param given_id: The given discipline id (str)
        :return: The discipline found with the given id
        Raises ValidationError if no discipline was found
        '''
        if not (given_id in [disc.id for disc in self._discipline_list]):
            raise ValidationError('\nDiscipline with given id not found\n')
        for discipline in self._discipline_list:
            if discipline.id == given_id:
                return discipline

    def remove(self, discipline):
        self._discipline_list.pop(self._discipline_list.index(discipline))

    def get_id_list(self):
        return [discipline.id for discipline in self._discipline_list]

    def modify(self, discipline, new_name):
        discipline.name = new_name

    def search(self, search_str):
        '''
        Returns a list of all disciplines found containing the given string in their id or name
        :param search_str: The given string (str)
        :return: The found list of disciplines
        Raises ValidationError if no discipline was found
        '''
        found_list = []
        for discipline in self._discipline_list:
            if search_str.lower() in discipline.id or search_str.lower() in discipline.name.lower():
                found_list.append(discipline)
        if found_list == []:
            raise ValidationError('\nNo discipline found\n')
        return found_list