# latex-motivator++

import subprocess
import os
import time
import sys
from datetime import date
import ascii_motivators as motivators
import csv

LM_DIR = '.latex-motivator'
LM_CONFIG_FILE = LM_DIR + '/lm.cfg'
LM_STATS_FILE = LM_DIR + '/stats.csv'
LM_CONFIG_SECTION = 'lm-section'


def get_raw_texcount(tex_file):
    perl_command = 'perl texcount.pl  -inc -brief ' + tex_file
    date = subprocess.Popen('date', stdout=subprocess.PIPE).stdout.read()
    texcount = subprocess.Popen(perl_command, stdout=subprocess.PIPE, shell=True).stdout.read()
    return texcount
        
def get_current_count(tex_file):
    raw_texcount = get_raw_texcount(tex_file)
    current_count = int(raw_texcount.splitlines()[-1].split('+')[0])
    return current_count

def get_stats():
    #open the stats csv file, return array
    stats_file = open(LM_STATS_FILE,"rU")
    reader = csv.reader(stats_file)
    stats_list = [tuple(row) for row in reader]
    stats_file.close()
    return stats_list
    
def update_current_count(current_count, stats):
    stats_file = open(LM_STATS_FILE,"w+")
    writer = csv.writer(stats_file)
    writer.writerows(stats)
    writer.writerow((date.today(), current_count))
    stats_file.close()
      
def get_last_count(stats):
    return int(stats[len(stats)-1][1])
        
def get_motivating_message(diff):
    if diff <= 250:
        return "Get working, slacker!"
    elif diff <= 500:
        return "Well, that's something. A small something! Get cracking!"
    elif diff <= 1000:
        return "Whoohoo! You've cracked the magic 500. Now get back to work!"
    elif diff <= 1500:
        return "OMG you've, like, written, like, literally, over, like, a thousand words!!!11!1!"
    elif diff <= 2500:
        return "You're. On. FIRE!"
    else:
        return """Amazeballs! Treat yourself to some cake... then come back and write some more!"""
  
 # todo: the props should be a dictionary...
def print_current_summary(config):
    print_motivator_says(config)
    
    stats = get_stats()
    last_count = get_last_count(stats)
    current_count = get_current_count(config.get(LM_CONFIG_SECTION, 'tex-file'))
    update_current_count(current_count, stats)
    
    goal_count = config.getint(LM_CONFIG_SECTION, 'goal-count')
    diff = current_count - last_count 
    motivation = get_motivating_message(diff)
    print "* You have written " + `diff` + " words. " + motivation
    percentdone = `(current_count/float(goal_count))*100`[0:4]
    print "* In total you have written " + `current_count` + " words." 
    print "* Given that you need around " + `goal_count` + " words, you are "+ percentdone + "% done!\n" 
    
    

#todo: could turn this into a dictionary: dino: ("the dino says", dino ascii)
def print_motivator_says(config):
    motivator = config.get('lm-section', 'motivator')
    if motivator == 'ducks':
        print motivators.get_ducks() + "\n" 
        print "The motivating ducks say: \n"
    elif motivator == 'fox':
        print motivators.get_fox() + "\n"
        print "The motivating fox says: \n"
    elif motivator == 'dino':
        print motivators.get_dino() + "\n"
        print "The motivating dinosaur says: \n"
    elif motivator == 'owl':
        print motivators.get_owl() + "\n"
        print "The motivating owl says: \n"
    

def print_total_summary():
    yearstart = date(2010,1,1)
    start = date(2009,10,19)
    today = date.today()
    yearavg = (current_count - 4817.0)/(today - yearstart).days
    avg = (current_count - 4817.0)/(today - start).days
    print "* You have written "+ `current_count - 4817` + " words in 2010." 
    print "* Your average words/day for this year: "+`int(round(yearavg))`+"."
    print "* Your average words/day from Oct 19th: "+`int(round(avg))`+"."

