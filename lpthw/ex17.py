from sys import argv

script, from_file = argv

print "Copying from %s to " % (from_file)

in_file = open(from_file)


print type(in_file)
for i in in_file:
    print '%r' % i
print in_file.tell()
in_file.seek(0)
print in_file.tell()
print '%r' % in_file.readline()
print in_file.tell()
print in_file.readline()

print in_file.tell()
print in_file.readline()
print in_file.tell()
