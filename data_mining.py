#!/usr/bin/env python

import sys
import machine_learning as ml

MODE = sys.argv[1]

if MODE == 'train':
  algorithm = sys.argv[2]
  input_file = open(sys.argv[3], 'r')
  program = sys.argv[4]

  if algorithm == 'zero_rules':
    ml.zero_rules(input_file, program)

  input_file.close()

elif MODE == 'test':
  program = sys.argv[2]
  test_file = open(sys.argv[3], 'r')

  test_file.close()

