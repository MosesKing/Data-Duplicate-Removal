#!/usr/bin/env python

import hashlib

def getRid_Duplicates(inputFile, outputFile):

    assesed_lines_hash = set()

    output_file = open(outputFile, "w")

    for line in open(inputFile, 'r'):
        hashVal = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        if hashVal not in assesed_lines_hash:
            output_file.write(line)
            assesed_lines_hash.add(hashVal)

    output_file.close()

def main():

    output_file_path = 'c:/Users/Administrator/Desktop/noDupe.txt'
    input_file = input("Which file would you like to remove duplicates from (please put in full path): ")

    getRid_Duplicates(input_file, output_file_path)

    print("Duplicates Sucessfully Removed!")
    print("Please see the created file on YOUR desktop! ")

    input()

if __name__ == '__main__':
    main()
