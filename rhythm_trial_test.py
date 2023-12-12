#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on September 21, 2023, at 12:35
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.5')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
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

# Run 'Before Experiment' code from init_modules
import sys
import time
sys.path.append("./pkgs")

from rhythm_trial_code.main import build_stim, play_stim
from rhythm_trial_code.message import PlayFactories as _PF
from rhythm_trial_code.serial_trigger import init_port

debug = False
port_name = "COM3"
if len(sys.argv) > 1:
    if sys.argv[-1] == "DEBUG":
        debug = True
    else:
        port_name = sys.argv[-1]

port = init_port(port_name, dummy=debug)

_play_trigger_on_cross = _PF([]).trig_fctr(port, [4])
play_trigger_on_cross = lambda: _play_trigger_on_cross(True)

_play_trigger_on_start = _PF([]).trig_fctr(port, [5])
play_trigger_on_start = lambda: _play_trigger_on_start(True)

_play_trigger_on_stim_start= _PF([]).trig_fctr(port, [6])
play_trigger_on_stim_start = lambda: _play_trigger_on_stim_start(True)

_play_trigger_on_ans = _PF([]).trig_fctr(port, [7])
play_trigger_on_ans = lambda: _play_trigger_on_ans(True)

_play_trigger_on_move = _PF([]).trig_fctr(port, [8])
play_trigger_on_move = lambda: _play_trigger_on_move(True)

_play_trigger_on_ans_enabled = _PF([]).trig_fctr(port, [9])
play_trigger_on_ans_enabled = lambda: _play_trigger_on_ans_enabled(True)

_play_trigger_on_end = _PF([]).trig_fctr(port, [10])
play_trigger_on_end = lambda: _play_trigger_on_end(True)


# reset Port
port.write([0])



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'rhythm_trial_test'  # from the Builder filename that created this script
expInfo = {
    'participant': 'test',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'test_data/test'

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\data\\haga\\PsychoPyRhythmExperiment\\rhythm_trial_test.py',
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
    size=[1680, 1050], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# --- Initialize components for Routine "prepare" ---

# --- Initialize components for Routine "blank" ---
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# --- Initialize components for Routine "trial_inst" ---
text_norm_4 = visual.TextStim(win=win, name='text_norm_4',
    text='',
    font='Osaka',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from text_align_4
# Code components should usually appear at the top
# of the routine. This one has to appear after the
# text component it refers to.
text_norm_4.alignText= 'center'

# --- Initialize components for Routine "fixation_cross" ---
cross_white = visual.ShapeStim(
    win=win, name='cross_white', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6, 0, 0.7], fillColor=[0.6, 0, 0.7],
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "trial" ---
cross_white_2 = visual.ShapeStim(
    win=win, name='cross_white_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6, 0, 0.7], fillColor=[0.6, 0, 0.7],
    opacity=None, depth=0.0, interpolate=True)
cross_colored = visual.ShapeStim(
    win=win, name='cross_colored', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6, 0.7, 0], fillColor=[0.6, 0.7, 0],
    opacity=None, depth=-1.0, interpolate=True)
key_resp = keyboard.Keyboard()
key_resp_moving = keyboard.Keyboard()

# --- Initialize components for Routine "ending_message" ---
text_norm_3 = visual.TextStim(win=win, name='text_norm_3',
    text='実験はこれで終了です。\n\nお疲れ様でした！',
    font='Osaka',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_instruct_3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from text_align_3
# Code components should usually appear at the top
# of the routine. This one has to appear after the
# text component it refers to.
text_norm_3.alignText= 'center'

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "prepare" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
prepareComponents = []
for thisComponent in prepareComponents:
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

# --- Run Routine "prepare" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prepare" ---
for thisComponent in prepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prepare" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank" ---
continueRoutine = True
routineForceEnded = False
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
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI* period
    if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI.frameNStart = frameN  # exact frame index
        ISI.tStart = t  # local t and not account for scr refresh
        ISI.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('ISI.started', t)
        ISI.start(1)
    elif ISI.status == STARTED:  # one frame should pass before updating params and completing
        ISI.complete()  # finish the static period
        ISI.tStop = ISI.tStart + 1  # record stop time
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('exp_params/test.csv'),
    seed=0, name='trials')
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
    
    # --- Prepare to start Routine "trial_inst" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_norm_4.setText(msg)
    # Run 'Begin Routine' code from build_stim
    stim = build_stim(port=port, delay=delay, scale=scale, soundfiles=['./sound/SD1010.WAV','./sound/SD0050.WAV'])
    play_trigger_on_start()
    
    # keep track of which components have finished
    trial_instComponents = [text_norm_4]
    for thisComponent in trial_instComponents:
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
    
    # --- Run Routine "trial_inst" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_4* updates
        if text_norm_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_4.frameNStart = frameN  # exact frame index
            text_norm_4.tStart = t  # local t and not account for scr refresh
            text_norm_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_norm_4.started')
            text_norm_4.setAutoDraw(True)
        if text_norm_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_norm_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_norm_4.tStop = t  # not accounting for scr refresh
                text_norm_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_norm_4.stopped')
                text_norm_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_inst" ---
    for thisComponent in trial_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "fixation_cross" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trig_on_fix
    play_trigger_on_cross()
    # keep track of which components have finished
    fixation_crossComponents = [cross_white]
    for thisComponent in fixation_crossComponents:
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
    
    # --- Run Routine "fixation_cross" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_white* updates
        if cross_white.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            cross_white.frameNStart = frameN  # exact frame index
            cross_white.tStart = t  # local t and not account for scr refresh
            cross_white.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_white, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_white.started')
            cross_white.setAutoDraw(True)
        if cross_white.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_white.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                cross_white.tStop = t  # not accounting for scr refresh
                cross_white.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_white.stopped')
                cross_white.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation_cross" ---
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    key_resp_moving.keys = []
    key_resp_moving.rt = []
    _key_resp_moving_allKeys = []
    # Run 'Begin Routine' code from cross_manage
    cross_white.setAutoDraw(True)
    win.flip()
    # Run 'Begin Routine' code from sound_stim
    sound_stim_started_time = core.getTime()
    play_trigger_on_stim_start()
    play_stim(stim_series=stim, sound=msg!="REST")
    play_trigger_on_end()
    #run_stim(port=port, delay=delay, scale=scale, soundfiles=['./sound/SD1010.WAV','./sound/SD0050.WAV'], sound=msg!="REST")
    sound_stim_end_time = core.getTime()
    trials.addData('stim.start_time', sound_stim_started_time)
    trials.addData('stim.end_time', sound_stim_end_time)
    trials.addData('stim.delay', delay)
    trials.addData('stim.scale', scale)
    trials.addData('stim.ans', ans)
    trials.addData('stim.msg', msg)
    
    # keep track of which components have finished
    trialComponents = [cross_white_2, cross_colored, key_resp, key_resp_moving]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_white_2* updates
        if cross_white_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            cross_white_2.frameNStart = frameN  # exact frame index
            cross_white_2.tStart = t  # local t and not account for scr refresh
            cross_white_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_white_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_white_2.started')
            cross_white_2.setAutoDraw(True)
        
        # *cross_colored* updates
        if cross_colored.status == NOT_STARTED and tThisFlip >= 11-frameTolerance:
            # keep track of start time/frame for later
            cross_colored.frameNStart = frameN  # exact frame index
            cross_colored.tStart = t  # local t and not account for scr refresh
            cross_colored.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_colored, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_colored.started')
            cross_colored.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 11-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            play_trigger_on_ans_enabled()
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['b', 'n'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                play_trigger_on_ans()
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(ans)) or (key_resp.keys == ans):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *key_resp_moving* updates
        waitOnFlip = False
        if key_resp_moving.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_moving.frameNStart = frameN  # exact frame index
            key_resp_moving.tStart = t  # local t and not account for scr refresh
            key_resp_moving.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_moving, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_moving.started')
            key_resp_moving.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_moving.clock.reset)  # t=0 on next screen flip
        if key_resp_moving.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_moving.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_moving_allKeys.extend(theseKeys)
            if len(_key_resp_moving_allKeys):
                key_resp_moving.keys = [key.name for key in _key_resp_moving_allKeys]  # storing all keys
                key_resp_moving.rt = [key.rt for key in _key_resp_moving_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # check responses
    if key_resp_moving.keys in ['', [], None]:  # No response was made
        key_resp_moving.keys = None
    trials.addData('key_resp_moving.keys',key_resp_moving.keys)
    if key_resp_moving.keys != None:  # we had a response
        trials.addData('key_resp_moving.rt', key_resp_moving.rt)
    # Run 'End Routine' code from cross_manage
    core.wait(1)
    cross_white.setAutoDraw(False)
    win.flip()
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

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

# --- Prepare to start Routine "ending_message" ---
continueRoutine = True
routineForceEnded = False
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
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_norm_3* updates
    if text_norm_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_norm_3.frameNStart = frameN  # exact frame index
        text_norm_3.tStart = t  # local t and not account for scr refresh
        text_norm_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_norm_3, 'tStartRefresh')  # time at next scr refresh
        text_norm_3.setAutoDraw(True)
    
    # *key_instruct_3* updates
    waitOnFlip = False
    if key_instruct_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_instruct_3.frameNStart = frameN  # exact frame index
        key_instruct_3.tStart = t  # local t and not account for scr refresh
        key_instruct_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_instruct_3, 'tStartRefresh')  # time at next scr refresh
        key_instruct_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_instruct_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_instruct_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_instruct_3.status == STARTED and not waitOnFlip:
        theseKeys = key_instruct_3.getKeys(keyList=['space'], waitRelease=False)
        _key_instruct_3_allKeys.extend(theseKeys)
        if len(_key_instruct_3_allKeys):
            key_instruct_3.keys = _key_instruct_3_allKeys[-1].name  # just the last key pressed
            key_instruct_3.rt = _key_instruct_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
# the Routine "ending_message" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Run 'End Experiment' code from init_modules
# Close the serial port
port.write([0])
port.close()

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
