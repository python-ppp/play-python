import turtle as t
total = 10
x = 360 / total
y = 120
for i in range(total):
	if i % 2 == 0:
		t.color('red')
	else :
		t.color('pink')
	t.begin_fill()
	t.forward(y)
	t.left(x)
	t.forward(y)
	t.left(180-x)
	t.forward(y)
	t.left(x)
	t.forward(y)
	t.left(180-x)
	t.end_fill()
	t.left(x)
t.done()

