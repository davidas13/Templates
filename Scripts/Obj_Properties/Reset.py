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
lis_sel = pm.ls(sl=True)

if lis_sel:
    for sel in lis_sel:
        print(sel)
        if pm.nodeType(sel) == "VRayObjectProperties":
            render_layer = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
            try:
                print(render_layer)
                pm.editRenderLayerAdjustment(sel.ignore, layer=render_layer, remove=1)
                pm.editRenderLayerAdjustment(sel.matteSurface, layer=render_layer, remove=1)
                pm.editRenderLayerAdjustment(sel.alphaContribution, layer=render_layer, remove=1)
                pm.editRenderLayerAdjustment(sel.affectAlpha, layer=render_layer, remove=1)
                pm.editRenderLayerAdjustment(sel.reflectionAmount, layer=render_layer, remove=1)
                pm.editRenderLayerAdjustment(sel.refractionAmount, layer=render_layer, remove=1)
                pm.editRenderLayerAdjustment(sel.receiveGI, layer=render_layer, remove=1)
                pm.editRenderLayerAdjustment(sel.generateRenderElements, layer=render_layer, remove=1)
                pm.editRenderLayerAdjustment(sel.reflectionVisibility, layer=render_layer, remove=1)
                pm.editRenderLayerAdjustment(sel.primaryVisibility, layer=render_layer, remove=1)
                pm.editRenderLayerAdjustment(sel.shadows, layer=render_layer, remove=1)
            except Exception as ex:
                print('ERROR: {}'.format(ex))