#!/usr/bin/python
import os
import subproces
process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
out, err = process.communicate()
print(out)

