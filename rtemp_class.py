class rtemp:

  def __init__(self,port):
    self.port = port;
  
  def read(self):
    import serial
    if self.port==0:
      ser=serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    else:
      ser=serial.Serial('/dev/ttyUSB1',9600,timeout=1)
# get measurement temperature
    mtemp=b'\x04\x32\x37\x4D\x31\x05'
    ser.write(mtemp)  
    line = ser.readline()  
    line2 = line.strip().decode("utf-8")
    b=line2.split()
    c=float(b[1][:-2])
    ser.close()
    return c
