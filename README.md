# image_duplicate_finder
A program to find, and delete duplicate images using image hashing.

# Features
* ability to find a folder given a name, or part of it's path

# command line Flags
* -ph" use phash instead of dhash for more accuracy, but less speed
* "-s" to print number of files processed
* "-d" to remove duplicate files
* "-t" to time how long the process takes
* "-pd" to print all duplicates found
* "-nd" to print the number of duplicates
* "-a" to go through all folders contained in the inital folder

# Requirements
* PIL
* imagehash
