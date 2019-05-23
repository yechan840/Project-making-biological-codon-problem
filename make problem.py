import numpy as np

def make_problem(size=10, pre=5,post=5) :
  stop_codon = ['UAA', 'UAG', 'UGA']
  RNA = get_RNA(pre) + 'AUG' + get_RNA2(size-1)  + stop_codon[np.random.choice(3)] + get_RNA(post) + get_RNA(post)
  original = gene(RNA)
  original.show()
  
def get_RNA(size) :
  x = np.random.choice(4,size)
  base_RNA = 'AUGC'
  RNA = ''
  for i in x :
    RNA += base_RNA[i]
    
  for i in range(size-2) :
    sub = RNA[i:i+3]
    while sub == 'AUG' :
      sub = ''.join(np.random.choice(['A','G','C','U'],3))
    RNA = RNA[:i] + sub + RNA[i+3:]
   
  return RNA

def get_RNA2(size) :
  codon = ['UUU', 'UUC', 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG', 'AUU', 
           'AUC', 'AUA', 'AUG', 'GUU', 'GUC', 'GUA', 'GUG', 'UCU', 'UCC', 
           'UCA', 'UCG', 'CCU', 'CCC', 'CCA', 'CCG', 'ACU', 'ACC', 'ACA', 
           'ACG', 'GCU', 'GCC', 'GCA', 'GCG', 'UAU', 'UAC', 'CAU', 'CAC', 
           'CAA', 'CAG', 'AAU', 'AAC', 'AAA', 'AAG', 'GAU', 'GAC', 'GAA', 
           'GAG', 'UGU', 'UGC', 'UGG', 'CGU', 'CGC', 'CGA', 'CGG', 'AGU', 
           'AGC', 'AGA', 'AGG', 'GGU', 'GGC', 'GGA', 'GGG']
  x = np.random.choice(61, size)
  RNA = ''
  for i in x :
    RNA += codon[i]
  return RNA
