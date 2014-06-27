#!/usr/bin/env python

def zero_rules (input_file, program):
  name, attributes, classes, data = read_file(input_file)
  class_count = []

  for klass in classes:
    class_count.append(0)

  for value in data:
    for index, klass in enumerate(classes):
      if value[0] == klass:
        class_count[index] += 1

  zero_rules_class = classes[class_count.index(max(class_count))]

  print name
  print attributes
  print classes
  print data
  print zero_rules_class


def read_file(input_file):
  attributes = []
  attributes_type = []
  classes = []
  final_data = []
  data = []
  data_values = []
  data_classes = []
  flag = 0

  name = input_file.readline().rstrip('\n')

  for line in input_file:

    if line != '@dados\n' and flag == 0:

      if(line.split(',')[0] == 'classe'):
        classes = line.split(',')[2:-1]
        classes.append(line.split(',')[-1].rstrip('\n'))

      else:
        attributes.append(line.split(',')[0])
        attributes_type.append(line.split(',')[1].rstrip('\n'))

    else:
      flag = 1
      if line != '@dados\n':
        data_values.append(line.split(',')[0:len(attributes)])
        data_classes.append(line.split(',')[len(attributes)].rstrip('\n'))

  for index, value in enumerate(data_classes):
    data.append([value, data_values[index]])

  return name, attributes, classes, data