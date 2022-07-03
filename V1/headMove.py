import serial
 
#ser = serial.Serial('/dev/ttyACM0', 9600)
 
class Motion():
    x_pos = 0
    y_pos = 0
    z_pos = 0
    angle_pos = 0
 
    def __init__(self):
        #ser.write(b'G28\r\n')
        print('abc')
 
    def headMove(self,x=0, y=0, z=0, angle=0):
        ser.write(b'G91\r\n')
        pulse = bytes("G01 " +'X' + str(x) + 'Y' + str(y) + 'Z' + str(z) + "\r\n", 'utf-8')
        ser.write(pulse)
        print('command: G01, X:',x,', Y:',y,', Z:',z,', theta:',angle,'Printed')
 