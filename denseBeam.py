import re
import math

import os
import sys
import glob

from statistics import variance as Var
class CharData(object):
  def __init__(self):
    self.lazy_prob  = 0.
    self.view       = 0.

  def getProb():
    self.lazy_prob = self.view / self.total_view



char_char_data = {}
def main():
  contexts = ""
  files = glob.glob('data/*.utf8') 
  for file in files:
    with open(file, "r") as f:
      contexts += f.read()

  for start in range(1, len(contexts) - 1 ):
    prv, tgt, nxt = contexts[start-1], contexts[start], contexts[start+1]

    """ crop window """
    if char_char_data.get(tgt) is None:
      char_char_data[tgt] = {}
    if char_char_data[tgt].get(nxt) is None:
      char_char_data[tgt][nxt] = CharData()
    char_char_data[tgt][nxt].view += 1.
  
  for ci, c in enumerate(contexts):
    cnxt = contexts[ci+1]
    total = sum(map(lambda x:x.view, char_char_data[c].values()))
    print("{}{}".format(c, "%.02f"%( char_char_data[c][cnxt].view/total )), end="")
if __name__ == '__main__':
  main()
