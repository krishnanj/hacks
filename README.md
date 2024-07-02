# Hacks
Some hacky scripts that may come in handy time to time.

# Summary

## Scripts Overview

### 1. `convert.sh`
**Purpose:** Converts multiple .pdf files to .eps format.

**Process:**
- Locates all .pdf files in the current directory.
- Converts each found .pdf file into an .eps file using the `convert` command with specific density, units, and size parameters.
- Displays progress for each file during the conversion.

### 2. `github.sh`
**Purpose:** Migrates a git repository to a new GitHub repository.

**Process:**
- Adds a new remote repository location on GitHub.
- Mirrors the current repository to the new GitHub location.
- Changes the URL of the origin to the new GitHub repository and removes the temporary GitHub remote.

### 3. `rename.py`
**Purpose:** Renames all files in the current directory with a specified format.

**Process:**
- Iterates over each file in the current directory.
- Renames each file with a prefix followed by a sequential number and retains its original format (.png).

### 4. `runlatex.py`
**Purpose:** Automates the compilation of LaTeX files.

**Process:**
- Accepts command line arguments to determine the type of LaTeX compilation (e.g., pdflatex, xelatex), the filename, and whether to run BibTeX.
- Depending on the number of arguments, it compiles the LaTeX file, optionally runs BibTeX, and provides completion status.

### 5. `search_old.py`
**Purpose:** Searches for a specified string within files of the current directory, excluding certain file types.

**Process:**
- Takes a string to search as an input argument.
- Uses the `grep` command to perform a recursive search in the current directory, excluding specific file types like .html, .js, and .dat.
- Prints out where the string occurs within the files.

### 6. `billion_bday.py`

**Purpose:** Calculates the exact dates and times when various milestones in seconds are reached since a given birth date.

**Process:**
- Defines the birth date and time as a list and converts it into a datetime object.
- Creates a list of milestone labels corresponding to powers of ten (e.g., "1 second", "10 seconds", "1 million seconds", etc.).
- Iterates through each power of ten from 10^0 to 10^9.
- For each iteration, calculates the time delta in seconds.
- Adds the calculated time delta to the birth date to determine the new date and time.
- Prints the milestone label and the corresponding new date and time.

## Usage

Each script is designed for ease of use with command-line operation, enhancing productivity and streamlining tasks. Users should ensure proper execution permissions and dependencies are set before running the scripts.


[Ajay Mandyam Rangarajan](https://armandyam.github.io/) also contributed to this repository.
