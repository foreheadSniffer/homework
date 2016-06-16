def printObjectProps(object):
	for property in dir(object):
		if not property.startswith('_'):
			print (property)

def _getInputArray():
	return [int(x) for x in input().split(',')]

def findSecondMax():
	_secondMaxMethod(_getInputArray())
def _secondMaxMethod(array):
	firstMax = array[0]
	secondMax = None
	for key in array:
		if (key > firstMax):
			secondMax = firstMax
			firstMax = key
		elif not firstMax==key and (secondMax is None or secondMax < key):
			secondMax = key
	if secondMax is None:
		print('NO')
	else:
		print(secondMax)

def checkIfParallel():
	print(_parallel(_getInputArray()))
def _parallel(array):
	def _getAngleSin(x1,y1,x2,y2):
		return (y1-y2)/(x1-x2)
	if len(array) == 8:
		return 'YES' if _getAngleSin(array[0],array[1],array[2],array[3]) == _getAngleSin(array[4], array[5], array[6], array[7]) else 'NO'
	else: 
		raise Exception('Wrong number of parameters')

def getSmallestRepetitiveSubstring(str):
    ss = ''
    for j in range(int(len(str)/2 +1)) :
        ss+=str[j]
        substring = ''
        for i in range(int(len(str)/len(ss))):
            substring+=ss
        if str == substring and len(str) != len(ss):
            return (int(len(str)/len(ss)))

    return 1
print (getSmallestRepetitiveSubstring('abcabcabcabc'))
#print(_parallel([1,2,7,14,8,8,18,28]))
# checkIfParallel()
# printObjectProps(1)
# findSecondMax()