#!/bin/bash
# convert multiple .eps files to .jpeg 

cd $(pwd)    
eps_files=$(find . -iname "*.pdf")

total=$(echo "$eps_files" | wc -l)
num=0

echo "There are $total files to be converted."

for f in $eps_files
do
    ((num++))
    echo "Converting $f, $num/$total"   
    convert -density 150  -units PixelsPerInch -resize 2475x3525 "$f" "${f%.pdf}.eps" 
done
