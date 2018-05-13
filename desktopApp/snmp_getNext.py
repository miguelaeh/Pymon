from pysnmp.hlapi import *

#####################################################
def snmp_getNext(ip, community,mib,oidObjeto):

    puerto = 161

    g = nextCmd(SnmpEngine(),
                CommunityData(community),
                UdpTransportTarget((ip, puerto)),
                ContextData(),
                ObjectType(ObjectIdentity(mib, oidObjeto).addAsn1MibSource('file:///usr/share/snmp',
                                                                                     'http://mibs.snmplabs.com/asn1/@mib@')))
    errorIndication, errorStatus, errorIndex, varBinds = next(g)

    #g.send( [ ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets')) ] ) #La funcion send permite repetir todo lo anterior cambiando solo lo que le pasamos

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    return varBinds
##################################################




ip = raw_input("Introduzca IP: ")
community = raw_input("Introduzca community: ")
mib = raw_input("Introduzca nombre de la MIB: ") #la mib es el oid de la mib
oidObjeto = raw_input("Introduzca Id del objeto: ")


#EJECUTO E IMPRIMO
varBinds = snmp_getNext(ip, community,mib,oidObjeto)

for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))