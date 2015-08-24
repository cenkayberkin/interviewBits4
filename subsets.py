__author__ = 'cenk'

def subsets(text):
  length = len(text)
  masks = []
  result = []
  for i in range(2 ** length):
    masks.append(bin(i)[2:].zfill(length))
  for mask in masks:
    result.append(applyMask(mask,text))
  r = sorted(result)
  return r

def applyMask(mask,text):
  result = []
  for index,i in enumerate(mask):
    if i == "1":
      result.append(text[index])

  r = sorted(result)
  return r


S = [12,13]
print subsets(S)