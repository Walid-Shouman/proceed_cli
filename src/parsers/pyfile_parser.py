from models.Function import Function
import re
import settings

def fetch_functions_of_pyfile(pyfile):

	functionList = []
	notAppendedFunction = False
	implemented = False
	index = 0

	for line in open(pyfile,'r'):
		line = line.rstrip('\n')
		splitLine = filter(bool, re.split('[ ]+|\(', line))

		# if (settings.VERBOSE == True):
		# 	print "splitLine"
		# 	print line
		# 	print splitLine

		if len(splitLine) > 0:
			part1 = splitLine[0]

			# if (settings.VERBOSE == True):
			# 	print "line: " + line
			# 	print "part1" + part1

			if part1 == "def":
				# if (settings.VERBOSE == True):
				# 	print "part2" + splitLine[1]

				if (notAppendedFunction == True):
					# print functionName
					# print implemented
					prevFunction = Function(index, functionName, implemented)
					index = index + 1
					functionList.append(prevFunction)
					notAppendedFunction = False

				notAppendedFunction = True

				functionName = splitLine[1]
				implemented = True

		if line.find("TODO") > -1:
			implemented = False

	if (notAppendedFunction == True):
		# print functionName
		# print implemented
		prevFunction = Function(index, functionName, implemented)
		functionList.append(prevFunction)

	return functionList

