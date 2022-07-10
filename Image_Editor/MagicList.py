class MagicList :
	def __init__(self):
		self.data = [0]
	
	def findMin(self):
		M = self.data
		''' you need to find and return the smallest
			element in MagicList M.
			Write your code after this comment.
		'''
		return M[1]
	
	def insert(self, E):
		M = self.data
		''' you need to insert E in MagicList M, so that
			properties of the MagicList are satisfied. 
			Return M after inserting E into M.
			Write your code after this comment.
		'''
		
		if(len(M)==1):
			return M.append(E)
		else:
			n=len(M)
			M.append(E)
			while(n>1):
				i=n//2
				if(M[i]>M[n]):
					(M[i],M[n])=(M[n],M[i])
					n=n//2
				else:
					return M
		
	
	def deleteMin(self):
		M = self.data
		''' you need to delete the minimum element in
			MagicList M, so that properties of the MagicList
			are satisfied. Return M after deleting the 
			minimum element.
			Write your code after this comment.
		'''
			
		n=len(M)-1
		(M[1],M[n])=(M[n],M[1])
		M.pop()
		n=1
		if(len(M)>(2*n+1)):
			while((2*n +1)<len(M)):
				if(M[n]>M[2*n]):
					if(M[2*n]<M[2*n +1]):
						(M[n],M[2*n])=(M[2*n],M[n])
						n=2*n
					else:
						(M[n],M[2*n +1])=(M[2*n +1],M[n])
						n=2*n +1
				else:
					if(M[n]>M[2*(n) +1]):
						(M[n],M[2*(n)+1])=(M[2*(n) +1],M[n])
						n=2*(n) +1
					else:
						return M
		else:
			(M[n],M[2*n])=(M[2*n],M[n])
			return M
	

		


def K_sum(L, K):
	''' you need to find the sum of smallest K elements
		of L using a MagicList. Return the sum.
		Write your code after this comment.
	'''
	for i in L:
		M.insert(i)
	r=0	
	for j in range(K):
		r=r+M.findMin()
		M.deleteMin()
		
	return r
		
	

	
if __name__ == "__main__" :
	'''Here are a few test cases'''
	
	'''insert and findMin'''
	M = MagicList()
	M.insert(4)
	M.insert(3)
	M.insert(5)
	x = M.findMin()
	if x == 3 :
		print("testcase 1 : Passed")
	else :
		print("testcase 1 : Failed")
		
	'''deleteMin and findMin'''
	M.deleteMin()
	x = M.findMin()
	if x == 4:
		print("testcase 2 : Passed")
	else :
		print("testcase 2 : Failed")
		
	'''k-sum'''
	L = [2,5,8,3,6,1,0,9,4]
	K = 4
	x = K_sum(L,K)
	if x == 6 :
		print("testcase 3 : Passed")
	else :
		print("testcase 3 : Failed")