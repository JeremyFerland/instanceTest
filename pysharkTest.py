import pyshark
#from OSC import OSCClient, OSCMessage

macLst = []
capture = pyshark.LiveCapture(interface ='wlan1')
capture.display_filter = 'wlan.sa'

capture.display_filter = 'wlan.sa_resolved'
capture

myError = ''


#client = OSCClient()
#client.connect( ("192.168.1.143", 7001))




for packet in capture.sniff_continuously():
  #client.send(OSCMessage(packet['WLAN'].ta))
  #client.send(OSCMessage(packet['WLAN'].addr))


  print 'MAC address: ',packet['WLAN_RADIO'].signal_dbm
  print 'MAC address: ',packet['WLAN'].ta
  print 'MAC address: ',packet['WLAN'].addr
 # if packet['WLAN'].ta == '1c:b7:2c:51:ca:85':  
#    print packet

  #if int(packet['WLAN'].fc_type_subtype) == 8:
   

   # if packet['WLAN'].ta not in macLst:
    #  macLst.append(packet['WLAN'].ta)
     # print 'im out', packet['WLAN'].ta

  #if (int(packet['WLAN'].fc_type_subtype) == 4 or int(packet['WLAN'].fc_type_subtype) == 5):
    #if packet['WLAN'].ta not in macLst:
 
    #try:
      #client.send(OSCMessage(packet['WLAN'].ta))
      
    #  print 'MAC address: ',packet['WLAN'].addr
   # except :
     # print'nothing here'
      
 # if packet['WLAN'].ta not in macLst:
    #macLst.append(packet['WLAN'].ta)
    
    #print 'MAC address: ',packet['WLAN'].ta
		#print 'MAC address: ',packet