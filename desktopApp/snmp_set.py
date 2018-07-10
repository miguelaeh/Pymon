from pysnmp.hlapi import *

##########################################################################3
def snmp_set(ip,community,mib,idObjeto,oidInstancia,value):
    puerto = 161

    errorIndication, errorStatus, errorIndex, varBinds = next(
    		setCmd(SnmpEngine(),
             	CommunityData(community),
                UdpTransportTarget((ip, puerto)),
                ContextData(),
                ObjectType(ObjectIdentity(mib, idObjeto, oidInstancia), value).addAsn1MibSource('file:///usr/share/snmp',
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
mib = raw_input("Introduzca nombre de la MIB: ") #la mib es el oid de la mib
idObjeto = raw_input("Introduzca Id del objeto: ")
oidInstancia = raw_input("Introduzca oid de la instancia: ")
value = raw_input("Introduzca el nuevo valor: ")

varBinds = snmp_set(ip,community,mib,idObjeto,oidInstancia,value)
for varBind in varBinds:
    print(' = '.join([x.prettyPrint() for x in varBind]))