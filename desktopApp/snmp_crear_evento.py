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
eventCommunity =raw_input("Introduzca eventCommunity:")
#eventLastTimeSent =raw_input("Introduzca eventLastTimeSent:")
eventOwner =raw_input("Introduzca eventOwner:")
eventIndex = raw_input("INtroduzca indice evento: ")




errorIndication5, errorStatus5, errorIndex5, varBinds5 = next(
		setCmd(SnmpEngine(),
         	CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'eventStatus', eventIndex), 2).addAsn1MibSource('file:///usr/share/snmp', #lo ponemos en 2 underCreate
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
			ObjectType(ObjectIdentity(mib, 'eventDescription', eventIndex), eventDescription).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
			ObjectType(ObjectIdentity(mib, 'eventType', eventIndex), eventType).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
			ObjectType(ObjectIdentity(mib, 'eventOwner', eventIndex), eventOwner).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))



#configurar evento 
errorIndication1, errorStatus1, errorIndex1, varBinds1 = next(
		setCmd(SnmpEngine(),
         	CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'eventDescription', eventIndex), eventDescription).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))


errorIndication2, errorStatus2, errorIndex2, varBinds2 = next(
		setCmd(SnmpEngine(),
         	CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'eventType', eventIndex), eventType).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))

errorIndication3, errorStatus3, errorIndex3, varBinds3 = next(
		setCmd(SnmpEngine(),
         	CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'eventCommunity', eventIndex), eventCommunity).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))

errorIndication4, errorStatus4, errorIndex4, varBinds4 = next(
		setCmd(SnmpEngine(),
         	CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'eventOwner', eventIndex), eventOwner).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))






#if errorIndication:
#    print(errorIndication)
#elif errorStatus:
#    print('%s at %s' % (errorStatus.prettyPrint(),
#                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
#else:
#    for varBind in varBinds1:
#        print(' = '.join([x.prettyPrint() for x in varBind]))


if errorIndication1:
    print(errorIndication1)
elif errorStatus1:
    print('%s at %s' % (errorStatus1.prettyPrint(),
                        errorIndex1 and varBinds1[int(errorIndex1) - 1][0] or '?'))
else:
    for varBind in varBinds1:
        print(' = '.join([x.prettyPrint() for x in varBind]))



if errorIndication2:
    print(errorIndication2)
elif errorStatus2:
    print('%s at %s' % (errorStatus2.prettyPrint(),
                        errorIndex2 and varBinds2[int(errorIndex2) - 1][0] or '?'))
else:
    for varBind in varBinds2:
        print(' = '.join([x.prettyPrint() for x in varBind]))



if errorIndication3:
    print(errorIndication3)
elif errorStatus3:
    print('%s at %s' % (errorStatus3.prettyPrint(),
                        errorIndex3 and varBinds3[int(errorIndex3) - 1][0] or '?'))
else:
    for varBind in varBinds3:
        print(' = '.join([x.prettyPrint() for x in varBind]))


if errorIndication4:
    print(errorIndication4)
elif errorStatus4:
    print('%s at %s' % (errorStatus4.prettyPrint(),
                        errorIndex4 and varBinds4[int(errorIndex4) - 1][0] or '?'))
else:
    for varBind in varBinds4:
        print(' = '.join([x.prettyPrint() for x in varBind]))


if errorIndication5:
    print(errorIndication5)
elif errorStatus5:
    print('%s at %s' % (errorStatus5.prettyPrint(),
                        errorIndex5 and varBinds5[int(errorIndex5) - 1][0] or '?'))
else:
    for varBind in varBinds5:
        print(' = '.join([x.prettyPrint() for x in varBind]))
