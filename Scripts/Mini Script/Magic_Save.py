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
import datetime
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

item_cb = ['Replace (Save)', 'Backup (Save)', 'Backup (No Save)', 'Backup This Scene (No Save)']
BACKUP_PATH = 'C:/Users/{}/Documents/BackupSH'.format(username)
print(SC_PATH)

# ----------------------------------------------------------------------
# Main Script
# # ----------------------------------------------------------------------
# Link Ref File : http://timgolden.me.uk/python/win32_how_do_i/get-the-owner-of-a-file.html
# http://timgolden.me.uk
import win32api
import win32con
import win32security
global win32api, win32con, win32security

def get_owner(fname):
    FILENAME = fname
    open (FILENAME, "w").close()
    sd = win32security.GetFileSecurity (FILENAME, win32security.OWNER_SECURITY_INFORMATION)
    owner_sid = sd.GetSecurityDescriptorOwner ()
    name, domain, type = win32security.LookupAccountSid (None, owner_sid)
    return name

# Detection Dir File
if spath[0] == 'C:':
    item_cb.insert(4,'Backup & Open (J)')
    item_cb.insert(1,'Open (J)')
    BACKUP_FILE = os.path.join(BACKUP_PATH, '/'.join(spath[num_J:])) #'C:/Users/{}/Documents/BackupSH/{}'.format(username, '/'.join(spath[num_J:]))
    DIR = 'J:/Productions/{}'.format('/'.join(spath[num_J:]))
    print('FROM C:')
    print('\tFile Dir J: {}\n\tFile Backup: {}'.format(DIR, BACKUP_FILE))
elif spath[0] == 'J:':
	BACKUP_FILE = os.path.join(BACKUP_PATH, '/'.join(spath[num_C:])) #'C:/Users/{}/Documents/BackupSH/{}'.format(username, '/'.join(spath[num_C:]))
	DIR = 'C:/Users/{}/Projects/{}'.format(username, '/'.join(spath[num_C:]))
	print('FROM J:')
	print('\tFile Dir C: {}\n\tFile Backup: {}'.format(DIR, BACKUP_FILE))

item, ok = QtGui.QInputDialog.getItem(self, 'Select Action', 'Action File:', item_cb, 0)

try:
    if ok and item:
        fil_nam = os.path.join(os.path.dirname(BACKUP_FILE), datetime.datetime.fromtimestamp(os.stat(DIR).st_mtime).strftime("{} (%m_%d_%Y)".format(get_owner(DIR))))
        #datetime.datetime.fromtimestamp(os.stat(file_).st_mtime).strftime("%d_%m_%Y")
        nam = os.path.join(fil_nam, os.path.basename(BACKUP_FILE))
        if item == 'Replace (Save)':
            if os.path.isfile(DIR):
                cmds.file( save=1)
                pm.sysFile(SC_PATH, cp=DIR)
                print(item, DIR)
        elif item == 'Backup (Save)':
            if not os.path.exists(fil_nam):
                pm.sysFile(fil_nam, md=1)
                
            if os.path.isfile(DIR):
                pm.sysFile(DIR, cp=nam)
                cmds.file( save=1)
                pm.sysFile(SC_PATH, cp=DIR)
                print(item, DIR)
        elif item == 'Backup (No Save)':
            if not os.path.exists(fil_nam):
                pm.sysFile(fil_nam, md=1)
                
            if os.path.isfile(DIR):
                pm.sysFile(DIR, cp=nam)
                pm.sysFile(SC_PATH, cp=DIR)
                print(item, DIR)
        elif item == 'Backup (J) This Scene (No Save)':
            if os.path.isfile(DIR):
                pm.sysFile(SC_PATH, cp=DIR)
                pm.sysFile(DIR, cp=nam)

            if not os.path.exists(fil_nam):
                pm.sysFile(fil_nam, md=1)
                
        elif item == 'Backup & Open (J)' and spath[0] == 'C:':
            if not os.path.exists(fil_nam):
                pm.sysFile(fil_nam, md=1)
                
            if os.path.isfile(DIR):
                pm.sysFile(DIR, cp=nam)
                cmds.file(save=1)
                pm.sysFile(SC_PATH, cp=DIR)
                print(item, DIR)
                cmds.file(new=1, f=1)
                cmds.file(DIR, o=1 )
        elif item == 'Open (J)' and spath[0] == 'C':
                cmds.file(new=1, f=1)
                cmds.file(DIR, o=1 )
        else:
            print('Not Work!')
    else:
        print('Cancel')
except NameError:
    print('File has no Path!')
except WindowsError:
    pass