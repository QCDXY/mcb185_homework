def percent_id(s1,s2):
	match = 0
	for index,char in enumerate(s1):
		if s1[index]==s2[index]:
			match += 1
	return match / len(s1)
	

print(percent_id('ATCG','ATGC'))