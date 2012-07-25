# LATEX-MOTIVATOR++
# Author:  SP Bail
# based on Dr Bijan Parsia's [1] LaTeX count script 
# Keeps track of latex wordcount and sends motivating messages. Oh yes.
# Feature 1: Keep track of wordcount + send motivating message
# Feature 2: Keeps track of progress in % of final count
# Feature 3: Keeps track of wordcount with date + count as CSV
# [1] http://www.cs.man.ac.uk/~bparsia/

#TODO: super mega feature: keep motivating messages in csv, with the respective lower limit
#TODO: plot progress
#TODO: figure out how to use distutils: http://docs.python.org/distutils/index.html


import count
import subprocess
import os
import time
import sys
import csv
from datetime import date
import ConfigParser
import ascii_motivators as motivators

LM_DIR = '.latex-motivator'
LM_CONFIG_FILE = LM_DIR + '/lm.cfg'
LM_STATS_FILE = LM_DIR + '/stats.csv'
LM_CONFIG_SECTION = 'lm-section'


# setup (-setup parameter): goal word count, main .tex file, save start date, animal setting (owl, ducks, fox, dinosaur, random)

def setup():
    config = ConfigParser.RawConfigParser()
    config.add_section('lm-section')
    goal_count = raw_input("What is your goal word count? >>  ")
    tex_file = raw_input("Your main tex file: >>  ")
    motivator = raw_input("Choose your motivating animal (ducks, owl, dino, fox, random): >>  ")
    
    config.set('lm-section', 'goal-count', goal_count)
    config.set('lm-section', 'tex-file', tex_file)
    config.set('lm-section', 'start-date', date.today())
    config.set('lm-section', 'motivator', motivator)   
    
    # Writing our configuration file 
    if not os.path.exists(LM_DIR):
        os.makedirs(LM_DIR)
    with open(LM_CONFIG_FILE, 'wb') as f:
        config.write(f)
    
    count.update_current_count(0, ())
        


def get_config():
    config = ConfigParser.RawConfigParser()
    config.read(LM_CONFIG_FILE)    
    return config
    
    
if __name__ == "__main__":

    if len(sys.argv) > 1:
        if sys.argv[1] == '--setup':
            setup()
            
    if os.path.isfile(LM_CONFIG_FILE) == False:
        setup()
    config = get_config()
    count.print_current_summary(config)
    
    
    