# Keyword Metrics Code: (save following snippet as python file and execute)
from robot.api import ExecutionResult, ResultVisitor

result = ExecutionResult('output\output.xml')
result.configure(stat_config={'suite_stat_level': 2,
                              'tag_stat_combine': 'tagANDanother'})


class KeywordMetrics(ResultVisitor):

    def visit_keyword(self, kw):
        print("Keyword Name: " + str(kw.name))
        print("Keyword Status: " + str(kw.status))
        print("Keyword Starttime: " + str(kw.starttime))
        print("Keyword Endtime: " + " " + str(kw.endtime))
        print("Keyword Elapsedtime (Sec): " + " " + str(kw.elapsedtime/float(1000)))


result.visit(KeywordMetrics())
