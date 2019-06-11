stop_codon_mut = {'UAG':['AAG','GAG','CAG','UUG','UCG','UGG','UAU','UAC'],
                 'UGA':['AGA','CGA','GGA','UCA','UUA','UGC','UGU','UGG'],
                 'UAA':['AAA','CAA','GAA','UCA','UUA','UAC','UAU'] }

stop_codon = ['UAA', 'UAG', 'UGA']
def make_problem(*mutation,size=10, pre=5,post=5, stop=stop_codon[np.random.choice(3)]) :
  
    pre_RNA = get_RNA(pre) + 'AUG'
    post_RNA = stop + get_RNA(1) + stop_codon[np.random.choice(3)] + get_RNA(1) + stop_codon[np.random.choice(3)] + get_RNA(1) + stop_codon[np.random.choice(3)] + get_RNA(post)
    RNA = get_RNA2(size-1)
  
  
    mutated_RNAs = []
  
    cnt = 0
    pos_list = np.random.permutation(np.arange(size-1))
    
    stop_list = []
  
    for mut in mutation :
        if mut[0]=='sub' and mut[2]==1 :
            stop = stop_codon[np.random.choice(3)]
            RNA = RNA[:3*pos_list[cnt]] + np.random.choice(stop_codon_mut[stop]) + RNA[3*pos_list[cnt]+3:]
            stop_list.append(stop)
            
        cnt += 1
    
    cnt = 0
  
    for mut in mutation :
      
        if mut[0] == 'sub' : #만약 돌연변이가 치환이라면
            if mut[2] == 0 : #길이 변화가 일어나지 않는다면
                pos = pos_list[cnt]*3 + np.random.choice(2)
                
                sub = RNA[pos:pos+mut[1]]
                
                while True :
                    sub2 = get_RNA(mut[1])
                    if all([a!=b for a, b in zip(sub, sub2)]) :
                        break
                
                mutated_RNA = pre_RNA + RNA[:pos] + sub2 + RNA[pos+mut[1]:] + post_RNA
        
            elif mut[2] == 1: #길이 수축이 일어나면
                stop = stop_codon[np.random.choice(3)]
                mutated_RNA = pre_RNA + RNA[:3*pos_list[cnt]] + stop_list[0] + RNA[3*pos_list[cnt]+3:] + post_RNA
                stop_list.pop(0)
        
            else : #길이 증가가 일어나면
    
                stop = post_RNA[:3]
                while True :
                    pos = np.random.choice(3)
                    stop2 = stop[:pos] + get_RNA(mut[1]) + stop[pos+mut[1]:]
                    if stop2 not in stop_codon :
                        break
            
                mutated_RNA = pre_RNA + RNA + stop2 + post_RNA[3:]
        
        
        elif mut[0] == 'del' : #만약 돌연변이가 삭제라면
            pos = pos_list[cnt]*3 + np.random.choice(3)
            mutated_RNA = pre_RNA + RNA[:pos] + RNA[pos+mut[1]:] + post_RNA
      
    
        else : #만약 돌연변이가 삽입이라면
            pos = pos_list[cnt]*3 + np.random.choice(3)
            mutated_RNA = pre_RNA + RNA[:pos] + get_RNA(mut[1]) + RNA[pos:] + post_RNA
      
      
        mutated_RNAs.append(mutated_RNA)
        cnt += 1
    
    original = pre_RNA + RNA + post_RNA
    gene(original).show()
  
    for mutated_RNA, mut, pos in zip(mutated_RNAs, mutation, pos_list) :
        print(mut[0], end=' ')
        if len(mut)==3 :
            if mut[2]==2 :
                print(size+1)
            else :
                print(pos+2)
        else :
            print(pos+2)
        gene(mutated_RNA).show()
        
        
        
 
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
