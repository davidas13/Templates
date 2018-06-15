import pymel.core as pm

sel = pm.ls(sl=1)
ob_sel = []
cur_rl = pm.editRenderLayerGlobals(q=1, crl=1)
er = pm.editRenderLayerAdjustment( cur_rl, q=1, lyr=1)
# global er, cur_rl

def attr(obj, val):
	if type(er) is list:
	    for x in er:
	        pm.editRenderLayerAdjustment(x, r=1)
	else:
	    pm.editRenderLayerAdjustment(obj.objectIDEnabled)
	    pm.editRenderLayerAdjustment(obj.objectID)
	    pm.setAttr(obj.objectIDEnabled, val)
	    # pm.setAttr(obj.objectID, 2002)
	    

print('Object ID')
print(pm.editRenderLayerAdjustment( query=True, alg=True ))
if cur_rl != 'defaultRenderLayer':
    for x in sel:
        try:
            print(pm.getAttr(x.objectIDEnabled))
            if pm.getAttr(x.objectIDEnabled) is True:
                # attr(x, 1)
                # ob_sel.append(x)
                print('\t{}: {} -> {}'.format(x, pm.getAttr(x.objectIDEnabled), pm.getAttr(x.objectID)))
            else:
                attr(x, 1)
                ob_sel.append(x)

                print('\t{}: {}'.format(x, pm.getAttr(x.objectIDEnabled)))
        except Exception as ex:
            # pass
            # print(type(ex))
            print('\t{}: {}'.format(x, ex))
            #raise AttributeError
            print(path_lc)


# print(ob_sel[0])
# print(cur_rl)