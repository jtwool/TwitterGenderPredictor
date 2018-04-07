import happyfuntokenizing as hftknz
import csv
from math import sin

class GndrPrdct:
  '''Takes text and provides gender prediction (1 is female, 0 is male)'''
  def __init__(self,fp="gender_lex.csv"):
    self.tknzr = hftknz.Tokenizer(preserve_case=False)
    self.weights = dict()
    with open(fp) as f:
      rdr = csv.reader(f)
      rdr.__next__()
      for r in rdr:
        self.weights[r[0]]=float(r[1])

  def weigh(self,token,tokens):
    w = self.weights.get(token,0)
    if w == 0:
      return 0
    else:
      return w*tokens.count(token)/len(tokens)
  
  def predict_gender(self,txt):
    tkns = list(self.tknzr.tokenize(txt))
    wts = sum([self.weigh(t,tkns) for t in set(tkns)])
    p = sin(-0.06724152+wts)
    if p >= 0:
      # Female
      return 1
    else: 
      # Male
      return 0
