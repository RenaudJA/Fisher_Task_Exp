#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on décembre 13, 2022, at 10:53
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'fisher_task'  # from the Builder filename that created this script
expInfo = {
    'participant_id': '1',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant_id'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\NextCloud\\1-Recherche\\04-PSYCHOPY\\Renaud\\2022\\FisherTask\\FisherTask2022_NwVers\\Fisher Task Finale\\Fisher Task PPyV2FR\\fisher_task_FR_lastrun.py',
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
    size=[1920, 1200], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
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

# --- Initialize components for Routine "Variable" ---
# Run 'Begin Experiment' code from Variables
basket_size = 0.0035
lake_size = 0.7

left_lakeX = -0.25
left_lakeY = 0.25
right_lakeX = 0.25
right_lakeY = 0.25

left_basketX = -0.25
left_basketY = 0.25
right_basketX = 0.25
right_basketY = 0.25

widthBasketLeft = 0.1
heightBasketLeft = 0.1
widthBasketRight = 0.1
heightBasketRight = 0.1

colorScale = [-1,-1,-1]

instrRightPos = (0.31, -0.365)
instrLeftPos = (-0.31, -0.365)

sureRightPos = (0.31, -0.43)
sureLeftPos = (-0.31, -0.43)

# --- Initialize components for Routine "instructions1" ---
# Run 'Begin Experiment' code from setNspaces
nspaces = -1
helloText = visual.TextStim(win=win, name='helloText',
    text="Bonjour\nMerci d'avoir accepté de participer à cette expérience.\n\nNous allons bientôt démarrer.",
    font='Arial',
    pos=(0, 0.1), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
fullscreen = visual.TextStim(win=win, name='fullscreen',
    text='Merci de ne pas presser la touche Esc, cela vous ferait sortir du mode plein-écran.\nSi vous le faisiez par erreur, vous pouvez tenter de revenir en mode plein-écran en appuyant sur F11 (sous Windows).',
    font='Arial',
    pos=(0, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
spaceText1 = visual.TextStim(win=win, name='spaceText1',
    text='Appuyez sur la barre espace pour continuer',
    font='Arial',
    pos=(0, -0.46), height=0.03, wrapWidth=None, ori=0, 
    color=[-0.05, -0.05, -0.05], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
inEachTrial = visual.TextStim(win=win, name='inEachTrial',
    text="Dans cette expérience, vous allez devoir déterminer, à chaque essai, de quel lac provient le poisson rouge.\n\nVoilà le poisson que vient d'attraper le pêcheur.",
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
fisherman1 = visual.ImageStim(
    win=win,
    name='fisherman1', 
    image='stimuli/hum.png', mask=None, anchor='center',
    ori=0, pos=(0, -0.15), size=(0.26, 0.39),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
whichLake = visual.TextStim(win=win, name='whichLake',
    text='Mais duquel de ces deux lacs vient ce poisson ?',
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
lake1 = visual.ImageStim(
    win=win,
    name='lake1', 
    image='stimuli/lake.jpg', mask=None, anchor='center',
    ori=0, pos=(-0.23, 0.00), size=(0.3275, 0.3275),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-8.0)
lake2 = visual.ImageStim(
    win=win,
    name='lake2', 
    image='stimuli/lake.jpg', mask=None, anchor='center',
    ori=0, pos=(0.23, 0.0), size=(0.3275, 0.3275),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-9.0)
twoInformation = visual.TextStim(win=win, name='twoInformation',
    text="Pour répondre, vous allez devoir combiner deux types d'information.",
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
preference = visual.TextStim(win=win, name='preference',
    text='1) Le temps que le pêcheur a passé à pêcher sur le lac de droite ou de gauche.',
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
example = visual.TextStim(win=win, name='example',
    text='Par exemple',
    font='Arial',
    pos=(0, 1), height=0.042, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
basket1 = visual.ImageStim(
    win=win,
    name='basket1', 
    image='stimuli/basket.png', mask=None, anchor='center',
    ori=0, pos=(-0.23, 0), size=(0.349027907, 0.282842712),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
basket2 = visual.ImageStim(
    win=win,
    name='basket2', 
    image='stimuli/basket.png', mask=None, anchor='center',
    ori=0, pos=(0.23, 0), size=(0.174513954, 0.141421356),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
preferenceExplanation = visual.TextStim(win=win, name='preferenceExplanation',
    text='Un plus grand panier de pêcheur à gauche indique que le pêcheur y a passé plus de temps que sur le lac de droite.',
    font='Arial',
    pos=(0, 1), height=0.042, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
proportions = visual.TextStim(win=win, name='proportions',
    text='2) La quantité de poissons rouges et noirs dans chaque lac.',
    font='Arial',
    pos=(1, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
lakeMore = visual.ImageStim(
    win=win,
    name='lakeMore', 
    image='stimuli/lake_more.jpg', mask=None, anchor='center',
    ori=0, pos=(-0.23, 0), size=(0.3275, 0.3275),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-17.0)
lakeLess = visual.ImageStim(
    win=win,
    name='lakeLess', 
    image='stimuli/lake_less.jpg', mask=None, anchor='center',
    ori=0, pos=(0.25, 0), size=(0.3275, 0.3275),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-18.0)
proportionsExplanation = visual.TextStim(win=win, name='proportionsExplanation',
    text='Ici, il y a un peu plus de poissons rouges dans le lac de gauche.',
    font='Arial',
    pos=(0, 1), height=0.042, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
upToYou = visual.TextStim(win=win, name='upToYou',
    text='En tenant compte de ces informations, à quel point êtes-vous certain que le poisson rouge vienne du lac de gauche ou du lac de droite ?',
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
# Run 'Begin Experiment' code from mouseAtStart
mouse_2.setPos([0,-0.5])

# --- Initialize components for Routine "instructions2" ---
howToAnswer = visual.TextStim(win=win, name='howToAnswer',
    text='Pour répondre, vous utiliserez la souris pour cliquer sur une échelle semi-circulaire.\n\nVous devrez être le plus rapide et précis possible.',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instrScale = visual.ImageStim(
    win=win,
    name='instrScale', 
    image='stimuli/scale.png', mask=None, anchor='center',
    ori=0, pos=(0, -0.26), size=(0.4, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
cursor = visual.ImageStim(
    win=win,
    name='cursor', 
    image='stimuli/cursor.png', mask=None, anchor='center',
    ori=0, pos=(-0.01, -0.4), size=(0.043, 0.09),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
instrSureRight = visual.TextStim(win=win, name='instrSureRight',
    text='Je suis certain\nLAC DE DROITE',
    font='Arial',
    pos=instrRightPos, height=0.03, wrapWidth=None, ori=0, 
    color=colorScale, colorSpace='rgb', opacity=1, 
    languageStyle='RTL',
    depth=-4.0);
instrSureLeft = visual.TextStim(win=win, name='instrSureLeft',
    text='Je suis certain\nLAC DE GAUCHE',
    font='Arial',
    pos=instrLeftPos, height=0.03, wrapWidth=None, ori=0, 
    color=colorScale, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
instrKnow = visual.TextStim(win=win, name='instrKnow',
    text='Je ne sais pas',
    font='Arial',
    pos=(0, -0.125), height=0.03, wrapWidth=None, ori=0, 
    color=colorScale, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
uncertain = visual.TextStim(win=win, name='uncertain',
    text='Par exemple, si vous n\'avez aucun indice, vous pouvez cliquer sur "Je ne sais pas".',
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
answerRight = visual.TextStim(win=win, name='answerRight',
    text='Si vous êtes sûr que le poisson a été pêché dans le lac de droite, vous pouvez répondre\n"Je suis certain LAC DE DROITE".',
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
answerLeft = visual.TextStim(win=win, name='answerLeft',
    text='Si vous êtes sûr que le poisson a été pêché dans le lac de gauche, vous pouvez répondre\n"Je suis certain LAC DE GAUCHE".',
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
somewhatRight = visual.TextStim(win=win, name='somewhatRight',
    text='Maintenant, si vous pensez que le poisson vient du lac de droite mais que des doutes persistent, vous pouvez répondre comme ceci:',
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
somewhatLeft = visual.TextStim(win=win, name='somewhatLeft',
    text='De la même manière, si vous pensez que le poisson vient du lac de gauche mais que des doutes persistent, vous pouvez répondre comme ceci:',
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
newExample = visual.TextStim(win=win, name='newExample',
    text='Prenons un autre exemple.\n\nSi le pêcheur passe plus de temps sur le lac de gauche, comme indiqué ici',
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
basket3 = visual.ImageStim(
    win=win,
    name='basket3', 
    image='stimuli/basket.png', mask=None, anchor='center',
    ori=0, pos=(-0.23, -0.05), size=(0.349027907, 0.282842712),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
basket4 = visual.ImageStim(
    win=win,
    name='basket4', 
    image='stimuli/basket.png', mask=None, anchor='center',
    ori=0, pos=(0.23, -0.05), size=(0.174513954, 0.141421356),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
asManyFish = visual.TextStim(win=win, name='asManyFish',
    text="... et qu'il y a autant de poissons rouges et noirs dans le lac de droite que dans le lac de gauche",
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
lake501 = visual.ImageStim(
    win=win,
    name='lake501', 
    image='stimuli/lake501.jpg', mask=None, anchor='center',
    ori=0, pos=(-0.23, 0), size=(0.3275, 0.3275),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-17.0)
lake502 = visual.ImageStim(
    win=win,
    name='lake502', 
    image='stimuli/lake502.jpg', mask=None, anchor='center',
    ori=0, pos=(0.25, 0), size=(0.3275, 0.3275),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-18.0)
whatConfidence = visual.TextStim(win=win, name='whatConfidence',
    text="Quelle est votre degré de certitude sur l'origine du poisson rouge fraîchement pêché ?",
    font='Arial',
    pos=(0, 1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
fisherman2 = visual.ImageStim(
    win=win,
    name='fisherman2', 
    image='stimuli/hum.png', mask=None, anchor='center',
    ori=0, pos=(0, 0.12), size=(0.22, 0.33),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
spaceText2 = visual.TextStim(win=win, name='spaceText2',
    text='Appuyez sur la barre espace pour continuer',
    font='Arial',
    pos=(0, -0.46), height=0.03, wrapWidth=None, ori=0, 
    color=[-0.05, -0.05, -0.05], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
leftArrow = visual.ImageStim(
    win=win,
    name='leftArrow', 
    image='stimuli/left_arrow.png', mask=None, anchor='center',
    ori=0, pos=(-0.185, -0.225), size=(0.1452, 0.1914),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
rightArrow = visual.ImageStim(
    win=win,
    name='rightArrow', 
    image='stimuli/right_arrow.png', mask=None, anchor='center',
    ori=0, pos=(0.18, -0.23), size=(0.144, 0.18),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
wholeScale = visual.TextStim(win=win, name='wholeScale',
    text="Utilisez bien toute\n l'échelle !",
    font='Arial',
    pos=(0, 1), height=0.035, wrapWidth=None, ori=0, 
    color=[0.5, -1, -1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
box = visual.ImageStim(
    win=win,
    name='box', 
    image='stimuli/box.png', mask=None, anchor='center',
    ori=0, pos=(-0.1265, -0.2565), size=(0.125, 0.105),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
wellDone = visual.TextStim(win=win, name='wellDone',
    text='Bravo !',
    font='Arial',
    pos=(0, 1), height=0.03, wrapWidth=None, ori=0, 
    color=[0.5, -1, -1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);

# --- Initialize components for Routine "instructionsRepeat" ---
repeatLoop = visual.TextStim(win=win, name='repeatLoop',
    text="Si vous avez compris les consignes de l'expérience, cliquez avec votre souris pour démarrer la phase d'entraînement.\n\nSinon, appuyez sur la barre espace pour lire les consignes une nouvelle fois.",
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keySpace = keyboard.Keyboard()

# --- Initialize components for Routine "TrainingInstruction" ---
TrainingInstrTxt = visual.TextStim(win=win, name='TrainingInstrTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='Appuyez sur la barre espace pour continuer',
    font='Arial',
    pos=(0,-0.46), height=0.03, wrapWidth=None, ori=0.0, 
    color=[-0.05, -0.05, -0.05], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "baskets" ---
basketLeft = visual.ImageStim(
    win=win,
    name='basketLeft', 
    image='stimuli/basket.png', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
basketRight = visual.ImageStim(
    win=win,
    name='basketRight', 
    image='stimuli/basket.png', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
cross_2 = visual.TextStim(win=win, name='cross_2',
    text='+',
    font='Times New Roman',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "choice_train" ---
left_lake = visual.ImageStim(
    win=win,
    name='left_lake', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
right_lake = visual.ImageStim(
    win=win,
    name='right_lake', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
fisherman = visual.ImageStim(
    win=win,
    name='fisherman', 
    image='stimuli/hum.png', mask=None, anchor='center',
    ori=0, pos=(0, 0.00), size=(0.20, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
scale = visual.ImageStim(
    win=win,
    name='scale', 
    image='stimuli/scale.png', mask=None, anchor='center',
    ori=0, pos=(0.0, -0.325), size=(0.4, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
sureRight = visual.TextStim(win=win, name='sureRight',
    text='Je suis certain\nLAC DE DROITE',
    font='Arial',
    pos=sureRightPos, height=0.03, wrapWidth=None, ori=0, 
    color=colorScale, colorSpace='rgb', opacity=1, 
    languageStyle='RTL',
    depth=-5.0);
sureLeft = visual.TextStim(win=win, name='sureLeft',
    text='Je suis certain\nLAC DE GAUCHE',
    font='Arial',
    pos=sureLeftPos, height=0.03, wrapWidth=None, ori=0, 
    color=colorScale, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
dontKnow = visual.TextStim(win=win, name='dontKnow',
    text='Je ne sais pas',
    font='Arial',
    pos=(0, -0.19), height=0.03, wrapWidth=None, ori=0, 
    color=colorScale, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "toExperiment" ---
trainingText = visual.TextStim(win=win, name='trainingText',
    text="L'entraînement est terminé.\n\nAppuyez sur la barre espace lorsque vous êtes prêt à démarrer l'expérience.",
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space2 = keyboard.Keyboard()
fullscreen2 = visual.TextStim(win=win, name='fullscreen2',
    text='Rappel: merci de ne pas presser la touche Esc.\nSi vous le faisiez par erreur, utilisez F11 pour revenir en mode plein-écran (sous Windows).',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
wholeScaleReminder = visual.TextStim(win=win, name='wholeScaleReminder',
    text="Souvenez vous de bien utiliser toute l'échelle pour répondre !",
    font='Arial',
    pos=(0, -0.12), height=0.05, wrapWidth=None, ori=0, 
    color=[0.5, -1, -1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "breakscreen" ---
breakText = visual.TextStim(win=win, name='breakText',
    text='',
    font='Arial',
    pos=(0, 0.05), height=0.055, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
space1 = keyboard.Keyboard()
fullscreen3 = visual.TextStim(win=win, name='fullscreen3',
    text='Rappel: merci de ne pas presser la touche Esc.\nSi vous le faisiez par erreur, utilisez F11 pour revenir en mode plein-écran (sous Windows).',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "baskets" ---
basketLeft = visual.ImageStim(
    win=win,
    name='basketLeft', 
    image='stimuli/basket.png', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
basketRight = visual.ImageStim(
    win=win,
    name='basketRight', 
    image='stimuli/basket.png', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
cross_2 = visual.TextStim(win=win, name='cross_2',
    text='+',
    font='Times New Roman',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "choice_train" ---
left_lake = visual.ImageStim(
    win=win,
    name='left_lake', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
right_lake = visual.ImageStim(
    win=win,
    name='right_lake', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
fisherman = visual.ImageStim(
    win=win,
    name='fisherman', 
    image='stimuli/hum.png', mask=None, anchor='center',
    ori=0, pos=(0, 0.00), size=(0.20, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
scale = visual.ImageStim(
    win=win,
    name='scale', 
    image='stimuli/scale.png', mask=None, anchor='center',
    ori=0, pos=(0.0, -0.325), size=(0.4, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
sureRight = visual.TextStim(win=win, name='sureRight',
    text='Je suis certain\nLAC DE DROITE',
    font='Arial',
    pos=sureRightPos, height=0.03, wrapWidth=None, ori=0, 
    color=colorScale, colorSpace='rgb', opacity=1, 
    languageStyle='RTL',
    depth=-5.0);
sureLeft = visual.TextStim(win=win, name='sureLeft',
    text='Je suis certain\nLAC DE GAUCHE',
    font='Arial',
    pos=sureLeftPos, height=0.03, wrapWidth=None, ori=0, 
    color=colorScale, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
dontKnow = visual.TextStim(win=win, name='dontKnow',
    text='Je ne sais pas',
    font='Arial',
    pos=(0, -0.19), height=0.03, wrapWidth=None, ori=0, 
    color=colorScale, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "finalScreen" ---
finalText1 = visual.TextStim(win=win, name='finalText1',
    text="L'expérience est terminée.\nMerci de votre participation.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finalSpace1 = keyboard.Keyboard()
spaceFinal1 = visual.TextStim(win=win, name='spaceFinal1',
    text='Appuyez sur la barre espace pour sortir',
    font='Arial',
    pos=(0, -0.46), height=0.03, wrapWidth=None, ori=0, 
    color=[-0.05, -0.05, -0.05], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Variable" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
VariableComponents = []
for thisComponent in VariableComponents:
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

# --- Run Routine "Variable" ---
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
    for thisComponent in VariableComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Variable" ---
for thisComponent in VariableComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Variable" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instructions = data.TrialHandler(nReps=100, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instructions')
thisExp.addLoop(instructions)  # add the loop to the experiment
thisInstruction = instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
if thisInstruction != None:
    for paramName in thisInstruction:
        exec('{} = thisInstruction[paramName]'.format(paramName))

for thisInstruction in instructions:
    currentLoop = instructions
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
    if thisInstruction != None:
        for paramName in thisInstruction:
            exec('{} = thisInstruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instructions1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructions1Components = [helloText, fullscreen, spaceText1, inEachTrial, fisherman1, whichLake, lake1, lake2, twoInformation, preference, example, basket1, basket2, preferenceExplanation, proportions, lakeMore, lakeLess, proportionsExplanation, upToYou, mouse_2]
    for thisComponent in instructions1Components:
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
    
    # --- Run Routine "instructions1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *helloText* updates
        if helloText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            helloText.frameNStart = frameN  # exact frame index
            helloText.tStart = t  # local t and not account for scr refresh
            helloText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(helloText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'helloText.started')
            helloText.setAutoDraw(True)
        
        # *fullscreen* updates
        if fullscreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fullscreen.frameNStart = frameN  # exact frame index
            fullscreen.tStart = t  # local t and not account for scr refresh
            fullscreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fullscreen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fullscreen.started')
            fullscreen.setAutoDraw(True)
        
        # *spaceText1* updates
        if spaceText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            spaceText1.frameNStart = frameN  # exact frame index
            spaceText1.tStart = t  # local t and not account for scr refresh
            spaceText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(spaceText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'spaceText1.started')
            spaceText1.setAutoDraw(True)
        
        # *inEachTrial* updates
        if inEachTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inEachTrial.frameNStart = frameN  # exact frame index
            inEachTrial.tStart = t  # local t and not account for scr refresh
            inEachTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inEachTrial, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'inEachTrial.started')
            inEachTrial.setAutoDraw(True)
        
        # *fisherman1* updates
        if fisherman1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fisherman1.frameNStart = frameN  # exact frame index
            fisherman1.tStart = t  # local t and not account for scr refresh
            fisherman1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fisherman1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fisherman1.started')
            fisherman1.setAutoDraw(True)
        
        # *whichLake* updates
        if whichLake.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            whichLake.frameNStart = frameN  # exact frame index
            whichLake.tStart = t  # local t and not account for scr refresh
            whichLake.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whichLake, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'whichLake.started')
            whichLake.setAutoDraw(True)
        
        # *lake1* updates
        if lake1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lake1.frameNStart = frameN  # exact frame index
            lake1.tStart = t  # local t and not account for scr refresh
            lake1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lake1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lake1.started')
            lake1.setAutoDraw(True)
        
        # *lake2* updates
        if lake2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lake2.frameNStart = frameN  # exact frame index
            lake2.tStart = t  # local t and not account for scr refresh
            lake2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lake2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lake2.started')
            lake2.setAutoDraw(True)
        
        # *twoInformation* updates
        if twoInformation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            twoInformation.frameNStart = frameN  # exact frame index
            twoInformation.tStart = t  # local t and not account for scr refresh
            twoInformation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(twoInformation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'twoInformation.started')
            twoInformation.setAutoDraw(True)
        
        # *preference* updates
        if preference.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            preference.frameNStart = frameN  # exact frame index
            preference.tStart = t  # local t and not account for scr refresh
            preference.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(preference, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'preference.started')
            preference.setAutoDraw(True)
        
        # *example* updates
        if example.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            example.frameNStart = frameN  # exact frame index
            example.tStart = t  # local t and not account for scr refresh
            example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(example, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'example.started')
            example.setAutoDraw(True)
        
        # *basket1* updates
        if basket1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            basket1.frameNStart = frameN  # exact frame index
            basket1.tStart = t  # local t and not account for scr refresh
            basket1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(basket1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'basket1.started')
            basket1.setAutoDraw(True)
        
        # *basket2* updates
        if basket2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            basket2.frameNStart = frameN  # exact frame index
            basket2.tStart = t  # local t and not account for scr refresh
            basket2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(basket2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'basket2.started')
            basket2.setAutoDraw(True)
        
        # *preferenceExplanation* updates
        if preferenceExplanation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            preferenceExplanation.frameNStart = frameN  # exact frame index
            preferenceExplanation.tStart = t  # local t and not account for scr refresh
            preferenceExplanation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(preferenceExplanation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'preferenceExplanation.started')
            preferenceExplanation.setAutoDraw(True)
        
        # *proportions* updates
        if proportions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proportions.frameNStart = frameN  # exact frame index
            proportions.tStart = t  # local t and not account for scr refresh
            proportions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proportions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'proportions.started')
            proportions.setAutoDraw(True)
        
        # *lakeMore* updates
        if lakeMore.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lakeMore.frameNStart = frameN  # exact frame index
            lakeMore.tStart = t  # local t and not account for scr refresh
            lakeMore.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lakeMore, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lakeMore.started')
            lakeMore.setAutoDraw(True)
        
        # *lakeLess* updates
        if lakeLess.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lakeLess.frameNStart = frameN  # exact frame index
            lakeLess.tStart = t  # local t and not account for scr refresh
            lakeLess.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lakeLess, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lakeLess.started')
            lakeLess.setAutoDraw(True)
        
        # *proportionsExplanation* updates
        if proportionsExplanation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proportionsExplanation.frameNStart = frameN  # exact frame index
            proportionsExplanation.tStart = t  # local t and not account for scr refresh
            proportionsExplanation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proportionsExplanation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'proportionsExplanation.started')
            proportionsExplanation.setAutoDraw(True)
        
        # *upToYou* updates
        if upToYou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upToYou.frameNStart = frameN  # exact frame index
            upToYou.tStart = t  # local t and not account for scr refresh
            upToYou.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upToYou, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'upToYou.started')
            upToYou.setAutoDraw(True)
        # Run 'Each Frame' code from spaceEffects1
        if event.getKeys('space'):
            nspaces = nspaces + 1
            if nspaces == 0:
                helloText.pos = (0, 1)
                fullscreen.pos = (0, 1)
                inEachTrial.pos = (0, 0.25)
                fisherman1.opacity = 1
            if nspaces == 1:
                inEachTrial.pos = (0, 1)
                fisherman1.opacity = 0
                whichLake.pos = (0, 0.35)
                lake1.opacity = 1
                lake2.opacity = 1
                twoInformation.pos = (0, -0.25)
            if nspaces == 2:
                whichLake.pos = (0, 1)
                lake1.opacity = 0
                lake2.opacity = 0
                twoInformation.pos = (0, 1)
                preference.pos = (0, 0.35)
                example.pos = (0, 0.25)
                basket1.opacity = 1
                basket2.opacity = 1
                preferenceExplanation.pos = (0, -0.3)
            if nspaces == 3:
                preference.pos = (0, 1)
                basket1.opacity = 0
                basket2.opacity = 0
                preferenceExplanation.pos = (0, 1)
                proportions.pos = (0, 0.35)
                lakeMore.opacity = 1
                lakeLess.opacity = 1
                proportionsExplanation.pos = (0, -0.3)
            if nspaces == 4:
                proportions.pos = (0, 1)
                example.pos = (0, 1)
                lakeMore.opacity = 0
                lakeLess.opacity = 0
                proportionsExplanation.pos = (0, 1)
                upToYou.pos = (0, 0.3)
                fisherman1.opacity = 1
            if nspaces == 5:
                upToYou.pos = (0, 1)
                fisherman1.opacity = 0
                helloText.pos = (0, 0.1)
                fullscreen.pos = (0, -0.25)
                continueRoutine = False
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_2.started', t)
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
                    
                    continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions1" ---
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for instructions (TrialHandler)
    instructions.addData('mouse_2.x', mouse_2.x)
    instructions.addData('mouse_2.y', mouse_2.y)
    instructions.addData('mouse_2.leftButton', mouse_2.leftButton)
    instructions.addData('mouse_2.midButton', mouse_2.midButton)
    instructions.addData('mouse_2.rightButton', mouse_2.rightButton)
    instructions.addData('mouse_2.time', mouse_2.time)
    # the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    instructions2Components = [howToAnswer, instrScale, cursor, instrSureRight, instrSureLeft, instrKnow, uncertain, answerRight, answerLeft, somewhatRight, somewhatLeft, newExample, basket3, basket4, asManyFish, lake501, lake502, whatConfidence, fisherman2, spaceText2, leftArrow, rightArrow, wholeScale, box, wellDone]
    for thisComponent in instructions2Components:
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
    
    # --- Run Routine "instructions2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *howToAnswer* updates
        if howToAnswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            howToAnswer.frameNStart = frameN  # exact frame index
            howToAnswer.tStart = t  # local t and not account for scr refresh
            howToAnswer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(howToAnswer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'howToAnswer.started')
            howToAnswer.setAutoDraw(True)
        
        # *instrScale* updates
        if instrScale.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instrScale.frameNStart = frameN  # exact frame index
            instrScale.tStart = t  # local t and not account for scr refresh
            instrScale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrScale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrScale.started')
            instrScale.setAutoDraw(True)
        
        # *cursor* updates
        if cursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cursor.frameNStart = frameN  # exact frame index
            cursor.tStart = t  # local t and not account for scr refresh
            cursor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cursor, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cursor.started')
            cursor.setAutoDraw(True)
        
        # *instrSureRight* updates
        if instrSureRight.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instrSureRight.frameNStart = frameN  # exact frame index
            instrSureRight.tStart = t  # local t and not account for scr refresh
            instrSureRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrSureRight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrSureRight.started')
            instrSureRight.setAutoDraw(True)
        
        # *instrSureLeft* updates
        if instrSureLeft.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instrSureLeft.frameNStart = frameN  # exact frame index
            instrSureLeft.tStart = t  # local t and not account for scr refresh
            instrSureLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrSureLeft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrSureLeft.started')
            instrSureLeft.setAutoDraw(True)
        
        # *instrKnow* updates
        if instrKnow.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instrKnow.frameNStart = frameN  # exact frame index
            instrKnow.tStart = t  # local t and not account for scr refresh
            instrKnow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrKnow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrKnow.started')
            instrKnow.setAutoDraw(True)
        
        # *uncertain* updates
        if uncertain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            uncertain.frameNStart = frameN  # exact frame index
            uncertain.tStart = t  # local t and not account for scr refresh
            uncertain.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(uncertain, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'uncertain.started')
            uncertain.setAutoDraw(True)
        
        # *answerRight* updates
        if answerRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answerRight.frameNStart = frameN  # exact frame index
            answerRight.tStart = t  # local t and not account for scr refresh
            answerRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answerRight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'answerRight.started')
            answerRight.setAutoDraw(True)
        
        # *answerLeft* updates
        if answerLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answerLeft.frameNStart = frameN  # exact frame index
            answerLeft.tStart = t  # local t and not account for scr refresh
            answerLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answerLeft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'answerLeft.started')
            answerLeft.setAutoDraw(True)
        
        # *somewhatRight* updates
        if somewhatRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            somewhatRight.frameNStart = frameN  # exact frame index
            somewhatRight.tStart = t  # local t and not account for scr refresh
            somewhatRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(somewhatRight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'somewhatRight.started')
            somewhatRight.setAutoDraw(True)
        
        # *somewhatLeft* updates
        if somewhatLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            somewhatLeft.frameNStart = frameN  # exact frame index
            somewhatLeft.tStart = t  # local t and not account for scr refresh
            somewhatLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(somewhatLeft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'somewhatLeft.started')
            somewhatLeft.setAutoDraw(True)
        # Run 'Each Frame' code from spaceEffects2
        if event.getKeys('space'):
            nspaces = nspaces + 1
            if nspaces == 6:
                howToAnswer.pos = (0, 1)
                uncertain.pos = (0, 0.2)
                cursor.pos = (-0.01, -0.2)
            if nspaces == 7:
                uncertain.pos = (0, 1)
                answerRight.pos = (0, 0.2)
                cursor.pos = (0.15, -0.365)
            if nspaces == 8:
                answerRight.pos = (0, 1)
                answerLeft.pos = (0, 0.2)
                cursor.pos = (-0.17, -0.365)
            if nspaces == 9:
                answerLeft.pos = (0, 1)
                somewhatRight.pos = (0, 0.2)
                rightArrow.opacity = 1
                wholeScale.pos = (0.39, -0.185)
                cursor.pos = (0.12, -0.28)
            if nspaces == 10:
                somewhatRight.pos = (0, 1)
                rightArrow.opacity = 0
                leftArrow.opacity = 1
                wholeScale.pos = (-0.4, -0.185)
                somewhatLeft.pos = (0, 0.2)
                cursor.pos = (-0.14, -0.28)
            if nspaces == 11:
                leftArrow.opacity = 0
                somewhatLeft.pos = (0, 1)
                cursor.pos = (-0.01, -0.4)
                cursor.opacity = 0
                instrScale.opacity = 0
                instrKnow.pos = (0, 1)
                instrSureLeft.pos = (0, 1)
                instrSureRight.pos = (0, 1)
                wholeScale.pos = (0, 1)
                newExample.pos = (0, 0.3)
                basket3.opacity = 1
                basket4.opacity = 1
            if nspaces == 12:
                newExample.pos = (0, 1)
                basket3.opacity = 0
                basket4.opacity = 0
                asManyFish.pos = (0, 0.3)
                lake501.opacity = 1
                lake502.opacity = 1
            if nspaces == 13:
                asManyFish.pos = (0, 1)
                lake501.opacity = 0
                lake502.opacity = 0
                whatConfidence.pos = (0, 0.4)
                fisherman2.opacity = 1
                instrScale.opacity = 1
                instrKnow.pos = (0, -0.125)
                cursor.opacity = 1
                instrSureRight.pos = instrRightPos
                instrSureLeft.pos  = instrLeftPos
            if nspaces == 14:
                box.opacity = 1
                wellDone.pos = (-0.25, -0.235)
            if nspaces == 15:
                wellDone.pos = (0, 1)
                box.opacity = 0
                howToAnswer.pos = (0, 0.2)
                whatConfidence.pos = (0, 1)
                fisherman2.opacity = 0
                nspaces = -2
                continueRoutine = False
        
        # *newExample* updates
        if newExample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            newExample.frameNStart = frameN  # exact frame index
            newExample.tStart = t  # local t and not account for scr refresh
            newExample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(newExample, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'newExample.started')
            newExample.setAutoDraw(True)
        
        # *basket3* updates
        if basket3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            basket3.frameNStart = frameN  # exact frame index
            basket3.tStart = t  # local t and not account for scr refresh
            basket3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(basket3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'basket3.started')
            basket3.setAutoDraw(True)
        
        # *basket4* updates
        if basket4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            basket4.frameNStart = frameN  # exact frame index
            basket4.tStart = t  # local t and not account for scr refresh
            basket4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(basket4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'basket4.started')
            basket4.setAutoDraw(True)
        
        # *asManyFish* updates
        if asManyFish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            asManyFish.frameNStart = frameN  # exact frame index
            asManyFish.tStart = t  # local t and not account for scr refresh
            asManyFish.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(asManyFish, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'asManyFish.started')
            asManyFish.setAutoDraw(True)
        
        # *lake501* updates
        if lake501.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lake501.frameNStart = frameN  # exact frame index
            lake501.tStart = t  # local t and not account for scr refresh
            lake501.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lake501, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lake501.started')
            lake501.setAutoDraw(True)
        
        # *lake502* updates
        if lake502.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lake502.frameNStart = frameN  # exact frame index
            lake502.tStart = t  # local t and not account for scr refresh
            lake502.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lake502, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lake502.started')
            lake502.setAutoDraw(True)
        
        # *whatConfidence* updates
        if whatConfidence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            whatConfidence.frameNStart = frameN  # exact frame index
            whatConfidence.tStart = t  # local t and not account for scr refresh
            whatConfidence.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whatConfidence, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'whatConfidence.started')
            whatConfidence.setAutoDraw(True)
        
        # *fisherman2* updates
        if fisherman2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fisherman2.frameNStart = frameN  # exact frame index
            fisherman2.tStart = t  # local t and not account for scr refresh
            fisherman2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fisherman2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fisherman2.started')
            fisherman2.setAutoDraw(True)
        
        # *spaceText2* updates
        if spaceText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            spaceText2.frameNStart = frameN  # exact frame index
            spaceText2.tStart = t  # local t and not account for scr refresh
            spaceText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(spaceText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'spaceText2.started')
            spaceText2.setAutoDraw(True)
        
        # *leftArrow* updates
        if leftArrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftArrow.frameNStart = frameN  # exact frame index
            leftArrow.tStart = t  # local t and not account for scr refresh
            leftArrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftArrow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'leftArrow.started')
            leftArrow.setAutoDraw(True)
        
        # *rightArrow* updates
        if rightArrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightArrow.frameNStart = frameN  # exact frame index
            rightArrow.tStart = t  # local t and not account for scr refresh
            rightArrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightArrow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rightArrow.started')
            rightArrow.setAutoDraw(True)
        
        # *wholeScale* updates
        if wholeScale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wholeScale.frameNStart = frameN  # exact frame index
            wholeScale.tStart = t  # local t and not account for scr refresh
            wholeScale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wholeScale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wholeScale.started')
            wholeScale.setAutoDraw(True)
        
        # *box* updates
        if box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box.frameNStart = frameN  # exact frame index
            box.tStart = t  # local t and not account for scr refresh
            box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'box.started')
            box.setAutoDraw(True)
        
        # *wellDone* updates
        if wellDone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wellDone.frameNStart = frameN  # exact frame index
            wellDone.tStart = t  # local t and not account for scr refresh
            wellDone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wellDone, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wellDone.started')
            wellDone.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions2" ---
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructionsRepeat" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    keySpace.keys = []
    keySpace.rt = []
    _keySpace_allKeys = []
    # keep track of which components have finished
    instructionsRepeatComponents = [repeatLoop, keySpace]
    for thisComponent in instructionsRepeatComponents:
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
    
    # --- Run Routine "instructionsRepeat" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from mouseProceed
        if (mouse.getPressed()[0] == 1 or mouse.getPressed()[1] == 1 or mouse.getPressed()[2] == 1):
            instructions.finished = True
            continueRoutine = False
        
        # *repeatLoop* updates
        if repeatLoop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            repeatLoop.frameNStart = frameN  # exact frame index
            repeatLoop.tStart = t  # local t and not account for scr refresh
            repeatLoop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeatLoop, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'repeatLoop.started')
            repeatLoop.setAutoDraw(True)
        
        # *keySpace* updates
        waitOnFlip = False
        if keySpace.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keySpace.frameNStart = frameN  # exact frame index
            keySpace.tStart = t  # local t and not account for scr refresh
            keySpace.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keySpace, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keySpace.started')
            keySpace.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keySpace.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keySpace.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keySpace.status == STARTED and not waitOnFlip:
            theseKeys = keySpace.getKeys(keyList=['space'], waitRelease=False)
            _keySpace_allKeys.extend(theseKeys)
            if len(_keySpace_allKeys):
                keySpace.keys = _keySpace_allKeys[-1].name  # just the last key pressed
                keySpace.rt = _keySpace_allKeys[-1].rt
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
        for thisComponent in instructionsRepeatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructionsRepeat" ---
    for thisComponent in instructionsRepeatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keySpace.keys in ['', [], None]:  # No response was made
        keySpace.keys = None
    instructions.addData('keySpace.keys',keySpace.keys)
    if keySpace.keys != None:  # we had a response
        instructions.addData('keySpace.rt', keySpace.rt)
    # the Routine "instructionsRepeat" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 100 repeats of 'instructions'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TrainingFiles/TrainingInstructions.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "TrainingInstruction" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    TrainingInstructionComponents = [TrainingInstrTxt, key_resp, text]
    for thisComponent in TrainingInstructionComponents:
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
    
    # --- Run Routine "TrainingInstruction" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TrainingInstrTxt* updates
        if TrainingInstrTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrainingInstrTxt.frameNStart = frameN  # exact frame index
            TrainingInstrTxt.tStart = t  # local t and not account for scr refresh
            TrainingInstrTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrainingInstrTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrainingInstrTxt.started')
            TrainingInstrTxt.setAutoDraw(True)
        if TrainingInstrTxt.status == STARTED:  # only update if drawing
            TrainingInstrTxt.setText(Consigne, log=False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrainingInstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TrainingInstruction" ---
    for thisComponent in TrainingInstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_3.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_3.addData('key_resp.rt', key_resp.rt)
    # the Routine "TrainingInstruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    training = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(TrainingFile),
        seed=None, name='training')
    thisExp.addLoop(training)  # add the loop to the experiment
    thisTraining = training.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining != None:
        for paramName in thisTraining:
            exec('{} = thisTraining[paramName]'.format(paramName))
    
    for thisTraining in training:
        currentLoop = training
        # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
        if thisTraining != None:
            for paramName in thisTraining:
                exec('{} = thisTraining[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "baskets" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        basketLeft.setPos((left_basketX, left_basketY))
        basketLeft.setSize((Basket_G*basket_size, Basket_G*basket_size*527/555))
        basketRight.setPos((right_basketX, right_basketY))
        basketRight.setSize((Basket_D*basket_size, Basket_D*basket_size*527/555))
        # keep track of which components have finished
        basketsComponents = [basketLeft, basketRight, cross_2]
        for thisComponent in basketsComponents:
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
        
        # --- Run Routine "baskets" ---
        while continueRoutine and routineTimer.getTime() < 1.8:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *basketLeft* updates
            if basketLeft.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                basketLeft.frameNStart = frameN  # exact frame index
                basketLeft.tStart = t  # local t and not account for scr refresh
                basketLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(basketLeft, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'basketLeft.started')
                basketLeft.setAutoDraw(True)
            if basketLeft.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > basketLeft.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    basketLeft.tStop = t  # not accounting for scr refresh
                    basketLeft.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'basketLeft.stopped')
                    basketLeft.setAutoDraw(False)
            
            # *basketRight* updates
            if basketRight.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                basketRight.frameNStart = frameN  # exact frame index
                basketRight.tStart = t  # local t and not account for scr refresh
                basketRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(basketRight, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'basketRight.started')
                basketRight.setAutoDraw(True)
            if basketRight.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > basketRight.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    basketRight.tStop = t  # not accounting for scr refresh
                    basketRight.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'basketRight.stopped')
                    basketRight.setAutoDraw(False)
            
            # *cross_2* updates
            if cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_2.frameNStart = frameN  # exact frame index
                cross_2.tStart = t  # local t and not account for scr refresh
                cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_2.started')
                cross_2.setAutoDraw(True)
            if cross_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_2.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_2.tStop = t  # not accounting for scr refresh
                    cross_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_2.stopped')
                    cross_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in basketsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "baskets" ---
        for thisComponent in basketsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.800000)
        
        # --- Prepare to start Routine "choice_train" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        left_lake.setPos((left_lakeX, left_lakeY))
        left_lake.setSize((0.450*lake_size, 0.450*lake_size))
        left_lake.setImage(Lake_pic_G)
        right_lake.setPos((right_lakeX, right_lakeY))
        right_lake.setSize((0.450*lake_size, 0.450*lake_size))
        right_lake.setImage(Lake_pic_D)
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from SetMousePos
        mouse.setPos([0,-0.42])
        # keep track of which components have finished
        choice_trainComponents = [left_lake, right_lake, fisherman, scale, mouse, sureRight, sureLeft, dontKnow]
        for thisComponent in choice_trainComponents:
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
        
        # --- Run Routine "choice_train" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *left_lake* updates
            if left_lake.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                left_lake.frameNStart = frameN  # exact frame index
                left_lake.tStart = t  # local t and not account for scr refresh
                left_lake.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_lake, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_lake.started')
                left_lake.setAutoDraw(True)
            
            # *right_lake* updates
            if right_lake.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                right_lake.frameNStart = frameN  # exact frame index
                right_lake.tStart = t  # local t and not account for scr refresh
                right_lake.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_lake, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_lake.started')
                right_lake.setAutoDraw(True)
            
            # *fisherman* updates
            if fisherman.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                fisherman.frameNStart = frameN  # exact frame index
                fisherman.tStart = t  # local t and not account for scr refresh
                fisherman.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fisherman, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fisherman.started')
                fisherman.setAutoDraw(True)
            
            # *scale* updates
            if scale.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                scale.frameNStart = frameN  # exact frame index
                scale.tStart = t  # local t and not account for scr refresh
                scale.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(scale, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'scale.started')
                scale.setAutoDraw(True)
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(scale)
                            clickableList = scale
                        except:
                            clickableList = [scale]
                        for obj in clickableList:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # abort routine on response
            
            # *sureRight* updates
            if sureRight.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                sureRight.frameNStart = frameN  # exact frame index
                sureRight.tStart = t  # local t and not account for scr refresh
                sureRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sureRight, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sureRight.started')
                sureRight.setAutoDraw(True)
            
            # *sureLeft* updates
            if sureLeft.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                sureLeft.frameNStart = frameN  # exact frame index
                sureLeft.tStart = t  # local t and not account for scr refresh
                sureLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sureLeft, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sureLeft.started')
                sureLeft.setAutoDraw(True)
            
            # *dontKnow* updates
            if dontKnow.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                dontKnow.frameNStart = frameN  # exact frame index
                dontKnow.tStart = t  # local t and not account for scr refresh
                dontKnow.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dontKnow, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dontKnow.started')
                dontKnow.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in choice_trainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "choice_train" ---
        for thisComponent in choice_trainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for training (TrialHandler)
        training.addData('mouse.x', mouse.x)
        training.addData('mouse.y', mouse.y)
        training.addData('mouse.leftButton', mouse.leftButton)
        training.addData('mouse.midButton', mouse.midButton)
        training.addData('mouse.rightButton', mouse.rightButton)
        training.addData('mouse.time', mouse.time)
        training.addData('mouse.clicked_name', mouse.clicked_name)
        # the Routine "choice_train" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'training'
    
    # get names of stimulus parameters
    if training.trialList in ([], [None], None):
        params = []
    else:
        params = training.trialList[0].keys()
    # save data for this loop
    training.saveAsExcel(filename + '.xlsx', sheetName='training',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "toExperiment" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space2.keys = []
space2.rt = []
_space2_allKeys = []
# keep track of which components have finished
toExperimentComponents = [trainingText, space2, fullscreen2, wholeScaleReminder]
for thisComponent in toExperimentComponents:
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

# --- Run Routine "toExperiment" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trainingText* updates
    if trainingText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trainingText.frameNStart = frameN  # exact frame index
        trainingText.tStart = t  # local t and not account for scr refresh
        trainingText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trainingText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trainingText.started')
        trainingText.setAutoDraw(True)
    
    # *space2* updates
    waitOnFlip = False
    if space2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space2.frameNStart = frameN  # exact frame index
        space2.tStart = t  # local t and not account for scr refresh
        space2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space2.started')
        space2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space2.status == STARTED and not waitOnFlip:
        theseKeys = space2.getKeys(keyList=['space'], waitRelease=False)
        _space2_allKeys.extend(theseKeys)
        if len(_space2_allKeys):
            space2.keys = _space2_allKeys[-1].name  # just the last key pressed
            space2.rt = _space2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *fullscreen2* updates
    if fullscreen2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fullscreen2.frameNStart = frameN  # exact frame index
        fullscreen2.tStart = t  # local t and not account for scr refresh
        fullscreen2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fullscreen2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fullscreen2.started')
        fullscreen2.setAutoDraw(True)
    
    # *wholeScaleReminder* updates
    if wholeScaleReminder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wholeScaleReminder.frameNStart = frameN  # exact frame index
        wholeScaleReminder.tStart = t  # local t and not account for scr refresh
        wholeScaleReminder.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wholeScaleReminder, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'wholeScaleReminder.started')
        wholeScaleReminder.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in toExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "toExperiment" ---
for thisComponent in toExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space2.keys in ['', [], None]:  # No response was made
    space2.keys = None
thisExp.addData('space2.keys',space2.keys)
if space2.keys != None:  # we had a response
    thisExp.addData('space2.rt', space2.rt)
thisExp.nextEntry()
# the Routine "toExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BlockFiles/BlockConditions.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "breakscreen" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from breakCode
    perc = str(round(trials_2.thisTrialN /8*100))
    breakText.setText('Vous pouvez faire une pause.\n\nVous avez réalisé ' + perc + '% de la tâche.\n\nAppuyez sur la barre espace lorsque vous êtes prêt à reprendre.')
    space1.keys = []
    space1.rt = []
    _space1_allKeys = []
    # keep track of which components have finished
    breakscreenComponents = [breakText, space1, fullscreen3]
    for thisComponent in breakscreenComponents:
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
    
    # --- Run Routine "breakscreen" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from breakCode
        if trials_2.thisTrialN < 1 :
            continueRoutine = False
        
        # *breakText* updates
        if breakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            breakText.frameNStart = frameN  # exact frame index
            breakText.tStart = t  # local t and not account for scr refresh
            breakText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(breakText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'breakText.started')
            breakText.setAutoDraw(True)
        
        # *space1* updates
        waitOnFlip = False
        if space1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space1.frameNStart = frameN  # exact frame index
            space1.tStart = t  # local t and not account for scr refresh
            space1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space1.started')
            space1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space1.status == STARTED and not waitOnFlip:
            theseKeys = space1.getKeys(keyList=['space'], waitRelease=False)
            _space1_allKeys.extend(theseKeys)
            if len(_space1_allKeys):
                space1.keys = _space1_allKeys[-1].name  # just the last key pressed
                space1.rt = _space1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fullscreen3* updates
        if fullscreen3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fullscreen3.frameNStart = frameN  # exact frame index
            fullscreen3.tStart = t  # local t and not account for scr refresh
            fullscreen3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fullscreen3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fullscreen3.started')
            fullscreen3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breakscreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "breakscreen" ---
    for thisComponent in breakscreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if space1.keys in ['', [], None]:  # No response was made
        space1.keys = None
    trials_2.addData('space1.keys',space1.keys)
    if space1.keys != None:  # we had a response
        trials_2.addData('space1.rt', space1.rt)
    # the Routine "breakscreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(Fichier),
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
        
        # --- Prepare to start Routine "baskets" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        basketLeft.setPos((left_basketX, left_basketY))
        basketLeft.setSize((Basket_G*basket_size, Basket_G*basket_size*527/555))
        basketRight.setPos((right_basketX, right_basketY))
        basketRight.setSize((Basket_D*basket_size, Basket_D*basket_size*527/555))
        # keep track of which components have finished
        basketsComponents = [basketLeft, basketRight, cross_2]
        for thisComponent in basketsComponents:
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
        
        # --- Run Routine "baskets" ---
        while continueRoutine and routineTimer.getTime() < 1.8:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *basketLeft* updates
            if basketLeft.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                basketLeft.frameNStart = frameN  # exact frame index
                basketLeft.tStart = t  # local t and not account for scr refresh
                basketLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(basketLeft, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'basketLeft.started')
                basketLeft.setAutoDraw(True)
            if basketLeft.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > basketLeft.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    basketLeft.tStop = t  # not accounting for scr refresh
                    basketLeft.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'basketLeft.stopped')
                    basketLeft.setAutoDraw(False)
            
            # *basketRight* updates
            if basketRight.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                basketRight.frameNStart = frameN  # exact frame index
                basketRight.tStart = t  # local t and not account for scr refresh
                basketRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(basketRight, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'basketRight.started')
                basketRight.setAutoDraw(True)
            if basketRight.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > basketRight.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    basketRight.tStop = t  # not accounting for scr refresh
                    basketRight.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'basketRight.stopped')
                    basketRight.setAutoDraw(False)
            
            # *cross_2* updates
            if cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_2.frameNStart = frameN  # exact frame index
                cross_2.tStart = t  # local t and not account for scr refresh
                cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_2.started')
                cross_2.setAutoDraw(True)
            if cross_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_2.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_2.tStop = t  # not accounting for scr refresh
                    cross_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_2.stopped')
                    cross_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in basketsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "baskets" ---
        for thisComponent in basketsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.800000)
        
        # --- Prepare to start Routine "choice_train" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        left_lake.setPos((left_lakeX, left_lakeY))
        left_lake.setSize((0.450*lake_size, 0.450*lake_size))
        left_lake.setImage(Lake_pic_G)
        right_lake.setPos((right_lakeX, right_lakeY))
        right_lake.setSize((0.450*lake_size, 0.450*lake_size))
        right_lake.setImage(Lake_pic_D)
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from SetMousePos
        mouse.setPos([0,-0.42])
        # keep track of which components have finished
        choice_trainComponents = [left_lake, right_lake, fisherman, scale, mouse, sureRight, sureLeft, dontKnow]
        for thisComponent in choice_trainComponents:
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
        
        # --- Run Routine "choice_train" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *left_lake* updates
            if left_lake.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                left_lake.frameNStart = frameN  # exact frame index
                left_lake.tStart = t  # local t and not account for scr refresh
                left_lake.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_lake, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_lake.started')
                left_lake.setAutoDraw(True)
            
            # *right_lake* updates
            if right_lake.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                right_lake.frameNStart = frameN  # exact frame index
                right_lake.tStart = t  # local t and not account for scr refresh
                right_lake.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_lake, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_lake.started')
                right_lake.setAutoDraw(True)
            
            # *fisherman* updates
            if fisherman.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                fisherman.frameNStart = frameN  # exact frame index
                fisherman.tStart = t  # local t and not account for scr refresh
                fisherman.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fisherman, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fisherman.started')
                fisherman.setAutoDraw(True)
            
            # *scale* updates
            if scale.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                scale.frameNStart = frameN  # exact frame index
                scale.tStart = t  # local t and not account for scr refresh
                scale.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(scale, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'scale.started')
                scale.setAutoDraw(True)
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(scale)
                            clickableList = scale
                        except:
                            clickableList = [scale]
                        for obj in clickableList:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # abort routine on response
            
            # *sureRight* updates
            if sureRight.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                sureRight.frameNStart = frameN  # exact frame index
                sureRight.tStart = t  # local t and not account for scr refresh
                sureRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sureRight, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sureRight.started')
                sureRight.setAutoDraw(True)
            
            # *sureLeft* updates
            if sureLeft.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                sureLeft.frameNStart = frameN  # exact frame index
                sureLeft.tStart = t  # local t and not account for scr refresh
                sureLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sureLeft, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sureLeft.started')
                sureLeft.setAutoDraw(True)
            
            # *dontKnow* updates
            if dontKnow.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                # keep track of start time/frame for later
                dontKnow.frameNStart = frameN  # exact frame index
                dontKnow.tStart = t  # local t and not account for scr refresh
                dontKnow.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dontKnow, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dontKnow.started')
                dontKnow.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in choice_trainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "choice_train" ---
        for thisComponent in choice_trainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials (TrialHandler)
        trials.addData('mouse.x', mouse.x)
        trials.addData('mouse.y', mouse.y)
        trials.addData('mouse.leftButton', mouse.leftButton)
        trials.addData('mouse.midButton', mouse.midButton)
        trials.addData('mouse.rightButton', mouse.rightButton)
        trials.addData('mouse.time', mouse.time)
        trials.addData('mouse.clicked_name', mouse.clicked_name)
        # the Routine "choice_train" was not non-slip safe, so reset the non-slip timer
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
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "finalScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
finalSpace1.keys = []
finalSpace1.rt = []
_finalSpace1_allKeys = []
# keep track of which components have finished
finalScreenComponents = [finalText1, finalSpace1, spaceFinal1]
for thisComponent in finalScreenComponents:
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

# --- Run Routine "finalScreen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finalText1* updates
    if finalText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalText1.frameNStart = frameN  # exact frame index
        finalText1.tStart = t  # local t and not account for scr refresh
        finalText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalText1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'finalText1.started')
        finalText1.setAutoDraw(True)
    
    # *finalSpace1* updates
    waitOnFlip = False
    if finalSpace1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalSpace1.frameNStart = frameN  # exact frame index
        finalSpace1.tStart = t  # local t and not account for scr refresh
        finalSpace1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalSpace1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'finalSpace1.started')
        finalSpace1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(finalSpace1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(finalSpace1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if finalSpace1.status == STARTED and not waitOnFlip:
        theseKeys = finalSpace1.getKeys(keyList=['space'], waitRelease=False)
        _finalSpace1_allKeys.extend(theseKeys)
        if len(_finalSpace1_allKeys):
            finalSpace1.keys = _finalSpace1_allKeys[-1].name  # just the last key pressed
            finalSpace1.rt = _finalSpace1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *spaceFinal1* updates
    if spaceFinal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spaceFinal1.frameNStart = frameN  # exact frame index
        spaceFinal1.tStart = t  # local t and not account for scr refresh
        spaceFinal1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spaceFinal1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'spaceFinal1.started')
        spaceFinal1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finalScreen" ---
for thisComponent in finalScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if finalSpace1.keys in ['', [], None]:  # No response was made
    finalSpace1.keys = None
thisExp.addData('finalSpace1.keys',finalSpace1.keys)
if finalSpace1.keys != None:  # we had a response
    thisExp.addData('finalSpace1.rt', finalSpace1.rt)
thisExp.nextEntry()
# the Routine "finalScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='tab')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
