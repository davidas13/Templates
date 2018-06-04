# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import RD_Vamp2 as aw
reload(aw)

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
try:
    aw.set_GeneralSett_btn()
    aw.set_output_btn()
    aw.Cam_img_plane_fix_btn()
    aw.disable_DiscoBoots_btn()
    QtGui.QMessageBox.information(self, 'Information', 'Run: set_OptRender_MstrLyr\nRun: aw.set_output_btn\nRun: Cam_img_plane_fix_btn\nRun: disable_DiscoBoots_btn')
except Exception as ex:
    message = QtGui.QMessageBox.critical(self, 'Error', str(ex))
