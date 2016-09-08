lines = open('subtag.xml', 'r').readlines()

lines_set = set(lines)

out  = open('subtag.xml', 'w')

for line in lines_set:
    out.write(line)