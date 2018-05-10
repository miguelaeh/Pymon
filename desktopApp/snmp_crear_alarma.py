from pysnmp.hlapi import *


puerto = 161

ip = raw_input("Introduzca IP: ")
community = raw_input("Introduzca community: ") 
mib = 'RMON-MIB'
#idObjeto = raw_input("Introduzca Id del objeto: ")
#oidInstancia = raw_input("Introduzca oid de la instancia: ")
#value = raw_input("Introduzca el nuevo valor: ")
indiceAlarma = raw_input("Introduzca indice de indiceAlarma: ")
evento = raw_input("Introduzca indice del evento: ")
owner  = raw_input("Introduzca owner: ")
interval = raw_input("Introduzca intervalo: ")
variable = raw_input("Introduzca oid de la variable a monitorizar: ")
sampleType = raw_input("Introduzca tipo de muestreo: ")
risingthr = raw_input("Introduzca umbral superior: ")
fallingthr = raw_input("Introduzca umbral inferior: ")

#################################################################################
#
###################################################################################33


#configurar evento de la alarma
errorIndication, errorStatus, errorIndex, varBinds = next(
		setCmd(SnmpEngine(),
         	CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, 'alarmFallingEventIndex', indiceAlarma), evento).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
            ObjectType(ObjectIdentity(mib, 'alarmOwner', indiceAlarma), owner).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
            ObjectType(ObjectIdentity(mib, 'alarmInterval', indiceAlarma), interval).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
            ObjectType(ObjectIdentity(mib, 'alarmVariable', indiceAlarma), variable).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
            ObjectType(ObjectIdentity(mib, 'alarmSampleType', indiceAlarma), sampleType).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
            ObjectType(ObjectIdentity(mib, 'alarmRisingThreshold', indiceAlarma), risingthr).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'),
            ObjectType(ObjectIdentity(mib, 'alarmFallingThreshold', indiceAlarma), fallingthr).addAsn1MibSource('file:///usr/share/snmp',
                                                                                     'http://mibs.snmplabs.com/asn1/@mib@')))



if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))



