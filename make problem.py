stop_codon = ['UAA', 'UAG', 'UGA']
def make_problem(size=10, pre=5,post=5, stop=stop_codon[np.random.choice(3)], *mutation) :
  RNA = get_RNA(pre) + 'AUG' + get_RNA2(size-1)  + stop + get_RNA(post)
  #     비번역 부위 + 개시코돈 + 번역부위       + 종결코돈 + 비번역부위
  
  
  original = gene(RNA)
  
  mutated_seq = []
  
  for mut in mutation :
    if len(mut)==3 :
      mut = *mut, stop_codon[np.random.choice(3)]
      #만약 종결코돈이 정해지지 않았다면 임의로 정해준다.
      
    if mut[0] == 'sub' :
      if mut[2] == size : #만약 돌연변이가 일어난 후에도 서열의 길이가 유지되면
        mut_index = np.random.choice(range(pre+3,pre+3*size-mut[1]+1)) #개시코돈 뒤 종결코돈 앞 부분에서 위치 하나를 무작위로 정한다.
        NEW = RNA[:mut_index] + get_RNA(mut[1]) + RNA[mut_index+mut[1]:]  #새롭게 돌연변이된 서열을 만든다.
        mutated_seq.append(NEW)
        
      else : #서열의 길이가 유지되지 않는다면
        if mut[2] < size : #만약 길이가 줄어든다면 번역부위에 종결코돈이 생겨버린 것이다.
          pass
        
        
    elif mut[1] == 'del' : #만약 돌연변이가 삭제라면
      pass
    
    else : #만약 돌연변이가 삽입이라면
      pass
        
        
        
 
  
  
  
def get_RNA(size) :
  x = np.random.choice(4,size)  #염기 4가지 중에서 무작위로 고른다.
  base_RNA = 'AUGC'
  RNA = ''
  for i in x :
    RNA += base_RNA[i]
    
  for i in range(size-2) :
    sub = RNA[i:i+3]
    while sub in ['AUG', 'UAA', 'UAG', 'UGA'] :  #만약 우연히 개시코돈과 같으면 같이 않을 때까지
      sub = ''.join(np.random.choice(['A','G','C','U'],3))  #무작위로 다시 뽑는다.
    RNA = RNA[:i] + sub + RNA[i+3:]
    
  
  return RNA
  
  
def get_RNA2(size) :
  codon = ['UUU', 'UUC', 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG', 'AUU', 
           'AUC', 'AUA', 'AUG', 'GUU', 'GUC', 'GUA', 'GUG', 'UCU', 'UCC', 
           'UCA', 'UCG', 'CCU', 'CCC', 'CCA', 'CCG', 'ACU', 'ACC', 'ACA', 
           'ACG', 'GCU', 'GCC', 'GCA', 'GCG', 'UAU', 'UAC', 'CAU', 'CAC', 
           'CAA', 'CAG', 'AAU', 'AAC', 'AAA', 'AAG', 'GAU', 'GAC', 'GAA', 
           'GAG', 'UGU', 'UGC', 'UGG', 'CGU', 'CGC', 'CGA', 'CGG', 'AGU', 
           'AGC', 'AGA', 'AGG', 'GGU', 'GGC', 'GGA', 'GGG'] #종결코돈을 제외한 모든 코돈
  x = np.random.choice(61, size)  #무작위로 고른다.
  RNA = ''
  for i in x :
    RNA += codon[i]
  return RNA
