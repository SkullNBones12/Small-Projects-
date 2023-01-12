#Pig Latin attepmt
phrases1 = [] #English words
phrases2 =[] #Pig Lation Words
constonants = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 
               'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']#single constonants

cCLusters1 = ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr',
             'gh', 'gl', 'gr', 'ng', 'ph', 'pl', 'pr', 'qu', 'sc',
             'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th',
             'tr', 'tw', 'wh', 'wr'] #two letter constonant clusters rule
             
cClusters2 = ['nth', 'sch', 'scr', 'shr', 
             'spl', 'spr', 'squ', 'str', 'thr']#three letter constonant clusters rule

vowels = ['a', 'e', 'i', 'o', 'u']
  
while True:
    print('Hello, I speak pig latin. Please enter a word for me to translate (or press Enter to quit):')
    word = input().lower()    
    if word == '':
        print('Here is your list you asked for!:')
        for i in range(len(phrases1)):
            print(phrases1[i] + '\t\t\t' + phrases2[i])
        break
    elif word[:3] in cClusters2:
        pigLatin3 = word[3:] + word[:3] + 'ay'
        phrases1 = phrases1 + [word]
        phrases2 = phrases2 + [pigLatin3]
        print(pigLatin3)
    elif word[:2] in cCLusters1:
        pigLatin2 = word[2:] + word[:2] + 'ay'
        phrases1 = phrases1 + [word]
        phrases2 = phrases2 + [pigLatin2]
        print(pigLatin2)
    elif word[0] in constonants: 
        pigLatin1 = word[1:] + word[0] + 'ay'
        phrases1 = phrases1 + [word]
        phrases2 = phrases2 + [pigLatin1]
        print(pigLatin1)
    elif word[0] in vowels:
        pigLatin4 = word[1:] + word[0] + 'way'
        phrases1 = phrases1 + [word]
        phrases2 = phrases2 + [pigLatin4]
        print(pigLatin4)