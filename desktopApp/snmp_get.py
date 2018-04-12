from pysnmp.hlapi import *

puerto = 161

ip = raw_input("Introduzca IP: ")
community = raw_input("Introduzca community: ")
mib = raw_input("Introduzca nombre de la MIB: ") #la mib es el oid de la mib
idObjeto = raw_input("Introduzca Id del objeto: ")
oidInstancia = raw_input("Introduzca oid de la instancia: ")




errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(community, mpModel=0),
           UdpTransportTarget((ip, puerto)),
           ContextData(),
           ObjectType(ObjectIdentity(mib, idObjeto, oidInstancia))) #el 0 es porque es la instancia, 
                                                        #para tablas poner donde esta el 0 el oid del objeto columna
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
