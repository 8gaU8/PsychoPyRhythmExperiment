#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on 日  7/ 9 20:32:20 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from sound_stim
import sys
sys.path.append("./pkgs")

from main import run_stim
sound_stim_routine_index = 0
import numpy as np
np.random.seed(1)
delay_series = np.random.normal(loc=0, scale=0.3, size=300).clip(-0.2, 0.2)
scale_series = 1 + np.random.normal(loc=0, scale=0.3, size=300)



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = 'rhythm_trial_exp'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/hagayuya/Devs/NIDLab/PsychoPyTutorial/rhythm_trial_exp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "instruction" ---
text_norm = visual.TextStim(win=win, name='text_norm',
    text='リズム実験（テスト）\n\nクロスが表示されたあとにキーボードで回答\nProbe Toneが早ければb\n遅ければn\n\nSpaceで開始\n',
    font='Osaka',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_instruct = keyboard.Keyboard()
# Run 'Begin Experiment' code from text_align
# Code components should usually appear at the top
# of the routine. This one has to appear after the
# text component it refers to.
text_norm.alignText= 'center'

# --- Initialize components for Routine "blank" ---
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# --- Initialize components for Routine "blank" ---
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# --- Initialize components for Routine "trial" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
key_resp = keyboard.Keyboard()
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# --- Initialize components for Routine "blank" ---
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# --- Initialize components for Routine "break_2" ---
text_norm_2 = visual.TextStim(win=win, name='text_norm_2',
    text='休憩\n\nSpaceで再開',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_instruct_2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from text_align_2
# Code components should usually appear at the top
# of the routine. This one has to appear after the
# text component it refers to.
text_norm.alignText= 'center'

# --- Initialize components for Routine "blank" ---
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# --- Initialize components for Routine "ending_message" ---
text_norm_3 = visual.TextStim(win=win, name='text_norm_3',
    text='実験はこれで終了です',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_instruct_3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from text_align_3
# Code components should usually appear at the top
# of the routine. This one has to appear after the
# text component it refers to.
text_norm.alignText= 'left'

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instruction" ---
continueRoutine = True
# update component parameters for each repeat
key_instruct.keys = []
key_instruct.rt = []
_key_instruct_allKeys = []
# keep track of which components have finished
instructionComponents = [text_norm, key_instruct]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_norm* updates
    
    # if text_norm is starting this frame...
    if text_norm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_norm.frameNStart = frameN  # exact frame index
        text_norm.tStart = t  # local t and not account for scr refresh
        text_norm.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_norm, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_norm.status = STARTED
        text_norm.setAutoDraw(True)
    
    # if text_norm is active this frame...
    if text_norm.status == STARTED:
        # update params
        pass
    
    # if text_norm is stopping this frame...
    if text_norm.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_norm.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_norm.tStop = t  # not accounting for scr refresh
            text_norm.frameNStop = frameN  # exact frame index
            # update status
            text_norm.status = FINISHED
            text_norm.setAutoDraw(False)
    
    # *key_instruct* updates
    waitOnFlip = False
    
    # if key_instruct is starting this frame...
    if key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_instruct.frameNStart = frameN  # exact frame index
        key_instruct.tStart = t  # local t and not account for scr refresh
        key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_instruct, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_instruct.started')
        # update status
        key_instruct.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_instruct.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_instruct.status == STARTED and not waitOnFlip:
        theseKeys = key_instruct.getKeys(keyList=['space'], waitRelease=False)
        _key_instruct_allKeys.extend(theseKeys)
        if len(_key_instruct_allKeys):
            key_instruct.keys = _key_instruct_allKeys[0].name  # just the first key pressed
            key_instruct.rt = _key_instruct_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction" ---
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_instruct.keys in ['', [], None]:  # No response was made
    key_instruct.keys = None
thisExp.addData('key_instruct.keys',key_instruct.keys)
if key_instruct.keys != None:  # we had a response
    thisExp.addData('key_instruct.rt', key_instruct.rt)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [ISI]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI* period
    
    # if ISI is starting this frame...
    if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI.frameNStart = frameN  # exact frame index
        ISI.tStart = t  # local t and not account for scr refresh
        ISI.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('ISI.started', t)
        # update status
        ISI.status = STARTED
        ISI.start(1)
    elif ISI.status == STARTED:  # one frame should pass before updating params and completing
        ISI.complete()  # finish the static period
        ISI.tStop = ISI.tStart + 1  # record stop time
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank" ---
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code
win.flip()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
session = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='session')
thisExp.addLoop(session)  # add the loop to the experiment
thisSession = session.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSession.rgb)
if thisSession != None:
    for paramName in thisSession:
        exec('{} = thisSession[paramName]'.format(paramName))

for thisSession in session:
    currentLoop = session
    # abbreviate parameter names if possible (e.g. rgb = thisSession.rgb)
    if thisSession != None:
        for paramName in thisSession:
            exec('{} = thisSession[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "blank" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        blankComponents = [ISI]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *ISI* period
            
            # if ISI is starting this frame...
            if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI.frameNStart = frameN  # exact frame index
                ISI.tStart = t  # local t and not account for scr refresh
                ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('ISI.started', t)
                # update status
                ISI.status = STARTED
                ISI.start(1)
            elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                ISI.complete()  # finish the static period
                ISI.tStop = ISI.tStart + 1  # record stop time
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code
        win.flip()
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from sound_stim
        delay = delay_series[sound_stim_routine_index]
        scale = scale_series[sound_stim_routine_index]
        run_stim(delay=delay, scale=scale)
        trials.addData('stim.delay', delay)
        trials.addData('stim.scale', scale)
        sound_stim_routine_index += 1
        # keep track of which components have finished
        trialComponents = [cross, key_resp, ISI_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            
            # if cross is starting this frame...
            if cross.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.started')
                # update status
                cross.status = STARTED
                cross.setAutoDraw(True)
            
            # if cross is active this frame...
            if cross.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['b', 'n'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *ISI_2* period
            
            # if ISI_2 is starting this frame...
            if ISI_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI_2.frameNStart = frameN  # exact frame index
                ISI_2.tStart = t  # local t and not account for scr refresh
                ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('ISI_2.started', t)
                # update status
                ISI_2.status = STARTED
                ISI_2.start(0.5)
            elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
                ISI_2.complete()  # finish the static period
                ISI_2.tStop = ISI_2.tStart + 0.5  # record stop time
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        blankComponents = [ISI]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *ISI* period
            
            # if ISI is starting this frame...
            if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI.frameNStart = frameN  # exact frame index
                ISI.tStart = t  # local t and not account for scr refresh
                ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('ISI.started', t)
                # update status
                ISI.status = STARTED
                ISI.start(1)
            elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                ISI.complete()  # finish the static period
                ISI.tStop = ISI.tStart + 1  # record stop time
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code
        win.flip()
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials.saveAsText(filename + 'trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "break_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_instruct_2.keys = []
    key_instruct_2.rt = []
    _key_instruct_2_allKeys = []
    # keep track of which components have finished
    break_2Components = [text_norm_2, key_instruct_2]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "break_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_2* updates
        
        # if text_norm_2 is starting this frame...
        if text_norm_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_2.frameNStart = frameN  # exact frame index
            text_norm_2.tStart = t  # local t and not account for scr refresh
            text_norm_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_2.status = STARTED
            text_norm_2.setAutoDraw(True)
        
        # if text_norm_2 is active this frame...
        if text_norm_2.status == STARTED:
            # update params
            pass
        
        # *key_instruct_2* updates
        waitOnFlip = False
        
        # if key_instruct_2 is starting this frame...
        if key_instruct_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instruct_2.frameNStart = frameN  # exact frame index
            key_instruct_2.tStart = t  # local t and not account for scr refresh
            key_instruct_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instruct_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_instruct_2.started')
            # update status
            key_instruct_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instruct_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instruct_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instruct_2.status == STARTED and not waitOnFlip:
            theseKeys = key_instruct_2.getKeys(keyList=['space'], waitRelease=False)
            _key_instruct_2_allKeys.extend(theseKeys)
            if len(_key_instruct_2_allKeys):
                key_instruct_2.keys = _key_instruct_2_allKeys[0].name  # just the first key pressed
                key_instruct_2.rt = _key_instruct_2_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "break_2" ---
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_instruct_2.keys in ['', [], None]:  # No response was made
        key_instruct_2.keys = None
    session.addData('key_instruct_2.keys',key_instruct_2.keys)
    if key_instruct_2.keys != None:  # we had a response
        session.addData('key_instruct_2.rt', key_instruct_2.rt)
    # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [ISI]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        
        # if ISI is starting this frame...
        if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('ISI.started', t)
            # update status
            ISI.status = STARTED
            ISI.start(1)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 1  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank" ---
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    win.flip()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'session'

# get names of stimulus parameters
if session.trialList in ([], [None], None):
    params = []
else:
    params = session.trialList[0].keys()
# save data for this loop
session.saveAsExcel(filename + '.xlsx', sheetName='session',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
session.saveAsText(filename + 'session.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "ending_message" ---
continueRoutine = True
# update component parameters for each repeat
key_instruct_3.keys = []
key_instruct_3.rt = []
_key_instruct_3_allKeys = []
# keep track of which components have finished
ending_messageComponents = [text_norm_3, key_instruct_3]
for thisComponent in ending_messageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ending_message" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_norm_3* updates
    
    # if text_norm_3 is starting this frame...
    if text_norm_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_norm_3.frameNStart = frameN  # exact frame index
        text_norm_3.tStart = t  # local t and not account for scr refresh
        text_norm_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_norm_3, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_norm_3.status = STARTED
        text_norm_3.setAutoDraw(True)
    
    # if text_norm_3 is active this frame...
    if text_norm_3.status == STARTED:
        # update params
        pass
    
    # *key_instruct_3* updates
    waitOnFlip = False
    
    # if key_instruct_3 is starting this frame...
    if key_instruct_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_instruct_3.frameNStart = frameN  # exact frame index
        key_instruct_3.tStart = t  # local t and not account for scr refresh
        key_instruct_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_instruct_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_instruct_3.started')
        # update status
        key_instruct_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_instruct_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_instruct_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_instruct_3.status == STARTED and not waitOnFlip:
        theseKeys = key_instruct_3.getKeys(keyList=['space'], waitRelease=False)
        _key_instruct_3_allKeys.extend(theseKeys)
        if len(_key_instruct_3_allKeys):
            key_instruct_3.keys = _key_instruct_3_allKeys[0].name  # just the first key pressed
            key_instruct_3.rt = _key_instruct_3_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ending_messageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ending_message" ---
for thisComponent in ending_messageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_instruct_3.keys in ['', [], None]:  # No response was made
    key_instruct_3.keys = None
thisExp.addData('key_instruct_3.keys',key_instruct_3.keys)
if key_instruct_3.keys != None:  # we had a response
    thisExp.addData('key_instruct_3.rt', key_instruct_3.rt)
thisExp.nextEntry()
# the Routine "ending_message" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
