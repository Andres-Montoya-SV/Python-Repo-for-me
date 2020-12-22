## Self replicating Python program
from sys import argv
import subprocess

details = argv
name = str(details[0])
print(details)

for i in range(0, 20):
    directoryName = 'copy' + str(i)
    subprocess.call(['mkdir', directoryName])
    subprocess.call(['cp',name, directoryName])