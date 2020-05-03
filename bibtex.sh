#!/bin/bash

WWWDIR="/www/roam"
BIBFILEDIR="$HOME/Documents/Mendeley/BibTeX"

# Get the current date time
DATETIME=$(date +%c)

# See if a citekey was passed
CITEKEY=$1
if [ $# -ne 1 ]; then
    echo "Error: Not Citekey for $0"
    exit 1
fi

# Setup citekey filename
CITEKEYFILE=$WWWDIR/$CITEKEY.md

# See if the citekey file exists
filename="$BIBFILEDIR/$CITEKEY.bib"
if [ ! -f $filename ]; then
    echo "Error: File not found - $filename"
    exit 2
fi

# See if .bib file contains }}
warning1=''
count=$(cat $filename | grep -v ^title | fgrep "}}" | wc -l)
if [ $count -gt 0 ]; then
    warning1="contains }}..."
fi

# See if .bib file contains {\%}
warning2=''
count=$(cat $filename | grep -v ^title | fgrep "{\%}" | wc -l)
if [ $count -gt 0 ]; then
    warning2="contains {\%}..."
fi

# Display message
echo ${CITEKEY}...${warning1}${warning2}

# Delete md file file if it exists
if [ -f $CITEKEYFILE ]; then
    rm $CITEKEYFILE
fi

# Extract the bibtex data
python3 bibtex.py $BIBFILEDIR $CITEKEY > $CITEKEYFILE

# See if md file exists
if [ ! -f $CITEKEYFILE ]; then
    echo "Error: File does not exist - $CITEKEYFILE"
    exit 3
fi

# Count lines in md file
count=$(cat $CITEKEYFILE | wc -l)
if [ $count -le 10 ]; then
    echo "Warning: File not complete - $CITEKEYFILE"
    exit 4
fi

# Success message
echo "Success: $CITEKEY"

#EOF