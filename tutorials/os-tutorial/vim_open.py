import subprocess
import sys

f = sys.argv[1]

subprocess.call(['vi', '-M', f])