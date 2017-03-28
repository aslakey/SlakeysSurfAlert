'''
Slakeys Surf Alert

Add Users with the argument "add" "user name * email * surf spot name * surf spot url"

Run with the argument "run"


'''
import sys
from SurfAlertUtils import *

if __name__ == "__main__":
	args = sys.argv
	args.pop(0)
	if len(args) == 0:
		print("Welcome to Slakey\'s Surf Alert. If you have not added a user, please input \"add\" \"user\" \"email\" \"surfspot\" \"url\". If you want to run just input \"run\"")
	elif args[0] == "run":
		run()
	elif args[0] == "add":
		adduser(args[1:])
