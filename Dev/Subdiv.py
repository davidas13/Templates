# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import pymel.core as pm


# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
sel = pm.ls(sl=1, type='mesh', dag=1)
val_sub = QtGui.QInputDialog.getInt(self, 'Set value Subdivision', 'Set value Subdivision', 3)
for x in sel:
    cek = pm.attributeQuery('vrayMaxSubdivs', n=x, ex=1)
    if cek == True and val_sub:
        print('{}: {}'.format(x, pm.getAttr(x.vrayMaxSubdivs)))
        pm.setAttr(x.vrayMaxSubdivs, val_sub[0])
        print('\tSET: {}'.format(pm.getAttr(x.vrayMaxSubdivs)))
    else:
        print('Attr Subdivision Not Found!')