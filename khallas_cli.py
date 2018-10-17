import os
import sys
import argparse

sys.path.append('./src')

import lib.interpc as interpc

# Conversion for arguments
import common.conversion as conv

import creator

import settings
import gui.gui_settings as gsettings
import gui.gui_functions as gfunctions

def check_pid(pid):        
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

def get_args():
	# Set defaults
	IS_GUI_DEFAULT			= False

	# Handle different args
	parser = argparse.ArgumentParser(prog='khallas')

	parser.add_argument('--gui', dest='isGUI', default=IS_GUI_DEFAULT, type=conv.str2bool)

	args = parser.parse_args()

	return args

def main():
	# Get arguments
	args = get_args()

	parentPID = os.getppid()

	print parentPID

	fh = open("parentPID.txt", "w")
	fh.write(str(parentPID))
	fh.close()

	if args.isGUI is True:
		print "--------------"
		socket = interpc.open_and_get_socket()
		# allow overwrite of parameters by zmq
		# gsettings.modify_settings_by_gui(socket)

	# parse doxygen class xml
	[pyFileList] = creator.create()


	# Create output dir if not found
	f = open(settings.LOG_FILE, "w")
	f.write("Started logging\n")
	if args.isGUI is True:
		index = -1

		# won't work, we need the grandparent, or better, get it in a zmq message
		# while(check_pid(parentPID)):
		# 	socket.RCVTIMEO = 1000

		# 	socket.recv()

		# 	if (msg == "init_req_pyfile"):
		# 		[pyFileList] = creator.create()

		# 		for pyFile in pyFileList:
		# 			index = index + 1
		# 			# receive before each sending
		# 			msg = socket.recv()
		# 			f.write("Received message: " + msg + " through zmq.\n")

		# 			if (msg == "init_req_pyfile") or (msg == "req_pyfile"):
		# 				gfunctions.provide_pyfile(socket, pyFile)

		# 			else:
		# 				socket.send("Sent message wasn't expected")

		# 		# receive before each sending
		# 		msg = socket.recv()
		# 		if (msg == "init_req_pyfile") or (msg == "req_pyfile"):
		# 			f.write("Sending closure message\n")
		# 			gfunctions.provide_pyfile_are_over(socket)

		# 		f.close()
		# 		socket.close()


		for pyFile in pyFileList:
			index = index + 1
			# receive before each sending
			msg = socket.recv()
			f.write("Received message: " + msg + " through zmq.\n")

			if (msg == "init_req_pyfile") or (msg == "req_pyfile"):
				gfunctions.provide_pyfile(socket, pyFile)

			else:
				socket.send("Sent message wasn't expected")

		# receive before each sending
		msg = socket.recv()
		if (msg == "init_req_pyfile") or (msg == "req_pyfile"):
			f.write("Sending closure message\n")
			gfunctions.provide_pyfile_are_over(socket)

		f.close()
		socket.close()

	else:
		print "Run with --isGUI=true!"
if __name__ == '__main__':
	main()
