from pysnmp.hlapi import *


###################################################################################
def snmp_crear_alarma(ip,community,indiceAlarma,indiceEvento, owner, interval, variable, sampleType, risingthr, fallingthr):
    puerto = 161
    mib = 'RMON-MIB'
    #configurar evento de la alarma
    errorIndication1, errorStatus1, errorIndex1, varBinds1 = next(
    		setCmd(SnmpEngine(),
             	CommunityData(community),
                UdpTransportTarget((ip, puerto)),
                ContextData(),
                ObjectType(ObjectIdentity(mib, 'alarmFallingEventIndex', indiceAlarma), indiceEvento).addAsn1MibSource('file:///usr/share/snmp',
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
   
    return varBinds
##########################################################################3

ip = raw_input("Introduzca IP: ")
community = raw_input("Introduzca community: ") 
indiceAlarma = raw_input("Introduzca indice de indiceAlarma: ")
indiceEvento = raw_input("Introduzca indice del evento: ")
owner  = raw_input("Introduzca owner: ")
interval = raw_input("Introduzca intervalo: ")
variable = raw_input("Introduzca oid de la variable a monitorizar: ")
sampleType = raw_input("Introduzca tipo de muestreo: ")
risingthr = raw_input("Introduzca umbral superior: ")
fallingthr = raw_input("Introduzca umbral inferior: ")

##llamamos e imprimimos
varBinds = snmp_crear_alarma(ip,community,indiceAlarma,indiceEvento, owner, interval, variable, sampleType, risingthr, fallingthr)

for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))