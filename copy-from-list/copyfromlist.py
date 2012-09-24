import csv
import sys
import os
import shutil
import string
            
if __name__ == "__main__":

    if(len(sys.argv)>=4):
        args = sys.argv[1:]
        
        f = open(args[0],"rU")
        reader = csv.reader(f)
        for row in reader:
            filename = string.split(row[0])[0]
            srcfile = args[1] + filename
            if(os.path.exists(srcfile)):
                print "copying " + filename
                shutil.copytree(srcfile, args[2] + "/" + filename)
    
        f.close()
        
    else:
        print "usage: csvfile indir outdir [colindex]"

                
        