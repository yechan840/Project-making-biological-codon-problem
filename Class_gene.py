#version1 5 / 16


base_DNA = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
base_RNA = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}

class gene :
  def __init__(self, seq, d5_3 = True, cate = 'DNA') :

    self.DNA5_3 = ''
    self.DNA3_5 = ''
    self.RNA5_3 = ''
    self.RNA3_5 = ''

    if cate == 'DNA':
      if d5_3 :
        self.DNA5_3 = seq

        for base in self.DNA5_3 :
          self.DNA3_5 += base_DNA[base]
      
      else :
        self.DNA3_5 = seq
        
        for base in self.DNA3_5 :
          self.DNA5_3 += base_DNA[base]

      for base in self.DNA3_5 :
        if base != 'T' :
          self.RNA3_5 += base
        else :
          self.RNA3_5 += 'U'

      for base in self.RNA3_5 :
        self.RNA5_3 += base_RNA[base]
        
     
        
        
        
  def show(self) :
    print(self.DNA5_3)
    print(self.DNA3_5)
    print(self.RNA5_3)
    print(self.RNA3_5)
    
