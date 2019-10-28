from random import randint

def ask():
	ans = ['go for it', 'don\'t you dare', 'no', 'yes', 'absolutely','absolutely not','why not?','please do not','i do not know','try again','are you crazy?','would not be my first choice', 'would be the end of you','great idea','you should','not sure','maybe, maybe not', 'I don\'t wanna talk about it']
	print(ans[randint(0, len(ans) - 1)])
	return 

	
def mainloop(query):
	if query == 'q':
		exit()
	elif ('?' in query) and len(query) > 3:
		ask()
	else:
		print('Are you sure that\'s a question? Questions end with a question mark (?)')
	query = input('\nAsk your question and you shall get the answer:\n')
	mainloop(query)


mainloop(input('Ask your question and you shall get the answer:\n'))
