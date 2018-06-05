# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import BBF.Maya.Tools.Lighting.LGTBuild.LGTBuild as LGTBuild
reload(LGTBuild)


# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------



# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
# Masukan kode disini
LGTBuild.run()
lgtui = LGTBuild.LGTBuildUIWnd
# print(help(LGTBuild.run()))
if lgtui.optionsui.anb_file.displayText() != '':
    lgtui.optionsui.browse_anim.click()
    question = QtGui.QMessageBox.question(self, 'LGT File', 'Apakah kamu ingin mengisi manual file LGT ?', QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Open, QtGui.QMessageBox.Cancel)
    if question == QtGui.QMessageBox.Open:
        lgtui.optionsui.browse_lgt.click()
else:
    lgtui.close() # Optional


