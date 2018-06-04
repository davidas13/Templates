"""
    NOTE:

    show_print= :  Output Message with MessageDialog

    Alternatif:
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
        # pm.setAttr("CPS_MM.enabled", 0)
        pm.setAttr("Demi_MM_VRE.enabled", 0)
        pm.setAttr("ExtraTex_VRE.enabled", 0)

        # print('Edit Attr:\n\t CPS_MM: {}\n\t Demi_MM_VRE: {}\n\t ExtraTex_VRE: {}'.format(pm.getAttr("CPS_MM.enabled"), pm.getAttr("Demi_MM_VRE.enabled"), pm.getAttr("ExtraTex_VRE.enabled")))
        QtGui.QMessageBox.information(self, 'Information', 'Edit Attr (Demi Layer):\n    CPS_MM: {}\n    Demi_MM_VRE: {}\n    ExtraTex_VRE: {}'.format(pm.getAttr("CPS_MM.enabled"), pm.getAttr("Demi_MM_VRE.enabled"), pm.getAttr("ExtraTex_VRE.enabled")))
except Exception as ex:
    message = QtGui.QMessageBox.critical(self, 'Error', str(ex))