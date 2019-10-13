from robot.parsing import TestData


class ProjectSuites:

    def __init__(self):
        self.suites = TestData(parent=None, source='tests')
        self.all_suites_list = []
        self.suites_list = []
        self._get_suites_common(self.suites)

    def get_suites(self):
        return self.suites_list

    def get_all_suites(self):
        return self.all_suites_list

    def _get_suites_common(self, s):
        self.all_suites_list.append(s.name)
        if s.testcase_table.tests:
            self.suites_list.append(s.name)

        for child_suite in s.children:
            self._get_suites_common(child_suite)
