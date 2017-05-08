# Pilotage GCE USB 8 Relay Board
import time
import serial

def init_serial(pPort):         
    global ser          
    ser = serial.Serial()
    ser.baudrate = 9600 
    ser.port = pPort
    ser.bytesize = 8
    ser.parity = 'N'
    ser.timeout = None
    ser.xonxoff = False
    ser.rtscts=False
    ser.dsrdtr=False
    ser.timeout = 1
    ser.open()          

    if ser.isOpen():
        print 'Connexion port : ' + ser.portstr  

init_serial('/dev/ttyUSB0')
while True:
    ser.close()
    ser.open()
    time.sleep(2) 
    cmd = raw_input('Saisir ma commande :\r\n')
    ser.write(cmd.encode('ascii')+'\r\n')
    if cmd =='q':
        ser.close()
        print ser.portstr +' est interrompu'
        exit()
    else:
        bytes = ser.readline() 
        print ('Renvoie :\r\n' + bytes) 
