from Static_Resources import *
from time import *
import sys


def printer(stuff):
    sys.stdout.write("\r\x1b[K" + stuff.__str__())
    sys.stdout.flush()
