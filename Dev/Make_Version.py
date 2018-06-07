"""
NOTE MessageBox:
    Show Information: QtGui.QMessageBox.information(self)
    Show Question: QtGui.QMessageBox.question(self)
    Show Warning: QtGui.QMessageBox.warning(self)
    Show Critical: QtGui.QMessageBox.critical(self)

    With main:
            def main():
                pass
                
            if __name__=='__main__':
                main()
"""
# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------

# items = (['V00{}'.format(x) for x in range(1,11) if len(str(x)) == 2])
items = (['V{}'.format(str(x).zfill(3)) for x in range(1,11)])
print(items)

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
maya_path = '<Scene>/<Layer>_V001.exr'
maya_path_split = maya_path.split('_')
ver = 'V002'
print('{}_{}.exr'.format(maya_path_split[0], items[9]))