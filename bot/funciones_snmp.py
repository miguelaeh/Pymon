from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp, udp6
from pyasn1.codec.ber import decoder
from pysnmp.proto import api
from pysnmp.hlapi import *


def snmp_get(ip, community, mib, oidObjeto, oidInstancia):

	puerto = 161

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
	
	    

	return varBinds


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


def snmp_getBulk(ip,community,mib,nonRepeaters,maxRepetitions,introducidos):

	puerto = 161
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
	
	return varBinds


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

def snmp_crear_evento(ip,community,eventDescription,eventType,eventCommunity,eventOwner,eventIndex):

	mib = 'RMON-MIB'
	puerto = 161

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

	return varBinds

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


def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
    while wholeMsg:
        msgVer = int(api.decodeMessageVersion(wholeMsg))
        if msgVer in api.protoModules:
            pMod = api.protoModules[msgVer]
        else:
            print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(
            wholeMsg, asn1Spec=pMod.Message(),
            )
        print('Notification message from %s:%s: ' % (
            transportDomain, transportAddress
            )
        )
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:
                print('Enterprise: %s' % (
                    pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()
                    )
                )
                print('Agent Address: %s' % (
                    pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()
                    )
                )
                print('Generic Trap: %s' % (
                    pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()
                    )
                )
                print('Specific Trap: %s' % (
                    pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()
                    )
                )
                print('Uptime: %s' % (
                    pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()
                    )
                )
                varBinds = pMod.apiTrapPDU.getVarBindList(reqPDU)
            else:
                varBinds = pMod.apiPDU.getVarBindList(reqPDU)
            print('Var-binds:')
            for oid, val in varBinds:
                print('%s = %s' % (oid, val))
    return wholeMsg
