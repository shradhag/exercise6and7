from sys import argv
script, filename = argv
# filename = "./ex15.txt"     the path

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("? ")

print "Opening the file..."
target = open(filename,"w")
# target is the file object

print "Truncating the file.  Goodbye!"
target.truncate()

print "now I'm going to ask you for three lines."
line1 = str(raw_input("line 1: "))
line2 = str(raw_input("line 2: "))
line3 = str(raw_input("line 3: "))

print "%s, %s, %s" % (line1, line2, line3)
print "I'm going to write these to the file."
target.write(   "%s\n %s\n %s\n" % (line1, line2, line3)  )


print 'And finally, we close it.'
target.close()