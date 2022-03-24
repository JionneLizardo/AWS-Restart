#!/bin/python

code = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

a = code[0:24]
b = code[24:54]
c = code[54:89]
d = code[89:len(code)]

print("Amino accids : ", len(code))
print("lsinsulin: {} ({})".format(a, len(a)))
print("binsulin: {} ({})".format(b, len(b)))
print("cinsulin: {} ({})".format(c, len(c)))
print("ainsulin: {} ({})".format(d, len(d)))