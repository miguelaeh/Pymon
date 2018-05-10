from pysnmp.hlapi import *


puerto = 161

ip = raw_input("Introduzca IP: ")
community = raw_input("Introduzca community: ") 
mib = 'RMON-MIB'
#idObjeto = raw_input("Introduzca Id del objeto: ")
#oidInstancia = raw_input("Introduzca oid de la instancia: ")
#value = raw_input("Introduzca el nuevo valor: ")

#eventIndex 	=raw_input("Introduzca eventIndex")
eventDescription =raw_input("Introduzca eventDescription:")
eventType =raw_input("Introduzca eventType:")
eventOwner =raw_input("Introduzca eventOwner:")
eventIndex = raw_input("INtroduzca indice evento: ")


errorIndication5, errorStatus5, errorIndex5, varBinds5 = next(
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


if errorIndication5:
    print(errorIndication5)
elif errorStatus5:
    print('%s at %s' % (errorStatus5.prettyPrint(),
                        errorIndex5 and varBinds5[int(errorIndex5) - 1][0] or '?'))
else:
    for varBind in varBinds5:
        print(' = '.join([x.prettyPrint() for x in varBind]))