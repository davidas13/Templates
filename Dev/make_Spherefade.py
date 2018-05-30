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
pm.mel.eval('vrayCreateSphereFade;')
pm.setAttr("VRaySphereFadeShape1.shape", 1)
pm.setAttr("VRaySphereFadeShape1.enabled", 0)
pm.editRenderLayerAdjustment("VRaySphereFadeShape1.enabled")
pm.setAttr("VRaySphereFadeShape1.enabled", 1)
pm.setAttr("VRaySphereFadeVolume1.falloff", 0.02)
pm.setAttr("VRaySphereFadeVolume1.emptyColor", 0, 0, 0, type='double3')
pm.setAttr("VRaySphereFadeVolume1.affectAlpha", 1)

show_information = 'Create VRaySphereFadeShape1\nSuccessfully!'