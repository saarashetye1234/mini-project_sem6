
import sys

file1 = sys.argv[1]+'.ssv'
file2 = sys.argv[1]+'.csv'

input_file = open(file1, 'r')
output_file = open(file2, 'w')

input_record = 0
for line in input_file:
    if line.strip():
        input_record += 1
        line = line.replace(" ", ",")
        output_file.write(line)

input_file.close()
output_file.close()

print ('\n%i records transferred from %s to %s') % (input_record, file1, file2)

