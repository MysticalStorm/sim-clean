import re
import subprocess

bashCommand = "xcrun simctl list --json"
output = subprocess.check_output(['bash','-c', bashCommand])
udids = re.findall('"udid" : "(.*)"', output)

for udid in udids:
    bashCommand = "xcrun simctl erase %s" % udid
    print "Erase - %s" %udid

print "Done"

