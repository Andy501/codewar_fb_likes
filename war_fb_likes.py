


def liker(t_up):
	
	
	if len(t_up)== 0:
	    sentence_string = 'no one likes this'
	    finalized_string = (sentence_string)
	elif len(t_up)== 1:
	    a = t_up[0]#expressed this way to build raw string
	    sentence_string = ('{} likes this'.format(a))
	    finalized_string = (sentence_string)
	elif len(t_up) ==2:
	    a,b = t_up
	    sentence_string = ('{} and {} like this'.format (a,b))
	    finalized_string = (sentence_string)
	elif len(t_up) ==3:
	    a,b,c=t_up
	    sentence_string = ('{}, {} and {} like this'.format(a,b,c))
	    finalized_string = (sentence_string)
	elif len(t_up) >=4:
	    a,b,*c=t_up
	    liked_remainder  = (len(t_up)) - 2
	    liked_remainder = str(liked_remainder)
	    sentence_string = ('{}, {} and {} others like this'.format(a,b,liked_remainder))
	    finalized_string = (sentence_string)

	#print(liking_peeps)
	return finalized_string



_up5=['blake','whalen','vivean','kata','emo1992','blake','whalen','vivean','kata','emo1992','blake','whalen','vivean','kata','emo1992']
_up3=['blake','whalen','vivean']
_up2=['blake', 'whalen']
_up1=['rodney']
_up0=[]

likes = liker(_up1)
print(likes)

#https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python