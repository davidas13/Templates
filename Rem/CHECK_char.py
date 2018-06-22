"""
S:\pipeline\BASE_PIPELINE\BBF\Maya\Lib\bbfCharLightRig

"""
import pymel.core as pm
import re
import bbfCharLightRig.bbfCharLightRigUtil as lis

# ----------------------------------------------------------------------
# Settings
# ----------------------------------------------------------------------
# Checked = set 1
# Unchecked = set 0
set_ = 0

# ----------------------------------------------------------------------
# Variabel
# ----------------------------------------------------------------------
act = lis.listLights()
key_ = act.keys()
value_ = act.values()

# ----------------------------------------------------------------------
# Action
# ----------------------------------------------------------------------
for char in key_:
    # Variabel
    get_fill = '-'
    get_rim = '-'
    get_key = '-'

    if pm.getAttr(char + ".fillType") != 0:
        pm.setAttr(char + ".fillType", 0)
        get_fill = pm.getAttr(char + ".fillType")

    if pm.getAttr(char + ".rimType") != 0:
        pm.setAttr(char + ".rimType", 0)
        get_rim = pm.getAttr(char + ".rimType")

    if pm.getAttr(char + ".keyVisibility") != set_:
        pm.setAttr(char + ".keyVisibility", set_)
        get_key = pm.getAttr(char + ".keyVisibility")
        # get_fill = pm.getAttr(char + ".fillType")
        # get_rim = pm.getAttr(char + ".rimType")
        # get_key = pm.getAttr(char + ".keyVisibility")

        # print('CHANGE FILL: {} {}'.format(char.split(':')[0],get_fill))
        # print('\n== CHANGE ALL VALUES ==')
    else:
        # print('\nCHAR: {}:\n\tKey: {}\n\tFill: {}\n\tRim: {}'.format(char, get_key, get_fill, get_rim))
        print('\n== {} IS CORRECT =='.format(char))
    # print('CHAR: {}:\n\tKey: {}\n\tFill: {}\n\tRim: {}'.format(char, get_key, get_fill, get_rim))
    print('CHAR: {}:\n\tKey: {}\n\tFill: {}\n\tRim: {}'.format(char, get_key, get_fill, get_rim))