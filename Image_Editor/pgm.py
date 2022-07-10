# name: File path of the pgm image file
# Output is a 2D list of integers
def readpgm(name):
	image = []
	with open(name) as f:
		lines = list(f.readlines())
		if len(lines) < 3:
			print("Wrong Image Format\n")
			exit(0)

		count = 0
		width = 0
		height = 0
		for line in lines:
			if line[0] == '#':
				continue

			if count == 0:
				if line.strip() != 'P2':
					print("Wrong Image Type\n")
					exit(0)
				count += 1
				continue

			if count == 1:
				dimensions = line.strip().split(' ')
				print(dimensions)
				width = dimensions[0]
				height = dimensions[1]
				count += 1
				continue

			if count == 2:	
				allowable_max = int(line.strip())
				if allowable_max != 255:
					print("Wrong max allowable value in the image\n")
					exit(0)
				count += 1
				continue

			data = line.strip().split()
			data = [int(d) for d in data]
			image.append(data)
	return image	

# img is the 2D list of integers
# file is the output file path
def writepgm(img, file):
	with open(file, 'w') as fout:
		if len(img) == 0:
			pgmHeader = 'p2\n0 0\n255\n'
		else:
			pgmHeader = 'P2\n' + str(len(img[0])) + ' ' + str(len(img)) + '\n255\n'
			fout.write(pgmHeader)
			line = ''
			for i in img:
				for j in i:
					line += str(j) + ' '
				line += '\n'
			fout.write(line)

			
########## Function Calls ##########
x = readpgm('test.pgm')			# test.pgm is the image present in the same working directory
def averagefilter(A):
	n=len(A)
	m=len(A[0])
	I=[[0 for column in range(m)] for row in range(n)]
	i=1
	while(i<n-1):
		j=1
		while(j<m-1):
			I[i][j]=(A[i-1][j-1]+A[i-1][j]+A[i-1][j+1]+A[i][j-1]+A[i][j]+A[i][j+1]+A[i+1][j-1]+ A[i+1][j]+A[i+1][j+1])//9
			j+=1
		i+=1
	k=0
	while(k<n):
		I[k][0]=A[k][0]
		I[k][m-1]=A[k][m-1]
		k+=1
	l=0
	while(l<m):
		I[0][l]=A[0][l]
		I[n-1][l]=A[n-1][l]
		l+=1
	return I

	

x=averagefilter(x)
print(x)
writepgm(x, 'test_o.pgm')		# x is the image to output and test_o.pgm is the image output in the same working directory
###################################