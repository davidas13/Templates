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
er = pm.editRenderLayerAdjustment( cur_rl, q=1, lyr=1)

# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
print('Object ID')
print(pm.editRenderLayerAdjustment( query=True, alg=True ))
if cur_rl != 'defaultRenderLayer':
    for x in sel:
        try:
            ob_sel.append(x)
            if str(pm.getAttr(x.objectID)) == str(0):
                pm.editRenderLayerAdjustment(x.objectIDEnabled)
                pm.editRenderLayerAdjustment(x.objectID)
                pm.setAttr(x.objectIDEnabled, 1)
                pm.setAttr(x.objectID, int('200' + str(ob_sel.index(x))))
                pm.editRenderLayerAdjustment("vraySettings.renderMaskMode")
                pm.setAttr("vraySettings.renderMaskMode", 3)
                pm.editRenderLayerAdjustment("vraySettings.renderMaskObjectIDs")
                pm.setAttr('vraySettings.renderMaskObjectIDs', ', '.join(map(str, [int('2' + str(x).zfill(3)) for x in range(len(ob_sel))])), type="string")
            else:
                pm.editRenderLayerAdjustment(x.objectIDEnabled, r=1)
                pm.editRenderLayerAdjustment(x.objectID, r=1)
                pm.editRenderLayerAdjustment("vraySettings.renderMaskMode", r=1)
                pm.editRenderLayerAdjustment("vraySettings.renderMaskObjectIDs", r=1)
        except Exception as ex:
            print('\t{}: {}'.format(x, ex))
