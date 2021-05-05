#!/usr/bin/env python
import sys
import os

# Take input argument as one string

NoOfCommandLineArguments = len(sys.argv[1:])
if(NoOfCommandLineArguments>1 or NoOfCommandLineArguments==0):
	print "Error!\nUsage: search 'StringToSearch'"
else:
	StringToSearch = sys.argv[1]
	print "Searching for '"+StringToSearch +"' in current directory"
	CommandToSearch = "grep -R --exclude=*{.html,.js,.dat} '"+StringToSearch+"' ."
 	os.system(CommandToSearch)
