#!/usr/bin/env python

import sys
import machine_learning as ml

MODE = sys.argv[1]
ALGORITHM = sys.argv[2]
INPUT_FILE = open(sys.argv[3], 'r')
PROGRAM = sys.argv[4]

if ALGORITHM == 'zero_rules':
  ml.zero_rules(INPUT_FILE, PROGRAM)

INPUT_FILE.close()

