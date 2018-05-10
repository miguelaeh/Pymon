from pysnmp.hlapi import *


puerto = 161

ip = raw_input("Introduzca IP: ")
community = raw_input("Introduzca community: ")
mib = raw_input("Introduzca nombre de la MIB: ") #la mib es el oid de la mib
idObjeto = raw_input("Introduzca Id de la notificacion: ")





errorIndication, errorStatus, errorIndex, varBinds = next(sendNotification(SnmpEngine(),
	                 CommunityData(community),
                     UdpTransportTarget((ip, puerto)),
                     ContextData(),
					'trap',
					NotificationType(ObjectIdentity(mib, idObjeto))))



if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))