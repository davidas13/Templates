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
find_word = 'V0'
end_word = 4

# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
items = (['V{}'.format(str(x).zfill(3)) for x in range(1,11)])
item, ok = QtGui.QInputDialog.getItem(self, 'Select Version Layer', 'List Version Layer', items, 0)

cur_prefix = pm.getAttr("vraySettings.fileNamePrefix")
ind_prefix = cur_prefix.find(find_word)
rep_prefix = cur_prefix.replace(cur_prefix[ind_prefix:ind_prefix + end_word], item)
print(cur_prefix[ind_prefix + end_word])

if ok and item and cur_prefix[ind_prefix + end_word] == '/':
    curRL = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
    if curRL != 'defaultRenderLayer':
        pm.editRenderLayerAdjustment ("vraySettings.fileNamePrefix")
        pm.setAttr("vraySettings.fileNamePrefix", rep_prefix, type='string')
    else:
        for x in pm.ls(typ='renderLayer'):
            if x not in seL and x != 'defaultRenderLayer':
                pm.editRenderLayerGlobals(currentRenderLayer=x)
                pm.editRenderLayerAdjustment ("vraySettings.fileNamePrefix", r=1)
        pm.setAttr("vraySettings.fileNamePrefix", rep_prefix, type='string')
        pm.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
else:
    print('{} Not Found!'.format(find_word))