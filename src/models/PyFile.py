
import settings

class PyFile:
	""" PyFile class. """

	def __init__(self, id="", name="", functions=[], incomplete_functions=[]):
		self.id						= id

		self.name					= name
		self.functions 				= functions
		self.incomplete_functions 	= incomplete_functions

	@staticmethod
	def get_by_id(pyFileList, id):
		for pyFile in pyFileList:
			if pyFile.id == id:
				return pyFile

		return None

	# TODO: internally use the __str__
	def get_json(self):
		returnString  = '{'
		returnString += '"pyFile": {'
		returnString += '"id": "{0}", '.format(str(self.id))
		returnString += '"name": "{0}", '.format(str(self.name))

		returnString += '"functions": ['
		for index, function in enumerate(self.functions):
			returnString += '{'+'"id": {0}, '.format(str(function.id))
			returnString += '"name": "{0}" '.format(str(function.name))
			returnString += '}'

			if (len(self.functions) != index+1): returnString += ', '

		returnString += '], '

		returnString += '"incomplete_functions": ['
		for index, function in enumerate(self.incomplete_functions):
			returnString += '{'+'"id": {0}, '.format(str(function.id))
			returnString += '"name": "{0}" '.format(str(function.name))
			returnString += '}'

			if (len(self.incomplete_functions) != index+1): returnString += ', '

		returnString += ']'

		returnString += '}'
		returnString += '}'

		return returnString


	def __str__(self):
		returnString = "pyFile: {"
		returnString += "id: {0}, ".format(str(self.id))
		returnString += "name: {0}, ".format(str(self.name))

		returnString += "functions: ["
		for index, function in enumerate(self.functions):
			returnString += "{"+"id: {0}, ".format(str(function.id))
			returnString += "name: {0} ".format(str(function.name))
			returnString += "}"

			if (len(self.functions) != index+1): returnString += ", "

		returnString += "], "

		returnString += "incomplete_functions: ["
		for index, function in enumerate(self.incomplete_functions):
			returnString += "{"+"id: {0}, ".format(str(function.id))
			returnString += "name: {0} ".format(str(function.name))
			returnString += "}"

			if (len(self.incomplete_functions) != index+1): returnString += ", "

		returnString += "]"

		returnString += "}"

		return returnString
