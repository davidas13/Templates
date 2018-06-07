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

maya_path = '<Scene>/<Layer>_V001.exr'
maya_path_split = maya_path.split('_')
if ok and item:
    # print('{}_{}.exr'.format(maya_path_split[0], item))
    file_prefix = '{}_{}.exr'.format(maya_path_split[0], item)
    seL = pm.ls(typ='renderLayer')
    print(seL)
    # for x in seL:
    #     if x != 'defaultRenderLayer':
    #         pm.editRenderLayerGlobals(currentRenderLayer=x)
    #         pm.editRenderLayerAdjustment ("defaultRenderGlobals.imageFilePrefix", r=1)
    #         print(x)
    curRL = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
    if curRL != 'defaultRenderLayer':
        pm.editRenderLayerAdjustment ("defaultRenderGlobals.imageFilePrefix")
        pm.setAttr("defaultRenderGlobals.imageFilePrefix", file_prefix)
    else:
        for x in seL:
            if x != 'defaultRenderLayer':
                pm.editRenderLayerGlobals(currentRenderLayer=x)
                pm.editRenderLayerAdjustment ("defaultRenderGlobals.imageFilePrefix", r=1)
                print(x)
        pm.setAttr("defaultRenderGlobals.imageFilePrefix", file_prefix)
        pm.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')