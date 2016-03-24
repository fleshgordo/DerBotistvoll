import random, time

print "hello world"

while True:
	zufallszahl = random.randint(1,6)
	# pseudocode: ist die zufallszahl 4, dann tue das ....
	if zufallszahl == 4:
		print "wow, es ist die magische vier"
	else:
		print zufallszahl
	print "---------------"
	time.sleep(1)