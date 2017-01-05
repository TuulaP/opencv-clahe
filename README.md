# opencv-clahe-nlf

An experimental Windows version of opencv-clahe-nlf for Visual Studio 2015.

## Background

Original code from the 
https://github.com/joshdoe/opencv-clahe


## Changes

Updated project file to VS 2015, added property sheet for opencv libraries and created .sln to combine all.


## Prerequisites

Compilation requires opencv 2.3.1~.  The property file contain
a library directories and library files , but change the paths according to settings in given environment.

Running program has dependency req to couple of opencv dlls, which are included.


## TODO & :warning: 

* sort out the extra dlls real need
* opencv version could be upgraded to a newer one from 2.3.1 
etc.


# Compilation

Once you have setup opencv

1. Open the opencv-clahe-nlf.sln in Visual Studio
2. Pick Release, x64 and build solution

You should get to executable called 'clahe.exe'

In case of issues check property files, that opencv directories and libraries are correct.


## Usage

clahe.exe image.png

Without image assumes and tries to use webcamera of the machine.
NB. You can shutdown the program windows via Esc.




