from pysnmp.hlapi import *



g = sendNotification(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget(('demo.snmplabs.com', 162)),
                      ContextData(),
                      'trap',
                      NotificationType(ObjectIdentity('IF-MIB', 'ifInOctets'), instanceIndex=(123,)).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')) 


				###########CREO QUE PUEDO HACER LO DEL RMON CAMBIENADO EL INSTANCEINDEX, EL 123 ES EL VALOR DEL INDICE EN EL EJEMPLO

next(g)