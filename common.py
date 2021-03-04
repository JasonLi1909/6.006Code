##################################################
##  Problem 1. common
##################################################

# Given an array of lists of distinct numbers, 
# return the number of numbers common to all lists

def common(lists):
  '''
  Input:  lists  | Array of arrays of positive integers
  Output: num_common  | number of numbers common to all arrays
  '''
  if len(lists) == 0: 
    return 0
  commonNumbers = lists[0].copy()
  for list in lists: 
    for n in lists[0]: 
      if not n in list:
        try:
          commonNumbers.remove(n)
        except: 
          pass
  
  print(commonNumbers, len(commonNumbers))
  num_common = len(commonNumbers)
  return num_common

