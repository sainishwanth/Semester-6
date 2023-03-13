def sin(ws):
    #return 1/(1+np.exp(-ws))
    if ws > k:
        return 1
    else:
        return 0
def update(x , w):
    global ws
    er = n*(t-o)
    for i in range(len(w)):
        w[i] = w[i] + er*x[i]
        print(w , x)
    for i,j in zip(x,w):
        print(w , x)
        ws += i*j
x = [ -1.0 , 1.0 , 0.5 , -1]
w = [ 1.0 , -1.0, 0 , 0.5]
t = 1
n = 0.5
ws = 0
k = 0

for i,j in zip(x,w):
    ws += i*j
q = True
while q:
    o = sin(ws)
    print(ws)
    if t == o:
        print("output is " ,t)
        q = False

    else:
        update(x , w)