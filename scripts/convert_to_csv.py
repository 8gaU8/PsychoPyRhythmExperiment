# import PsychoPy function for loading Pickle/JSON data
from psychopy.misc import fromFile
# (replace with the file path to your .psydat file)
fpath = '/Users/my_user/myexperiments/myexperiment/participant_expname_date.psydat'
fpath = './data/237942abc_rhythm_trial_exp_2023-07-27_20h06.26.961.psydat'
# load in the data
psydata = fromFile(fpath)
# (replace with the file path to where you want the resulting .csv
# to be saved)
save_path = 'test.csv'
# save the data as a .csv file, ie separating the values with a
# comma. 'CSV' simply means 'comma-separated values'
psydata.saveAsWideText(save_path, delim=',')