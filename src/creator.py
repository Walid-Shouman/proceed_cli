####################
## TODO: clean up ##
####################

import parsers.pyfile_parser    as parser

import settings
from settings import VERBOSE

from models.PyFile import PyFile
from models.Function import Function

import os

# create classes

def create_pyfile_list(pyfileId, pyfile):
	pyfileName = os.path.basename(pyfile)

	if (VERBOSE):
		print "processing pyfile: " + pyfileName

	# fetch functions
	functionList = parser.fetch_functions_of_pyfile(pyfile)

	completedFunctionList  = filter(lambda x: x.completed == True,  functionList)
	incompleteFunctionList = filter(lambda x: x.completed == False, functionList)
	pyf = PyFile(pyfileId, pyfileName, completedFunctionList, incompleteFunctionList)

	return pyf

def create():

	index = 0

	# get all the files in directory
	if (settings.pyfileDir is not None):
		pyfileList = []
		for (dirpath, dirnames, filenames) in os.walk(settings.pyfileDir):
			for filename in sorted(filenames):
				if filename.endswith(".py"):
					if (VERBOSE == True):
						print "processing file: " + filename
					parsedPyFile = create_pyfile_list(index, os.path.join(dirpath, filename))
					index = index+1
					pyfileList.append(parsedPyFile)

	# use a specific file
	else:
		# the list will be of one element
		parsedPyFile = create_pyfile_list(0, settings.pyfile)
		pyfileList.append(parsedPyFile)

	if (VERBOSE):
		print "----"
		for pyf in pyfileList:
			print pyf

	return [pyfileList]
