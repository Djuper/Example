from robot.parsing import TestData


class ProjectSuites:

    def __init__(self, tags):
        self.tags = list(tags.replace(" ", "").split(","))
        print('Ищем сюты в которых есть тег - ', self.tags, '\n--------------------------------------')
        self.suites = TestData(source='tests')
        self.suites_list = []
        self._check_tag(self.suites)
        print('\nФинальный список сютов:', self.suites_list)

    def _check_tag(self, s):
        if s.testcase_table.tests:
            tags = get_tags(s)
            print('Перечень тегов сюта', s.name, '-', tags)
            if [tag for tag in self.tags if tag in tags]:
                self.suites_list.append(s.name)
                print('|------> Cют', s.name, 'подходящий')

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


ProjectSuites('Newton, wiki')
