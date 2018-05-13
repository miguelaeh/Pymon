from pysnmp.hlapi import *


##########################################################################3
def snmp_getBulk(ip,community,mib,nonRepeaters,maxRepetitions,introducidos):

	puerto = 161
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

	if errorIndication:
	    print(errorIndication)
	elif errorStatus:
	    print('%s at %s' % (errorStatus.prettyPrint(),
	                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
	
	return varBinds
##########################################################################3

ip = raw_input("Introduzca IP: ")
community = raw_input("Introduzca community: ")
mib = raw_input("Introduzca nombre de la MIB: ") #la mib es el oid de la mib
nonRepeaters = raw_input("Non-Repeaters: ")
maxRepetitions = raw_input("Max-Repetitions: ")
introducidos = raw_input("Introduzca Id de los objetos separados por comas: ")


##llamamos e imprimimos
varBinds = snmp_getBulk (ip,community,mib,nonRepeaters,maxRepetitions,introducidos)

for varBind in varBinds:
    print(' = '.join([x.prettyPrint() for x in varBind]))