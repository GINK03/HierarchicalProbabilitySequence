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


WINDOWS = [1,2,3,4,5]

win_char_data = {}
def main():
  contexts = ""
  files = glob.glob('data/*.utf8') 
  for file in files:
    with open(file, "r") as f:
      contexts += f.read()

  for start in range(len(contexts) - max(WINDOWS) ):
    target = contexts[start:]

    for window in WINDOWS:
      """ crop window """
      win  = target[:window]
      char = target[window]
      if win_char_data.get(win) is None:
        win_char_data[win] = { }
      if win_char_data[win].get(char) is None:
        win_char_data[win][char] = CharData()
      win_char_data[win][char].view += 1.
  """ total_viewを構築 """
  
  win_dist = {}
  for win, char_data in win_char_data.items():
    total = sum( map(lambda x:x.view, char_data.values() ) )
    dist  = [v.view/total for v in char_data.values()]
    
    win_dist[win] = dist
  for win, dist in sorted(win_dist.items(), key=lambda x:len(x[1])*-1):
    #print(win, dist)
    ...

  """ search task """
  i = 0
  while i < len(contexts) - max(WINDOWS):
    match = False
    # エンピリカルによい
    for w in sorted(WINDOWS, key=lambda x:x*-1):
      ev = contexts[i:i+w] 
      if len(win_dist.get(ev)) != 1:
        print(ev, "/", end="<%d>"%(len((win_dist.get(ev)))) ) 
        match = True
        break
    """
    buff = []
    for w in sorted(WINDOWS, key=lambda x:x*-1):
      ev = contexts[i:i+w] 
      len(win_dist.get(ev))
      buff.append( (ev, win_dist.get(ev)) )
      print(buff)
    """
    print( i, end="")
    if match == False:
      print(contexts[i], end=",")
      #print(ev, len(win_dist[ev]))
    i += w 


if __name__ == '__main__':
  main()
