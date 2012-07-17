# merge_csv.py v1.0
# sbail@delorean, 17/07/2012
# appends columns from other csv files to a csv, using the first column as the key
# seriously hideous code atm, but does the job

# todo: allow user to specify the column to be used as key
# todo: remove duplicate columns in the resulting csv


import csv
import numpy as np
import sys
import os

def load_dict_from_csv(filename):
	f = open(filename,"rU")
	reader = csv.reader(f)
	header = reader.next()
	dict = {}
	
	for row in reader:
	    key = row[0]
	    values = row[1:]
	    dict[key] = values
	    
	f.close() 
	return dict
	
	
def dict_to_list(dict):
    result = []
    for key, value in dict.iteritems():
        row = [key]
        row.extend(value)
        result.append(row) 
    return result


def get_result_dict(master, all_csvs):
    result_csv_dict = {}
    for key, value in master.iteritems():
        row_values = []
        key_occurs_in_all_csvs = True
        #check if all csv files have entries for this key
        for csv in all_csvs:
            if key in csv:
                row_values.extend(csv[key])
            else:
                key_occurs_in_all_csvs = False
       #if all csv files have an entry for this key, append to the resulting dict         
        if key_occurs_in_all_csvs:
            tmp = value
            tmp.extend(row_values)
            result_csv_dict[key] = tmp
    return result_csv_dict

def get_header(files):
    header = []
    
    master = open(files[0],"rU")
    reader = csv.reader(master)
    header.extend(reader.next())
    master.close()
	    
    for filename in files[1:]:
        f = open(filename,"rU")
        reader = csv.reader(f)
        row = reader.next()
        header.extend(row[1:])
        f.close()
    
    return header
	
def save_result(header, result, master_filename):
    result_filename = os.path.splitext(master_filename)[0] + "_merged.csv"
    result_file = open(result_filename, 'w')
    writer = csv.writer(result_file)
    writer.writerow(header)
    writer.writerows(result)
        
    result_file.close()
    
    print "\nSaved merged output to ", result_filename, "\n"
            
            
if __name__ == "__main__":
    files = sys.argv[1:]
    
    header = get_header(files)
    
    master = load_dict_from_csv(files[0])
    
    all_csvs = []
    
    for f in files[1:]:
       all_csvs.append(load_dict_from_csv(f))
   
    result_csv_dict = get_result_dict(master, all_csvs)
    
    result_csv = dict_to_list(result_csv_dict) 
    
    save_result(header, result_csv, files[0])
    
                
        