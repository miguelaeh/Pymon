from pysnmp.hlapi import *

##########################################################################3
def snmp_crear_evento(ip,community,eventDescription,eventType,eventCommunity,eventOwner,eventIndex):

	mib = 'RMON-MIB'
	puerto = 161

	errorIndication, errorStatus, errorIndex, varBinds = next(
			setCmd(SnmpEngine(),
	         	CommunityData(community),
	            UdpTransportTarget((ip, puerto)),
	            ContextData(),
	            ObjectType(ObjectIdentity(mib, 'eventStatus', eventIndex), 1).addAsn1MibSource('file:///usr/share/snmp', #lo ponemos en 2 underCreate
	                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
				   ObjectType(ObjectIdentity(mib, 'eventDescription', eventIndex), eventDescription).addAsn1MibSource('file:///usr/share/snmp',
	                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
				   ObjectType(ObjectIdentity(mib, 'eventType', eventIndex), eventType).addAsn1MibSource('file:///usr/share/snmp',
	                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
				   ObjectType(ObjectIdentity(mib, 'eventOwner', eventIndex), eventOwner).addAsn1MibSource('file:///usr/share/snmp',
	                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))


	if errorIndication:
	    print(errorIndication)
	elif errorStatus:
	    print('%s at %s' % (errorStatus.prettyPrint(),
	                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

	return varBinds
##########################################################################3



ip = raw_input("Introduzca IP: ")
community = raw_input("Introduzca community: ") 
eventDescription =raw_input("Introduzca eventDescription:")
eventType =raw_input("Introduzca eventType:")
eventCommunity =raw_input("Introduzca eventCommunity:")
eventOwner =raw_input("Introduzca eventOwner:")
eventIndex = raw_input("INtroduzca indice evento: ")

##LLAmamoe e imprimimos el resultado
varBinds = snmp_crear_evento(ip,community,eventDescription,eventType,eventCommunity,eventOwner,eventIndex)

for varBind in varBinds:
    print(' = '.join([x.prettyPrint() for x in varBind]))
