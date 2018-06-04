# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import pymel.core as pm


# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
#ANB:ShotCam:CAMTILTLocator
sel = pm.ls(sl=1)
# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
lis = pm.ls('VRaySphereFade*')#VRaySphereFadeVolume
if 'VRaySphereFadeShape1' not in lis:
    curRL = pm.editRenderLayerGlobals(q=1, crl=1)
    if curRL != 'defaultRenderLayer':
        pm.mel.eval('vrayCreateSphereFade;')
        pm.setAttr("VRaySphereFadeShape1.shape", 1)
        pm.setAttr("VRaySphereFadeShape1.enabled", 0)
        pm.editRenderLayerAdjustment("VRaySphereFadeShape1.enabled")
        pm.setAttr("VRaySphereFadeShape1.enabled", 1)
        pm.setAttr("VRaySphereFadeVolume1.falloff", 0.02)
        pm.setAttr("VRaySphereFadeVolume1.emptyColor", 0, 0, 0, type='double3')
        pm.setAttr("VRaySphereFadeVolume1.affectAlpha", 1)
        try:
            pm.setAttr("VRaySphereFade1.translateY", pm.getAttr('*::ShotCam:GUIDES.translateY'))
            pm.setAttr("VRaySphereFade1.translateX", pm.getAttr('*::ShotCam:GUIDES.translateX'))
            pm.setAttr("VRaySphereFade1.translateZ", pm.getAttr('*::ShotCam:GUIDES.translateZ'))

            pm.setAttr("VRaySphereFade1.scaleX", 80)
            pm.setAttr("VRaySphereFade1.scaleY", 80)
            pm.setAttr("VRaySphereFade1.scaleZ", 80)
        except:
            pass
        pm.select('VRaySphereFade1')
        QtGui.QMessageBox.information(self, 'Information', 'Membuat VRaySphereFadeShape1\nBerhasil!')
    else:
        QtGui.QMessageBox.critical(self, 'Error', 'Membuat VRaySphereFadeShape1 Gagal!\nKarena membuat di masterlayer\n*Buatlah diluar "masterlayer"')
else:
    pm.delete('VRaySphereFade*')
    QtGui.QMessageBox.information(self, 'Information', 'Hapus VRaySphereFadeShape1\nBerhasil!')
    pm.select(cl=1)
