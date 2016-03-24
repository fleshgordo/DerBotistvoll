import random, time

print "hello world"

while True:
	zufallszahl = random.randint(1,4)
	# pseudocode: ist die zufallszahl 4, dann tue das ....
	if zufallszahl == 1:
		print "wow, es ist die magische eins"
	elif zufallszahl == 2:
		print "wow, d'zahl isch zwai"
	elif zufallszahl == 3:
		print "druuuuuueeeee"
	elif zufallszahl == 4:
		print "vier"
	else:
		print "weder 1, 2, 3, 4"
	print "---------------"
	time.sleep(5)