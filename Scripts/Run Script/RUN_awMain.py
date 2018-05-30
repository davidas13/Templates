# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import RD_Vamp2 as aw
reload(aw)

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
activate_tooltip = True

TOOLTIP = """
Script ini menjalankan button:
1. set_OptRender_MstrLyr
2. aw.set_output_btn
3. Cam_img_plane_fix_btn
4. disable_DiscoBoots_btn
Script diatas dijalankan secara bersamaan.
"""

# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
aw.set_GeneralSett_btn()
print('-> set_OptRender_MstrLyr')
aw.set_output_btn()
print('-> aw.set_output_btn')
aw.Cam_img_plane_fix_btn()
print('-> Cam_img_plane_fix_btn')
aw.disable_DiscoBoots_btn()
print('-> disable_DiscoBoots_btn')

show_print = 'set_OptRender_MstrLyr\naw.set_output_btn\nCam_img_plane_fix_btn\ndisable_DiscoBoots_btn'