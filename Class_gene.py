#Version6
def gene_express(name, seq, start, final, lord=False) :
    if lord :
        print(name,seq[:start], ' '.join([seq[i:i+3] for i in range(start, final, 3)]), seq[final:], '주형가닥')
    else :
        print(name,seq[:start], ' '.join([seq[i:i+3] for i in range(start, final, 3)]), seq[final:])
    


class gene :
    def __init__(self, seq) :
    
        base_DNA = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        base_RNA = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
        codon = {'UUU':'phe', 'UUC':'phe', 'UUA':'leu', 'UUG':'leu', 'CUU':'leu', 'CUC':'leu', 
             'CUA':'leu', 'CUG':'leu', \
            'AUU':'ile', 'AUC':'ile', 'AUA':'ile', 'AUG':'met', 'GUU':'val', 
             'GUC':'val', 'GUA':'val', 'GUG':'val', \
            'UCU':'ser','UCC':'ser','UCA':'ser','UCG':'ser','CCU':'Pro','CCC':'Pro',
            'CCA':'Pro', 'CCG':'Pro','ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr',
            'GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala', 'UAU':'Tyr','UAC':'Tyr',
            'CAU':'His','CAC':'His','CAA':'Gln','CAG':'Gln','AAU':'Asn','AAC':'Asn',
            'AAA':'Lys','AAG':'Lys','GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu',
            'UGU':'Cys','UGC':'Cys','UGG':'Trp','CGU':'Arg','CGC':'Arg','CGA':'Arg',
            'CGG':'Arg','AGU':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg', 'GGU':'Gly',
            'GGC':'Gly','GGA':'Gly','GGG':'Gly'}

        self.DNA5_3 = ''
        self.DNA3_5 = ''
        self.RNA5_3 = seq
        self.RNA3_5 = ''
        self.amino = ''
        self.len = len(seq)
      
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
                start = i
                break
            
        self.start = i
    
        for i in range(start, len(self.RNA5_3), 3) :
            if self.RNA5_3[i:i+3] in ['UAG', 'UAA', 'UGA'] :
                self.amino += " "+self.RNA5_3[i:i+3]
                self.final = i+3
                break
            self.amino += ' '+codon[self.RNA5_3[i:i+3]]
      
        self.amino = self.amino[1:]
        self.amino_len = len(self.amino.split())
        self.amino_dict = {}
        for amino_acid in self.amino.split()[:-1] :
            if amino_acid in self.amino_dict :
                self.amino_dict[amino_acid] += 1
            else :
                self.amino_dict[amino_acid] = 1
   

     
        
    def show(self) :
        
        gene_express('DNA 5-3', self.DNA5_3, self.start, self.final)
        gene_express('DNA 3-5', self.DNA3_5, self.start, self.final, True)
        gene_express('RNA 5-3', self.RNA5_3, self.start, self.final)
        gene_express('RNA 3-5', self.RNA3_5, self.start, self.final)
        print('amino', self.amino[:-3], self.amino_len)
        print(self.amino_dict)
        print("STOP CODON", self.amino[-3:])
        print()
        
        print('Reverse Sequence')
        gene_express('DNA 5-3',self.DNA3_5[::-1], self.len-self.final, self.len-self.start, True)
        gene_express('DNA 3-5',self.DNA5_3[::-1], self.len-self.final, self.len-self.start)
        gene_express('RNA 5-3',self.RNA3_5[::-1], self.len-self.final, self.len-self.start)
        gene_express('RNA 3-5',self.RNA5_3[::-1], self.len-self.final, self.len-self.start)
        print()
