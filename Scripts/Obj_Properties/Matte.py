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
                pm.editRenderLayerAdjustment(sel.ignore, layer=render_layer)
                pm.editRenderLayerAdjustment(sel.matteSurface, layer=render_layer)
                pm.editRenderLayerAdjustment(sel.alphaContribution, layer=render_layer)
                pm.editRenderLayerAdjustment(sel.affectAlpha, layer=render_layer)
                pm.editRenderLayerAdjustment(sel.reflectionAmount, layer=render_layer)
                pm.editRenderLayerAdjustment(sel.refractionAmount, layer=render_layer)
                pm.editRenderLayerAdjustment(sel.receiveGI, layer=render_layer)
                pm.editRenderLayerAdjustment(sel.generateRenderElements, layer=render_layer)
                pm.editRenderLayerAdjustment(sel.reflectionVisibility, layer=render_layer)
                sel.ignore.set(0)
                sel.matteSurface.set(1)
                sel.alphaContribution.set(-1)
                sel.affectAlpha.set(1)
                sel.reflectionAmount.set(0.0)
                sel.refractionAmount.set(0.0)
                sel.receiveGI.set(0)
                sel.generateRenderElements.set(0)
                sel.reflectionVisibility.set(0)
            except Exception as ex:
                print('ERROR: {}'.format(ex))