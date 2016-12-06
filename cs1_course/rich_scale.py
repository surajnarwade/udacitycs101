richter=input('Please enter a Richter slace value')
#energy in joules
energy=10**((1.5*richter)+4.8)
#energy in tons
energy_in_ton=energy/(4.184*(10**9))
print 'Richter scale value:',richter
print 'Equivalce in joules:',energy
print 'equivalence in tons of TNT:',energy_in_ton
