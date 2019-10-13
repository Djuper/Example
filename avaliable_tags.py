from robot.parsing import TestData


def main():
    suite = TestData(parent=None, source='tests')
    tags = get_tags(suite)
    print(", ".join(sorted(set(tags))))


def get_tags(suite):
    tags = []

    if suite.setting_table.force_tags:
        tags.extend(suite.setting_table.force_tags.value)

    if suite.setting_table.default_tags:
        tags.extend(suite.setting_table.default_tags.value)

    for testcase in suite.testcase_table.tests:
        if testcase.tags:
            tags.extend(testcase.tags.value)

    for child_suite in suite.children:
        tags.extend(get_tags(child_suite))

    return tags


main()
