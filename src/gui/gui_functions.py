
# use simplejson to ease debugging
import simplejson as sjson
from dotmap import DotMap

import settings

def provide_pyfile(socket, pyfile):

	if settings.VERBOSE:
		print "Provided pyfile: " +pyfile.name+ " (" +pyfile.id+ ")"

	msg = socket.send(pyfile.get_json())

	# # parse json
	# parsedMsg = sjson.loads(msg)

	# if settings.VERBOSE:
	# 	print "Parsed message is: " + str(parsedMsg)

	# parsedMsgMap = DotMap(parsedMsg)
	# parsedSettings = parsedMsgMap.settings

	# # get the different settings and overwrite the settings with it
	# result = ""
	# for parsedSetting, value in parsedSettings.iteritems():
	# 	if parsedSetting in dir(settings):
	# 		# TODO: instead of dir-ing a class' attributes.
	# 		#       make all the settings in a dictionary.
	# 		#       and use ```if parsedSetting in settings:``` directly
	# 		settings.__dict__[parsedSetting] = value
	# 		result += 'Value of {0} is set to {1}!\n'.format(parsedSetting, value)

	# print result
	# socket.send(result)

def provide_pyfile_are_over(socket):
	socket.send("rep_no_more_pyfiles")
