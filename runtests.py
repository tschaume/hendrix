#! python

import os
import sys

# begin chdir armor
sys.path[:] = map(os.path.abspath, sys.path)
# end chdir armor

sys.path.insert(0, os.path.abspath(os.getcwd()))
sys.argv.append("hendrix/test")

from twisted.scripts.trial import run

run()
