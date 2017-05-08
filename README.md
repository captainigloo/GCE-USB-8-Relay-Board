# GCE-USB-8-Relay-Board
GCE USB 8 Relay Board
![alt text](https://github.com/captainigloo/GCE-USB-8-Relay-Board/blob/master/media/controller-usb-8-relay-board.jpg "")

****************************************************************************
PROTOCOLE DE COMMUNICATION CARTE RELAIS USB
****************************************************************************
Auteur: Patrick Gorce
Société:GCE.ELECTRONICS
Le:15/02/2009
****************************************************************************

Les ordres sont envoyées par trame série soit par port série virtuel (driver FTDI vpc) 
soit par tunnel usb (driver FTDI D2XX).
Pour personnaliser le driver USB, utiliser le SDK FTDI  www.fdi.com
Références:
http://www.ftdichip.com
http://www.ftdichip.com/FTDrivers.htm


For most of these operating systems two types of driver are available:  
Virtual COM Port (VCP) drivers and direct (D2XX) drivers.  
The VCP driver emulates a standard PC serial port such that the USB device 
may be communicated with as a standard RS232 device.  
The D2XX driver allows direct access to a USB device via a DLL interface.

To locate the drivers you want to install for a device, select which 
of the driver types you wish to use (VCP or D2XX) and then locate
the appropriate operating systems.  With the exception of Windows 98 and Windows ME, 
all devices are supported in each driver package.

 
In addition to the drivers developed by FTDI, there are a number 
of drivers available which have been developed by third parties. 
Some of these drivers are listed on our 3rd Par414ty Drivers page.



*****************************************************************************
Configuration port série: 1 start, 8 bit, 1 stop (vitesse 9600 bauds)
*****************************************************************************
La trame est composée de 5 caractères (minuscule ou majuscule) pouvant etre envoyés en ASCII ou en Hexadécimal

****************
Code ascii
****************
                          
Start of frame: RLY
N° channel: 0 à 8
CMD: 0 ou 1

Exemple de trame:

RLY11 // commute le relais 1 en position travail
RLY10 // commute le relais 1 en position repos
RLY21 // commute le relais 2 en position travail
...........................................................................
RLY80 commute le relais 8 en position repos

En cas de mauvaise commande la carte renvoi un retour chariot et le caractère ?

****************
Code hexa
****************
Start of frame:  0x52 0x4C 0x59 ou 0x72 0x6C 0x79
N° channel: 0x31 à 0x38
Cmd: 0x30 ou 0x31


Exemple de trame:

0x52 0x4C 0x59 0x31 0x31 // commute le relais 1 en position travail
0x52 0x4C 0x59 0x31 0x30 // commute le relais 1 en position repos
0x52 0x4C 0x59 0x32 0x31 // commute le relais 2 en position travail
...........................................................................
0x52 0x4C 0x59 0x38 0x30 commute le relais 8 en position repos

Pour tout autre caractère ou chaines de caractères la carte renvoi le code suivant:
0x0D 0x3F
*******************************************************************************
Modification du :04/09/2009
*******************************************************************************

Rajout du mode mémoire: la carte garde la dernière configuration en mémoire en cas de coupure d'alimentation.


****************
Code ascii 
****************
M0 // Mode mémore désactivé
M1 // Mode mémoire activé

****************
Code hexa
****************
0x4D 0x30 // Mode mémore désactivé
0x4D 0x31 // Mode mémoire activé
*******************************************************************************

Rajout d'une commande pour connaitre l'état des relais.


****************
Code ascii 
****************
?RLY // Renvoi l'état logique des 8 relais sous la forme >00000000   (le caractère le plus  à droite correspond au relais 8)

****************
Code hexa
****************
0X3F 0x52 0x4C 0x59 // Renvoi l'état logique des 8 relais sous la forme >00000000   (le caractère le plus  à droite correspond au relais 8)


******************************************************************************
END
