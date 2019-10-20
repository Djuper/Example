from get_suites_list import GetSuitesList


content = """test_name:"""


for i in GetSuitesList().get_suites():
    content += f"\n - {i}"


with open('suites.yml', 'w') as f:
    f.write(content)


print(content)
