#!/usr/bin/env python
import sys
import glob, os

# Check if the number of command line arguments is greater than three
# The first command line argument(apart from the name of the program) has to be which type of latex
# compilation has to be done - pdflatex, xelatex etc
# The second one has to be the name of the file with or without '.tex' extension
# The third has to be to specify if bibtex has to be run or not

# Usage for this is such that we specify the name of the .tex file to be executed.
# If the name given has '.tex' already then we can proceed to remove it for bibtex if not then can 
# optionally added for latex

NoOfCommandLineArguments = len(sys.argv[1:])

if(NoOfCommandLineArguments>3 or NoOfCommandLineArguments==0):
	print 'Error!\nUsage: runlatex TypeOfLatexCompilation NameOfTeXFile BibTeXOption\nSet BibTeXOption = 1 to run bibTeX'
elif(NoOfCommandLineArguments==1):
	print 'Error!\nUsage: runlatex TypeOfLatexCompilation NameOfTeXFile BibTeXOption\nSet BibTeXOption = 1 to run bibTeX'
elif(NoOfCommandLineArguments==2):
	# Use the type of LaTeX compilation
	TypeOfLatexCompilation = sys.argv[1]
	# The name of the file to be compiled. Could be with or without the '.tex' extension
	NameOfTeXFile = sys.argv[2]
	CommandToCall = TypeOfLatexCompilation+" -shell-escape -interaction=nonstopmode "+NameOfTeXFile
 	os.system(CommandToCall)
 	print '\n\n\n\n'+TypeOfLatexCompilation+' Compilation complete!'
else:
	# Use the type of LaTeX compilation
	TypeOfLatexCompilation = sys.argv[1]
	# The name of the file to be compiled. Could be with or without the '.tex' extension
	NameOfTeXFile = sys.argv[2]
	BiBTexName = ''
	for file in glob.glob("*.bib"):
		BiBTexName = file
	
	CommandToCall = TypeOfLatexCompilation+" -shell-escape -interaction=nonstopmode "+NameOfTeXFile
 	os.system(CommandToCall)

 	# Call BibTeX
 	CommandToCallBibTeX = "bibtex "+BiBTexName
 	os.system(CommandToCallBibTeX)

 	# Call the correct type of latex twice
	os.system(CommandToCall)
	os.system(CommandToCall)
 	print '\n\n\n\n'+TypeOfLatexCompilation+' and BibTex'+' Compilation complete!'
