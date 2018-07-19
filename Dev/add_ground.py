import os
import sys
import pymel.core as pm
import maya.cmds as mc

pm.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
pm.hide('ground:Ground00_MSH')

pm.duplicate('BG_RL', n='BG_GROUND_RL', ic=1)

pm.editRenderLayerGlobals(currentRenderLayer='BG_GROUND_RL')
pm.select('ground:Ground00_MSH', r=1)
pm.showHidden(a=1)

try:
	pm.hide('ANB:BackyardVampirinaWeddingMess:Wedding_Ground00_MSH')
except:
	print('CARI GROUND!!!!!!!!!!!!!')

pm.editRenderLayerAdjustment("vraySettings.renderMaskMode")
pm.setAttr("vraySettings.renderMaskMode", 3)
pm.editRenderLayerAdjustment("vraySettings.renderMaskObjectIDs")
pm.setAttr('vraySettings.renderMaskObjectIDs', "3001", type="string")
pm.select('ground:Ground00_MSH', r=1)
mc.vray("addAttributesFromGroup", "ground:Ground00_MSH", "vray_objectID", 1)
pm.editRenderLayerAdjustment("ground:Ground00_MSH.vrayObjectID")
pm.setAttr("ground:Ground00_MSH.vrayObjectID", 3001)
mc.sets('ground:Ground00_MSH', edit=1, forceElement='VOP_Set')
