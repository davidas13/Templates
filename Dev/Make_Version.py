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


# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
items = (['V{}'.format(str(x).zfill(3)) for x in range(1,11)])

item, ok = QtGui.QInputDialog.getItem(self, 'Select Version Layer', 'List Version Layer', items, 0)

fnp_path = pm.getAttr("vraySettings.fileNamePrefix")
fnp_path_split = fnp_path.split('_')
fnp_path_ver = fnp_path_split[-1].split('/')

print(fnp_path_split)       #[u'EP202B/SH049.00/<Layer>', u'V001/<Layer>']
print(fnp_path_ver)     # V001

#EP202B/SH049.00/<Layer>_V001/<Layer>
if ok and item:
    # print('{}_{}.exr'.format(fnp_path_split[0], item))
    file_prefix = '{}_{}/{}'.format(fnp_path_split[0], item, fnp_path_ver[-1])
    # print(file_prefix)
    seL = pm.ls(typ='renderLayer', rn=1)
    # print(seL)
    # for x in seL:
    #     if x != 'defaultRenderLayer':
    #         pm.editRenderLayerGlobals(currentRenderLayer=x)
    #         pm.editRenderLayerAdjustment ("vraySettings.fileNamePrefix", r=1)
    #         print(x)
    curRL = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
    if curRL != 'defaultRenderLayer':
        pm.editRenderLayerAdjustment ("vraySettings.fileNamePrefix")
        pm.setAttr("vraySettings.fileNamePrefix", file_prefix, type='string')
    else:
        for x in pm.ls(typ='renderLayer'):
            if x not in seL and x != 'defaultRenderLayer':
                pm.editRenderLayerGlobals(currentRenderLayer=x)
                pm.editRenderLayerAdjustment ("vraySettings.fileNamePrefix", r=1)
        #pm.setAttr("vraySettings.fileNamePrefix", file_prefix)
        #pm.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')