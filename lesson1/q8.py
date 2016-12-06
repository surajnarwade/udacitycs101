x=3.64159
p=str(x)
if int(p[p.find('.')+1])>=5:
 print int(p[:p.find('.')])+1
else:
 print int(x)
