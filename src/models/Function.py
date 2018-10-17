class Function:
	""" Function class """

	def __init__(self, id=None, name=None, completed=False):
		self.id				= id
		self.name 			= name
		self.completed		= completed

	@staticmethod
	def get_by_name(functionList, functionName):
		for function in functionList:
			if function.name == functionName:
				return function

		return None
