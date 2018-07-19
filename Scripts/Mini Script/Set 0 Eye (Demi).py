
# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------

import pymel.core as pm


# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
sel = pm.ls(typ='reference')
refDemi = []


# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------

for i in range(len(sel)):
    if 'ANB:Demi' in str(sel[i]):
        print(sel[i].split('RN')[0])
        refDemi.append(sel[i].split('RN')[0])

if len(refDemi) != 0:
    item, ok = QtGui.QInputDialog.getItem(self, 'Select Demi', 'List Demi ref', refDemi, 0)
    if ok and item:	
        dem = ['{}:EYES_R_highlight'.format(item), '{}:EYES_L_highlight'.format(item)]
        for x in dem:
            pm.select(x+'_OC', tgl=1)
            pm.select(x+'_CTRL', tgl=1)
            pm.setAttr(x+'_OC.offsetZ', 0)
            pm.setAttr(x+'_OC.offsetX', 0)
            pm.setAttr(x+'_OC.offsetY', 0)
            pm.setAttr(x+'_CTRL.rotateX', 0)
            pm.setAttr(x+'_CTRL.rotateY', 0)
            pm.setAttr(x+'_CTRL.auto', 0)