from robot.parsing import TestData
from get_suites_list import ProjectSuites


class ExcludedSuites:

    def __init__(self, tags):
        self.tags = list(tags.replace(" ", "").split(","))
        calculate_suites = ProjectSuites()
        self.suites_list = calculate_suites.get_suites()
        print(f'Полный перечень сютов: {self.suites_list}')
        print(f'Исключаем сюты в которых есть теги: {self.tags} \n--------------------------------------')
        self.suites = TestData(source='tests')
        self._check_tag(self.suites)
        print(f'\nФинальный список сютов: {self.suites_list}')

    def _check_tag(self, s):
        if s.testcase_table.tests:
            tags = get_tags(s)
            print(f'Перечень тегов сюта: \'{s.name}\' - {tags}')
            if [tag for tag in self.tags if tag in tags]:
                self.suites_list.remove(s.name)
                print(f'|------> Cют \'{s.name}\' исключен')

        for child_suite in s.children:
            self._check_tag(child_suite)


def get_tags(suite):
    tags = []

    if suite.setting_table.force_tags:
        tags.extend(suite.setting_table.force_tags.value)

    if suite.setting_table.default_tags:
        tags.extend(suite.setting_table.default_tags.value)

    for testcase in suite.testcase_table.tests:
        if testcase.tags:
            tags.extend(testcase.tags.value)

    return tags


ExcludedSuites('Newton, wiki')
