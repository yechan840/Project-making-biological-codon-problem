#version2 5 / 16

'''
주형가닥으로부터 아미노산 서열을 알아내서 속성으로 설정하는 기능이 추가되었다.
.show()에서 어떤 서열인지도 같이 출력하게 하였다.
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
    self.RNA5_3 = ''
    self.RNA3_5 = ''
    self.amino = ''


    self.DNA5_3 = seq

    for base in self.DNA5_3 :
      self.DNA3_5 += base_DNA[base]

    for base in self.DNA3_5 :
      if base != 'T' :
        self.RNA3_5 += base
      else :
        self.RNA3_5 += 'U'

    for base in self.RNA3_5 :
      self.RNA5_3 += base_RNA[base]
    
    
        
    
        
     
        
  def show(self) :
    print('DNA 5-3',self.DNA5_3)
    print('DNA 3-5', self.DNA3_5)
    print('RNA 5-3',self.RNA5_3)
    print('RNA 3-5',self.RNA3_5)
    
