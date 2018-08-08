#!/bin/bash
rm [0-9]*

python3 gen.py

for f in [0-9]**.svg
do
	echo $f
	inkscape $f --export-pdf=$f.pdf
	# rsvg-convert -f pdf -o $f.pdf $f
done

pdftk [0-9]*.pdf cat output output.pdf