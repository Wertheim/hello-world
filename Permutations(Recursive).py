def get_permutations(string):
    #base case
    
    if len(string) == 1:
        return string

    #declare return list and
    #recurse without the first letter
    plist = []
    for p in get_permutations(string[1:]):
        
        #for each permutation create the new string
        #by shifting position of letter
        for i in range(len(string)):
            plist.append(p[:i] + string[0:1] +p[i:]) 

    return plist


print get_permutations('Autry')
        
        
    

