def permutation(string):
	if len(string) <= 1:
		return [string]
	
	perms = permutation(string[1:])
	char = string[0]
	result = []
	
	for perm in perms:
		for i in range(len(perm)+1):
			result.append(perm[:i] + char + perm[i:])

	return result

def permutations(word):
    if len(word)<=1:
        return [word]
 
    #get all permutations of length N-1
    perms=permutations(word[1:])
    char=word[0]
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

print(permutation('Game'))
