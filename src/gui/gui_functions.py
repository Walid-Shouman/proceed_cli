
# use simplejson to ease debugging
import simplejson as sjson
from dotmap import DotMap

import settings

def provide_pyfile(socket, pyfile):

	if settings.VERBOSE:
		print "Provided pyfile: " +pyfile.name+ " (" +pyfile.id+ ")"

	msg = socket.send(pyfile.get_json())


def provide_pyfile_are_over(socket):
	socket.send("rep_no_more_pyfiles")
