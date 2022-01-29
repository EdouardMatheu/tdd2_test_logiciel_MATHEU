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

def deriv2(l):
	interval = 1.0
	temp_l = []
	rt_l = []
	if len(l) < 3:
		return None
	for e in l :
		if type(e) != float:
			return None
	for i in range(len(l)-1):
		temp_l.append((l[i+1]-l[i])/interval)
	for i in range(len(temp_l)-1):
		rt_l.append((temp_l[i+1]-temp_l[i])/interval)

	return rt_l

def derivapprox(f, ord, pt):
	h = 0.00000001
	fp = (f(pt+h)-f(pt))/h
	if ord == 0.0 :
		return 0.0
	if ord < 0.0 or ord > 1.0:
		return None
	rst = fp % ord
	rt_f = fp - rst
	if(rst >= 5*ord*0.1):
		rt_f += ord
	return rt_f

def f_x2(x):
	return x**2

def f_minus2x3(x):
	return -2*(x**3) 