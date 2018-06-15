"""
NOTE MessageBox:
    Show Information: QtGui.QMessageBox.information(self)
    Show Question: QtGui.QMessageBox.question(self)
    Show Warning: QtGui.QMessageBox.warning(self)
    Show Critical: QtGui.QMessageBox.critical(self)

    With main:
            def main():
                pass
                
            if __name__=='__main__':
                main()
"""
# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import pymel.core as pm



# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
sel = pm.ls(sl=1)
ob_sel = []
cur_rl = pm.editRenderLayerGlobals(q=1, crl=1)

def attr(obj, val):
    cur_rl = pm.editRenderLayerGlobals(q=1, crl=1)
    er = pm.editRenderLayerAdjustment( cur_rl, q=1, lyr=1)
    if type(er) is list:
	    for x in er:
	        pm.editRenderLayerAdjustment(x, r=1)
    else:
	    pm.editRenderLayerAdjustment(obj.objectIDEnabled)
	    pm.editRenderLayerAdjustment(obj.objectID)
	    pm.setAttr(obj.objectIDEnabled, val)
	    pm.setAttr(obj.objectID, 2002)

# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
print('Object ID')
print(pm.editRenderLayerAdjustment( query=True, alg=True ))
if cur_rl != 'defaultRenderLayer':
    for x in sel:
        try:
            if pm.getAttr(x.objectIDEnabled) is True:
                attr(x, 1)
                ob_sel.append(x)
                print('\t{}: {} -> {}'.format(x, getAttr(x.objectIDEnabled), getAttr(x.objectID)))
            else:
                attr(x, 1)
                ob_sel.append(x)
                print('\t{}: {}'.format(x, getAttr(x.objectIDEnabled)))
        except Exception as ex:
            # print(type(ex))
            print('\t{}: {}'.format(x, ex))
            #raise AttributeError



