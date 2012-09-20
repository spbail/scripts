scripts
=======

Random scripts for... stuff.
Author: sbail
Each directory contains a test dir with data + script to run the test

** Merge CSV **

Merge CSV merges CSV files by columns, taking the first column as a key.
E.g. if you have something like this:

File 1

Name | Age | Phone number

File 2

Name | Address

The resulting CSV file will be

Name | Age | Phone number | Address

Duplicates are removed and keys without match discarded. 

The script is very basic and the code probably dodgy, but it works alright for my stuff.