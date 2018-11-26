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
###output###
#['Autry', 'uAtry', 'utAry', 'utrAy', 'utryA', 'Atury', 'tAury', 'tuAry', 'turAy', 'turyA', 'Atruy', 'tAruy', 'trAuy', 'truAy', 'truyA', 'Atryu', 'tAryu', 'trAyu', 'tryAu', 'tryuA', 'Aurty', 'uArty', 'urAty', 'urtAy', 'urtyA', 'Aruty', 'rAuty', 'ruAty', 'rutAy', 'rutyA', 'Artuy', 'rAtuy', 'rtAuy', 'rtuAy', 'rtuyA', 'Artyu', 'rAtyu', 'rtAyu', 'rtyAu', 'rtyuA', 'Auryt', 'uAryt', 'urAyt', 'uryAt', 'urytA', 'Aruyt', 'rAuyt', 'ruAyt', 'ruyAt', 'ruytA', 'Aryut', 'rAyut', 'ryAut', 'ryuAt', 'ryutA', 'Arytu', 'rAytu', 'ryAtu', 'rytAu', 'rytuA', 'Autyr', 'uAtyr', 'utAyr', 'utyAr', 'utyrA', 'Atuyr', 'tAuyr', 'tuAyr', 'tuyAr', 'tuyrA', 'Atyur', 'tAyur', 'tyAur', 'tyuAr', 'tyurA', 'Atyru', 'tAyru', 'tyAru', 'tyrAu', 'tyruA', 'Auytr', 'uAytr', 'uyAtr', 'uytAr', 'uytrA', 'Ayutr', 'yAutr', 'yuAtr', 'yutAr', 'yutrA', 'Aytur', 'yAtur', 'ytAur', 'ytuAr', 'yturA', 'Aytru', 'yAtru', 'ytAru', 'ytrAu', 'ytruA', 'Auyrt', 'uAyrt', 'uyArt', 'uyrAt', 'uyrtA', 'Ayurt', 'yAurt', 'yuArt', 'yurAt', 'yurtA', 'Ayrut', 'yArut', 'yrAut', 'yruAt', 'yrutA', 'Ayrtu', 'yArtu', 'yrAtu', 'yrtAu', 'yrtuA']
        
        
    

