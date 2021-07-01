# python3
import sys

def InverseBWT(bwt):
    #initalize amounts at 0
    amt = {}
    for c in '$ACGT':
        amt[c] = 0
    
    #find out rank of each index
    rank = []
    for c in bwt:
        rank.append(amt[c])
        amt[c] += 1

    #get starting indexes, amount dictionary is now the starting index (si) for each character
    prev = '$'
    for c in 'ACGT':
        amt[c] += amt[prev]
        prev = c
    
    ahead = 'T'
    for c in 'GCA$':
        amt[ahead] = amt[c]
        ahead = c
    amt['$'] = 0
    si = amt
    
    #construct string
    char_list = []
    char_list.append('$')
    r = 0
    c=''
    while(bwt[r] != '$'):
        c = bwt[r]
        char_list.append(c)
        r = rank[r] + si[c]
        
    char_list.reverse()
    return ''.join(char_list)


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))