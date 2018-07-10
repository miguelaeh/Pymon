from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp, udp6
from pyasn1.codec.ber import decoder
from pysnmp.proto import api
from pysnmp.hlapi import *


def snmp_get(ip, community, mib, oidObjeto, oidInstancia):

	puerto = 161
	try:
		errorIndication, errorStatus, errorIndex, varBinds = next(
		    getCmd(SnmpEngine(),
		           CommunityData(community, mpModel=0),
		           UdpTransportTarget((ip, puerto)),
		           ContextData(),
		           ObjectType(ObjectIdentity(mib, oidObjeto, oidInstancia).addAsn1MibSource('file:///usr/share/snmp',
		                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'))) #el 0 es porque es la instancia, 
		                                                        #para tablas poner donde esta el 0 el oid del objeto columna
		)

		if errorIndication:
		    print(errorIndication)
		elif errorStatus:
		    print('%s at %s' % (errorStatus.prettyPrint(),
		                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
	except:
		varBinds =  None
	    

	return varBinds


def snmp_set(ip,community,mib,idObjeto,oidInstancia,value):

	puerto = 161
	try:
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
	except:
		varBinds = None

	return varBinds


def snmp_getBulk(ip,community,mib,nonRepeaters,maxRepetitions,introducidos):

	puerto = 161
	try:
		objetos = introducidos.split(",")
		oidsObjetos = []
		for x in xrange(1,len(objetos)):
			oidsObjetos += ObjectType(ObjectIdentity(mib, objetos[x]).addAsn1MibSource('file:///usr/share/snmp',
		                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'))
		g = bulkCmd(SnmpEngine(),
		             CommunityData(community),
		             UdpTransportTarget((ip,puerto)),
		             ContextData(),
		             nonRepeaters, maxRepetitions,
		             oidsObjetos)

		errorIndication, errorStatus, errorIndex, varBinds = next(g)

		if errorIndication:
		    print(errorIndication)
		elif errorStatus:
		    print('%s at %s' % (errorStatus.prettyPrint(),
		                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
	except:
		varBinds = None
	
	return varBinds


def snmp_getNext(ip, community,mib,oidObjeto):

    puerto = 161
    try:
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
    except:
    	varBinds = None

    return varBinds

def snmp_crear_evento(ip,community,eventDescription,eventType,eventCommunity,eventOwner,eventIndex):

	mib = 'RMON-MIB'
	puerto = 161
	try:
		errorIndication, errorStatus, errorIndex, varBinds = next(
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


		if errorIndication:
		    print(errorIndication)
		elif errorStatus:
		    print('%s at %s' % (errorStatus.prettyPrint(),
		                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
	except:
		varBinds = None

	return varBinds

def snmp_crear_alarma(ip,community,indiceAlarma,indiceEvento, owner, interval, variable, sampleType, risingthr, fallingthr):
    puerto = 161
    mib = 'RMON-MIB'
    #configurar evento de la alarma
    try:

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
   
    except: 
    	varBinds = None


    return varBinds


