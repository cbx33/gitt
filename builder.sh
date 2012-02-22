#!/bin/bash

make print
cp gitt.pdf ../tempo/print.pdf
make screen
cp gitt.pdf ../tempo/screen.pdf
make mobi
cp build/complete.mobi ../tempo/
make epub
cp build/complete.epub ../tempo/
make site
