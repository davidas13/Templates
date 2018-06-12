"""
NOTE Auto Save:
1. Mencari path sesuai shot
2. jika ada file dgn nama yg sama di dalam directory maka akan direplace
3. file sebelumnya akan dibackup di folder Documents dengan folder sesuai tanggal


detect path:
- J:/
- Vampirina2/AssetsRepo/Shots/
- EP202B/SH122.00/
"""
# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import os
import sys
import time
import pymel.core as pm
import maya.cmds as cmds

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
username = os.environ['USERNAME']
SC_PATH = pm.sceneName()
spath = SC_PATH.split('/')
num_C = 2
num_J = 4

BACKUP_PATH = 'C:/Users/{}/Documents/BackupSH'.format(username)
print(SC_PATH)

# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------

# Detection Dir File
if spath[0] == 'C:':
	BACKUP_FILE = os.path.join(BACKUP_PATH, '/'.join(spath[num_J:])) #'C:/Users/{}/Documents/BackupSH/{}'.format(username, '/'.join(spath[num_J:]))
	DIR = 'J:/Productions/{}'.format('/'.join(spath[num_J:]))
	print('FROM C:')
	print('\tFile Dir J: {}\n\tFile Backup: {}'.format(DIR, BACKUP_FILE))
elif spath[0] == 'J:':
	BACKUP_FILE = os.path.join(BACKUP_PATH, '/'.join(spath[num_C:])) #'C:/Users/{}/Documents/BackupSH/{}'.format(username, '/'.join(spath[num_C:]))
	DIR = 'C:/Users/{}/Projects/{}'.format(username, '/'.join(spath[num_C:]))
	print('FROM J:')
	print('\tFile Dir C: {}\n\tFile Backup: {}'.format(DIR, BACKUP_FILE))

item, ok = QtGui.QInputDialog.getItem(self, 'Select Action', 'Action File:', ['Replace', 'Backup', 'Backup & Open (J)'], 0)
fil_nam = os.path.join(os.path.dirname(BACKUP_FILE), time.strftime("%d_%m_%Y"))
nam = os.path.join(fil_nam, os.path.basename(BACKUP_FILE))

if ok:
    if item == 'Replace':
        if os.path.isfile(DIR):
            cmds.file( save=1)
            pm.sysFile(SC_PATH, cp=DIR)
            print(item, DIR)
    elif item == 'Backup':
        if not os.path.exists(fil_nam):
            pm.sysFile(fil_nam, md=1)
            
        if os.path.isfile(DIR):
            pm.sysFile(DIR, cp=nam)
            cmds.file( save=1)
            pm.sysFile(SC_PATH, cp=DIR)
            print(item, DIR)
    elif item == 'Backup & Open (J)' and spath[0] == 'C:':
        if not os.path.exists(fil_nam):
            pm.sysFile(fil_nam, md=1)
            
        if os.path.isfile(DIR):
            pm.sysFile(DIR, cp=nam)
            cmds.file( save=1)
            pm.sysFile(SC_PATH, cp=DIR)
            print(item, DIR)
            cmds.file(DIR, o=True )
    else:
        print('Not Work!')
else:
    print('Cancel')