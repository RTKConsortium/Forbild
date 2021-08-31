import re
import os
import numpy as np

f = open('Head', 'w')
with os.popen("gcc -E -x c++ HeadPhantom.pha") as pipe:
    for line in pipe:
        while True:
            (line, n1) = re.subn(r'cos\(([\-+*/0-9\. ]*)\)', lambda m: "%+f" % (np.cos(np.deg2rad(eval(m.group(1))))), line)   # cos
            (line, n2) = re.subn(r'sin\(([\-+*/0-9\. ]*)\)', lambda m: "%+f" % (np.sin(np.deg2rad(eval(m.group(1))))), line)   # sin
            (line, n3) = re.subn(r'sqrt\(([\-+*/0-9\. ]*)\)', lambda m: "%+f" % (np.sqrt(eval(m.group(1)))), line)             # SQRT
            (line, n4) = re.subn(r'([\[+\-]?[0-9\.]+ *[*+\-/]+ *[+\-]?[0-9\.]+)', lambda m: "%+f" % (eval(m.group(1))), line)   # Arithmetic
            (line, n5) = re.subn(r'\( *([\[+-]?[0-9\.]*) *\)', r'\1', line)                                                     # Number in () 
            (line, n6) = re.subn(r'[+] *[\-]', '-', line)                                                                      # +- => -
            (line, n7) = re.subn(r'[\-] *[+]', '-', line)                                                                      # -+ => -
            (line, n8) = re.subn(r'[\-] *[-]', '+', line)                                                                      # -- => +
            if n1+n2+n3+n4+n5+n6+n7+n8 == 0:
                break
        f.write(line)
f.close()
