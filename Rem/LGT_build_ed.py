# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import BBF.Maya.Tools.Lighting.LGTBuild.LGTBuild as LGTBuild
reload(LGTBuild)


# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
activate_tooltip = True

TOOLTIP = """
Script ini menjalankan button:
1. Button Browse (ANB)
2. Button Run (Ctrl+R)
"""


# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
def main():
    global LGTBuild
    # Masukan kode disini
    LGTBuild.run()
    lgtui = LGTBuild.LGTBuildUIWnd
    # print(help(LGTBuild.run()))
    lgtui.optionsui.browse_anim.click()
    # print('\n\n=> PATH LGT: {}\n\n'.format(lgtui.optionsui.lgt_file.displayText()))
    if lgtui.optionsui.anb_file.displayText() != '':
        lgtui.close() # Optional
    elif lgtui.optionsui.lgt_file.displayText() != '':
        lgtui.optionsui.browse_anim.click()
    else:
        pass
        # lgtui.view._ui.pbRun.click()
    pass
    

if __name__=='__main__':
    main()