N=529
NBIN=bin(N)[2:]
count=0
j=0
countlist=[]
for i in range(len(NBIN)-1):
	i+=1
	if NBIN[i]=='0':
		count+=1
	else:
		countlist.append(count)
		count=0
		j+=1
if countlist:
	return max(countlist)
else:
	return 0