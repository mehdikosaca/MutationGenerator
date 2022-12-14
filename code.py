import sys
import pandas as pd

file = sys.argv[1]

interaction_list = []
one_letter_codes = []

aa_dict = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
           'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
           'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
           'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

with open(file, "r") as int_list:
  for line in int_list:
    seperating = line[:3], line[4], line[5:10]
    seperating = [x.strip(' ') for x in seperating]
    interaction_list.append(seperating)

		interaction_list = pd.DataFrame(interaction_list)

		for i in interaction_list[0]:
			one_letter_codes.append(aa_dict[i])

mutation_list = open("mutation_list", "w")	
EvoEF_Mut_Pattern = one_letter_codes + interaction_list[1] + interaction_list[2].astype(str)
EvoEF_Mut_Pattern_Sorted = sorted(EvoEF_Mut_Pattern)
aa = ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
for l in EvoEF_Mut_Pattern_Sorted:
  for j in l[0]:
    for item in aa:
      if j != item:
        print(l,item,";",sep = "",file = mutation_list)
        m = 1
mutation_list.close()
