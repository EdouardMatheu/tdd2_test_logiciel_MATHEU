def mirror(txt, a):
	rt_txt = ""
	for i in range(a+1) : 
		rt_txt += txt[i]
	for i in range(a, -1, -1) :
		rt_txt += txt[i]
	return rt_txt

def deriv(l):
	interval = 1.0
	rt_l = []
	if len(l) < 2:
		return None
	for e in l :
		if type(e) != float:
			return None
	for i in range(len(l)-1):
		rt_l.append((l[i+1]-l[i])/interval)

	return rt_l