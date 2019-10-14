import robot
from include_suite_by_tag import IncludeSuites

obj = IncludeSuites('wiki')
suites = obj.get_suites()

robot.run("tests", suite=suites, outputdir='output')
