from pysnmp.hlapi import *


puerto = 161

ip = raw_input("Introduzca IP: ")
community = raw_input("Introduzca community: ")
mib = raw_input("Introduzca nombre de la MIB: ") #la mib es el oid de la mib
print("Ìntroduzca el numero de objetos total a pedir:")
nonRepeaters = raw_input("Non-Repeaters: ")
maxRepetitions = raw_input("Max-Repetitions: ")

introducidos = raw_input("Introduzca Id de los objetos separados por comas: ")
objetos = introducidos.split(",")

oidsObjetos = []
for x in xrange(1,len(objetos)):
	oidsObjetos += ObjectType(ObjectIdentity(mib, objetos[x]).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'))

g = bulkCmd(SnmpEngine(),
             CommunityData(community),
             UdpTransportTarget((ip,puerto)),
             ContextData(),
             nonRepeaters, maxRepetitions,
             oidsObjetos)

errorIndication, errorStatus, errorIndex, varBinds = next(g)

#g.send( [ ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets')) ] ) #La funcion send permite repetir todo lo anterior cambiando solo lo que le pasamos

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))