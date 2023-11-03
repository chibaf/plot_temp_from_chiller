import matplotlib.pyplot as plt
import serial
from rtemp_class import rtemp

data=[0.0]*10
while True:
  try:
    temps=rtemp(1)
    data.pop(-1)
    data.insert(0,float(temps.read()))
    x=range(0, 10, 1)
    plt.clf()
    plt.plot(x,data)
    plt.pause(0.1)
  except KeyboardInterrupt:
    print ('exiting')
    break
exit()
