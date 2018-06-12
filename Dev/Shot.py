# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import pymel.core as pm

import RD_Vamp2 as aw
reload(aw)


# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
# Script 1
try:
    aw.set_GeneralSett_btn()
    aw.set_output_btn()
    aw.Cam_img_plane_fix_btn()
    aw.disable_DiscoBoots_btn()
    QtGui.QMessageBox.information(self, 'Information', 'Run: set_OptRender_MstrLyr\nRun: aw.set_output_btn\nRun: Cam_img_plane_fix_btn\nRun: disable_DiscoBoots_btn')
except Exception as ex:
    message = QtGui.QMessageBox.critical(self, 'Error', 'Error Script 1\n{}'.format(str(ex)))


# Script 2
try:
    curRL = pm.editRenderLayerGlobals(currentRenderLayer='Demi')
    if curRL != "defaultRenderLayer":
        print(curRL)
        pm.editRenderLayerAdjustment("CPS_MM.enabled")
        pm.editRenderLayerAdjustment("Demi_MM_VRE.enabled")
        pm.editRenderLayerAdjustment("ExtraTex_VRE.enabled")

        pm.setAttr("CPS_MM.enabled", 1)
        pm.setAttr("Demi_MM_VRE.enabled", 1)
        pm.setAttr("ExtraTex_VRE.enabled", 1)

        pm.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        pm.setAttr("CPS_MM.enabled", 1)
        pm.setAttr("Demi_MM_VRE.enabled", 0)
        pm.setAttr("ExtraTex_VRE.enabled", 0)

        # print('Edit Attr:\n\t CPS_MM: {}\n\t Demi_MM_VRE: {}\n\t ExtraTex_VRE: {}'.format(pm.getAttr("CPS_MM.enabled"), pm.getAttr("Demi_MM_VRE.enabled"), pm.getAttr("ExtraTex_VRE.enabled")))
        QtGui.QMessageBox.information(self, 'Information', 'Edit Attr (Demi Layer):\n    CPS_MM: {}\n    Demi_MM_VRE: {}\n    ExtraTex_VRE: {}'.format(pm.getAttr("CPS_MM.enabled"), pm.getAttr("Demi_MM_VRE.enabled"), pm.getAttr("ExtraTex_VRE.enabled")))
except Exception as ex:
    message = QtGui.QMessageBox.critical(self, 'Error', 'Error Script 2\n{}'.format(str(ex)))