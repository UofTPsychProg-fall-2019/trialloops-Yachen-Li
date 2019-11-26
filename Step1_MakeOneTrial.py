#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color = 'white', unit='height') 
trialClock = core.Clock()


instruct = visual.TextStim(win, color = 'black', height = .05, text="Verify the number of dots either from your perspective or from his perspective. Press Q if the number matches the number of dots, press P if the number does not match. Please respond as fast as you can. Press any key to proceed with the task")
instruct.draw()
win.flip()

if 'escape' in event.waitKeys():
    core.quit()

fixation = visual.TextStim(win, text='+', color = 'black', height=.05) 
fixation.draw()
win.flip()
core.wait(0.75)

perspect = visual.TextStim(win, text= 'You', color = 'black', height = .05)
perspect.draw()
win.flip()
core.wait(0.75)

dots = visual.TextStim(win, text= '1', color = 'black', height = .05)
dots.draw()
win.flip()
core.wait(0.75)

myimage = 'Perspective/1consist.jpg'

mypic = visual.ImageStim(win,image= myimage, pos = (0,0),size=1,interpolate=True)
mypic.draw()
win.flip()
core.wait(2)


keys = event.waitKeys(maxWait = 2, keylist = ('Q','P'))
print(keys)

if keys==None:
    keys=[]
    keys.append("no key")
    

win.close()
core.quit()

 
