# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import pymel.core as pm
import bbfCharLightRig.bbfCharLightRigUtil as lis
reload(lis)
# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
activate_tooltip = True

TOOLTIP = """
Script ini mengecek dan mengubah attribute Char:
1. Key -> (Uncheck)
2. Fill -> (Area)
3. Rim -> (Area)
"""

# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
def main():
    set_ = 0
    act = lis.listLights()
    key_ = act.keys()
    value_ = act.values()
    # Masukan kode disini
    for char in key_:
        get_fill = pm.getAttr(char + ".fillType")

        get_rim = pm.getAttr(char + ".rimType")

        get_key = pm.getAttr(char + ".keyVisibility")
