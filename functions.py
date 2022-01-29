def mirror(txt, a):
	rt_txt = ""
	for i in range(a+1) : 
		rt_txt += txt[i]
	for i in range(a, -1, -1) :
		rt_txt += txt[i]
	return rt_txt