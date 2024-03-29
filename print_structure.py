from robot.api import TestData


def print_suite(suite):
    print('Suite:', suite.name)
    for test in suite.testcase_table:
        print('-', test.name)
    for child in suite.children:
        print_suite(child)


suite = TestData(source='tests')
print_suite(suite)
