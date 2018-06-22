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
lisRL = pm.ls(typ='renderLayer')

path_split = pm.sceneName().split('/')
path_join = os.path.join('G:/PROJECTS/Vampirina2/AssetsRepo/Shots/',*path_split[-3:-1])
path_lc = os.path.join(path_join, 'LC_{}.vrlmap'.format(path_split[-2])).replace('\\', '/')

if os.path.exists(path_join):
    dRL = pm.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
    if 'defaultRenderLayer' in lisRL and 'M_RL_CACHE' not in lisRL:
        pm.duplicate('defaultRenderLayer', n='M_RL_CACHE', ic=1)
        pm.editRenderLayerGlobals(currentRenderLayer='M_RL_CACHE')

        pm.editRenderLayerAdjustment('vraySettings.mode')
        pm.editRenderLayerAdjustment('vraySettings.lc_autoSaveFile')
        pm.editRenderLayerAdjustment('vraySettings.lc_fileName')
        pm.editRenderLayerAdjustment('vraySettings.globopt_gi_dontRenderImage')

        pm.setAttr('vraySettings.globopt_gi_dontRenderImage', 1)
        pm.setAttr('vraySettings.mode', 0)

        pm.setAttr('vraySettings.lc_autoSaveFile', path_lc, type='string')
        pm.setAttr('vraySettings.lc_fileName', path_lc, type='string')

        pm.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        pm.setAttr('vraySettings.globopt_gi_dontRenderImage', 0)
        pm.setAttr('vraySettings.mode', 2)

        pm.setAttr('vraySettings.lc_fileName', path_lc, type='string')
        #setAttr -type "string" vraySettings.lc_fileName "33";

        QtGui.QMessageBox.information(self, 'Information', 'Membuat ML CACHE\nBerhasil!')
    else:
        pm.setAttr('vraySettings.lc_fileName', '', type='string')
        pm.setAttr('vraySettings.mode', 0)
        pm.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        pm.delete('M_RL_CACHE')

        QtGui.QMessageBox.information(self, 'Information', 'Menghapus BG CACHE\nBerhasil!')
else:
    QtGui.QMessageBox.critical(self, 'Error', 'Path Not Found!')


# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
