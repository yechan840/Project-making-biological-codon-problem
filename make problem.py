import numpy as np

def get_RNA(size) :
  x = np.random.choice(4,size)
  base_RNA = 'AUGC'
  RNA = ''
  for i in x :
    RNA += base_RNA[i]
  return RNA
  
def make_problem(size=10, pre=5,post=5) :
  stop_codon = ['UAA', 'UAG', 'UGA']
  RNA = get_RNA(pre) + 'AUG' + get_RNA(3*(size-1)) + get_RNA(pre) + stop_codon[np.random.choice(3)] + get_RNA(post)
  original = gene(RNA)
  original.show()
