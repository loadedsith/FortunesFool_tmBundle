import csv

txt_file = r"animals.txt"

# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect
in_txt = open(txt_file, "r")
string = ""
for line in in_txt:
    line = line.rstrip('\n')
    string += '"'+line+'", '
#wr = csv.writer( in_txt, quoting=csv.QUOTE_ALL)



print string