import win32api
import win32con
import win32security

global win32api, win32con, win32security

def get_owner(fname):
    FILENAME = "fname"
    open (FILENAME, "w").close()
    sd = win32security.GetFileSecurity (FILENAME, win32security.OWNER_SECURITY_INFORMATION)
    owner_sid = sd.GetSecurityDescriptorOwner ()
    name, domain, type = win32security.LookupAccountSid (None, owner_sid)
    return name

# import win32api
# import win32con
# import win32security

# FILENAME = "G:/PROJECTS/Vampirina2/tmp/RenderComp/UR/202B/202B_SH017.10 fr133-172.png"
# open (FILENAME, "w").close ()

# print "I am", win32api.GetUserNameEx (win32con.NameSamCompatible)

# sd = win32security.GetFileSecurity (FILENAME, win32security.OWNER_SECURITY_INFORMATION)
# owner_sid = sd.GetSecurityDescriptorOwner ()
# name, domain, type = win32security.LookupAccountSid (None, owner_sid)

# print "File owned by %s\\%s" % (domain, name)