import operator

def popularWord(text):
	str = text.replace('\n', '')
	words = str.split(' ')
	wordsTop = {}
	for word in words:
		if word in wordsTop:
			wordsTop[word] += 1
		else:
			wordsTop[word] = 1
	wordsTop = sorted(wordsTop.items(), key = lambda x: x[1], reverse=True)
	if len(wordsTop)>1 and wordsTop[0][1] == wordsTop[1][1]:
		return '---'
	else :
		return wordsTop[0][0]

def MultTable(m, n):
	eqLen = len(str(m*n))
	numLen = len(str(n))

	for i in range(1,n+1):
		string = '_'*(eqLen-len(str(i*m))) + str(i*m)+'='+'_'*(numLen - len(str(i)) + 1) + str(i)+'*'+ '_' +str(m)
		print(string)
	print (len)

def paidStairs(costs, step):
	price = costs[-1]
	i = len(costs)-1
	while i-step >= 0 :
		availableSteps = costs[i-step:i]
		cheapestStep = min(availableSteps)
		price += cheapestStep
		i-= step - availableSteps.index(cheapestStep)

	return price

def PolishNotation(expr):
	try:
		OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
		stack = []
		for token in expr.split(" "):
			if token in OPERATORS:
				op2, op1 = stack.pop(), stack.pop()
				stack.append(OPERATORS[token](op1,op2))
			elif token:
				stack.append(float(token))

		return stack.pop() if len(stack) == 1 else 'ERROR'

	except:
		return 'ERROR'

costs=  [5, 3, 6, 1, 1, 2, 3, 4, 7, 5, 5, 7, 1, 1, 4, 6, 3, 4, 7, 4, 2]
print(paidStairs(costs, 4))
#MultTable(3,100)
print(popularWord('fsdkflsdk kfdmdlk fsdfms fkdsmf skdfm skdfm'))
print(PolishNotation('234 345 456 + + 5 /'))