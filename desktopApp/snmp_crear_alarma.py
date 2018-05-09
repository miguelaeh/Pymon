from pysnmp.hlapi import *


puerto = 161

ip = raw_input("Introduzca IP: ")
community = raw_input("Introduzca community: ") 
mib = 'RMON-MIB'
#idObjeto = raw_input("Introduzca Id del objeto: ")
#oidInstancia = raw_input("Introduzca oid de la instancia: ")
#value = raw_input("Introduzca el nuevo valor: ")

evento = raw_input("Introduzca indice del evento: ")
owner  = raw_input("Introduzca owner: ")
interval = raw_input("Introduzca intervalo: ")
variable = raw_input("Introduzca oid de la variable a monitorizar: ")
sampleType = raw_input("Introduzca tipo de muestreo: ")
risingthr = raw_input("Introduzca umbral superior: ")
fallingthr = raw_input("Introduzca umbral inferior: ")

#################################################################################
#POR SER TABLAS PUEDE QUE HAYA QUE PONER EL CALOR DE LOS INDICES PARA HACER EL SET LO QUE PASA QUE EL VALOR NO PUEDO SABERLO PORQUE SE CONFUGRA SOLO
###################################################################################33


#configurar evento de la alarma
errorIndication1, errorStatus1, errorIndex1, varBinds1 = next(
		setCmd(SnmpEngine(),
         	CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'alarmFallingEventIndex', 0), evento).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))

#configurar dueno
errorIndication2, errorStatus2, errorIndex2, varBinds2 = next(
        setCmd(SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'alarmOwner', 0), owner).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))

#configurar intervalo
errorIndication3, errorStatus3, errorIndex3, varBinds3 = next(
        setCmd(SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'alarmInterval', 0), interval).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))

#configurar variable
errorIndication4, errorStatus4, errorIndex4, varBinds4 = next(
        setCmd(SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'alarmVariable', 0), variable).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))

#configurar tipo muestreo
errorIndication5, errorStatus5, errorIndex5, varBinds5 = next(
        setCmd(SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'alarmSampleType', 0), sampleType).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))

#configurar umbrales
errorIndication6, errorStatus6, errorIndex6, varBinds6 = next(
        setCmd(SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'alarmRisingThreshold', 0), risingthr).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))
errorIndication7, errorStatus7, errorIndex7, varBinds7 = next(
        setCmd(SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'alarmFallingThreshold', 0), fallingthr).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))






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


if errorIndication6:
    print(errorIndication6)
elif errorStatus6:
    print('%s at %s' % (errorStatus6.prettyPrint(),
                        errorIndex6 and varBinds6[int(errorIndex6) - 1][0] or '?'))
else:
    for varBind in varBinds6:
        print(' = '.join([x.prettyPrint() for x in varBind]))



if errorIndication7:
    print(errorIndication7)
elif errorStatus7:
    print('%s at %s' % (errorStatus7.prettyPrint(),
                        errorIndex7 and varBinds7[int(errorIndex7) - 1][0] or '?'))
else:
    for varBind in varBinds7:
        print(' = '.join([x.prettyPrint() for x in varBind]))