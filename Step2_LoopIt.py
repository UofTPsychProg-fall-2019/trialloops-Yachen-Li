#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging
import random

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
trialClock = core.Clock()


#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things
instruct = visual.TextStim(win, color = 'black', height = .05, text="Verify the number of dots either from your perspective or from his perspective. Press Q if the number matches the number of dots, press P if the number does not match. Please respond as fast as you can. Press any key to proceed with the task")
instruct.draw()
win.flip()

if 'escape' in event.waitKeys():
    core.quit()

# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']

stim = ['Perspective/1consist.jpg','Perspective/1inconsist.jpg','Perspective/2consist.jpg', 'Perspective/2inconsistA.jpg']
response = []
# make your loop
trialinfo = pd.read_csv('stim.csv')
trialinfo = trialinfo.sample(frac=1)
trialinfo = trialinfo.reset_index()

ntrial = len(trialinfo)

for thisTrial in np.arange(0,ntrial):
    fixation = visual.TextStim(win, text='+', color = 'black', height=.05) 
    fixation.draw()
    win.flip()
    core.wait(0.75)
    
    cuelist = ['You','He']
    cue = random.choice(cuelist)
    perspect = visual.TextStim(win, text= cue, color = 'black', height = .05)
    perspect.draw()
    win.flip()
    core.wait(0.75)
    
    dotlist = ['1','2']
    dotnumber = random.choice(dotlist)
    dots = visual.TextStim(win, text= dotnumber, color = 'black', height = .05)
    dots.draw()
    win.flip()
    core.wait(0.75)
    
    mypic = visual.ImageStim(win,image= i,units = 'pix',pos = (0,0),interpolate=True)
    mypic.draw()
    win.flip()
    core.wait(2)
    keys = event.waitKeys(maxWait = 2, keylist = ('Q','P'))
    print(keys)
    response.append([i, keys])
    
    mystim = visual.ImageStim(win, image = trialInfo.loc[thisTrial,'Perspective'],size =1, pos = (0,0),interpolate=True)
    out.loc[thisTrial,'Perspective'] = trialInfo.loc[thisTrial,'Perspective']
    out.loc[thisTrial,'trial'] = thisTrial + 1
    
    keys = event.waitKeys(maxWait = 2, keylist = ('Q','P'))
    print(keys)
    response.append([i, keys])
        
    
    while response.noResponse:
        mystim.draw()
        win.flip()
        
        
    goodbye = visual.TextStim(win, text = 'You are done with the task! Please inform your experimenter.')
    goodbye.draw()
    win.flip()
    core.wait(2)
    
 