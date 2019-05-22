#Version4

'''
반대 방향의 서열도 출력할 수 있게 한다.
간단한 버그 수정
출력된 결과를 통해 버그가 있었다는 것을 알 수 있었다.
'''

base_DNA = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
base_RNA = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
codon = {'UUU':'phe', 'UUC':'phe', 'UUA':'leu', 'UUG':'leu', 'CUU':'leu', 'CUC':'leu', 'CUA':'leu', 'CUG':'leu', \
        'AUU':'ile', 'AUC':'ile', 'AUA':'ile', 'AUG':'met', 'GUU':'val', 'GUC':'val', 'GUA':'val', 'GUG':'val', \
        'UCU':'ser', }

class gene :
  def __init__(self, seq) :

    self.DNA5_3 = ''
    self.DNA3_5 = ''
    self.RNA5_3 = seq
    self.RNA3_5 = ''
    self.amino = ''
      
    for base in self.RNA5_3 :
      self.RNA3_5 += base_RNA[base]
    
    for base in self.RNA5_3 :
      if base != 'U' :
        self.DNA5_3 += base
      else :
        self.DNA5_3 += 'T'
        
    for base in self.DNA5_3 :
      self.DNA3_5 += base_DNA[base]
      
      
    for i in range(len(self.RNA5_3)-3) :
      if self.RNA5_3[i:i+3] == 'AUG' :
        break
    start = i
    
    for i in range(start, len(self.RNA5_3), 3) :
      if self.RNA5_3[i:i+3] in ['UAG', 'UAA', 'UGA'] :
        break
      self.amino += ' '+codon[self.RNA5_3[i:i+3]]
      
    self.amino = self.amino[1:]
   
     
        
  def show(self) :
    print('DNA 5-3',self.DNA5_3)
    print('DNA 3-5',self.DNA3_5, ' 주형가닥')
    print('RNA 5-3',self.RNA5_3)
    print('RNA 3-5',self.RNA3_5)
    print('amino', self.amino)
    print()
    print('DNA 5-3',self.DNA3_5[::-1],' 주형가닥')
    print('DNA 3-5',self.DNA5_3[::-1])
    print('RNA 5-3',self.RNA3_5[::-1])
    print('RNA 3-5',self.RNA5_3[::-1])
