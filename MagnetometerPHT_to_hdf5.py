import pandas as pd
import matplotlib.pyplot as plt 
import re  
import numpy as np
Tiem = [] 
Fieldx=[]
Fieldy=[]
Fieldz=[]
Temp=[]
Field1x=[]
Field1y=[]
Field1z=[]
Temp1=[]
pressure=[]
humidity=[]
temperature=[]
graphy = open('sanity_test.txt','r')
#badFlag = False
for i, row in enumerate(graphy): 
    if i!=0 and i%4==1:
        Tiem.append(row)
    elif i!=0 and i%4==2:
        SPLITS=row.strip('[]').rsplit(',')
          #thisTemp = np.float32(splits[4].strip('C]\n'))
         # if abs(thisTemp) > 50:
         #     badFlag = True
         #     continue
         #badFlag = False
        #print(SPLITS)
        Fieldx.append(np.float32(SPLITS[0].rstrip('xyzC'))) 
        Fieldy.append(np.float32(SPLITS[1].rstrip('xyzC')))  
        Fieldz.append(np.float32(SPLITS[2].rstrip('xyzC')))
        Temp.append(np.float32(SPLITS[3].rstrip('xyzC]\n')))
    elif i!=0 and i%4==3:
         # if badFlag:
         #     continue
        SPLITS=row.strip('[]').rsplit(',')
        #print(SPLITS)
        Field1x.append(np.float32(SPLITS[0].rstrip('xyzC'))) 
        Field1y.append(np.float32(SPLITS[1].rstrip('xyzC')))  
        Field1z.append(np.float32(SPLITS[2].rstrip('xyzC')))
        Temp1.append(np.float32(SPLITS[3].rstrip('xyzC]\n')))
    elif i!=0 and i%4==0:
        SPLITS=row.strip('[]').rsplit(',')
        #print(SPLITS)
        pressure.append(np.float32(SPLITS[0].rstrip('hPa%rHC'))) 
        humidity.append(np.float32(SPLITS[1].rstrip('hPa%rHC'))) 
        temperature.append(np.float32(SPLITS[2].rstrip('hPa%rHC]\n'))) 
graphy.close()
#Converting time and date to make plotting work correctly
Tiem=pd.to_datetime(Tiem)
#Outputting as hdf files
df=pd.DataFrame({'Time':Tiem,
                 'x':Fieldx,
                 'y':Fieldy,
                 'z':Fieldz,
                 'Temp':Temp})
df1=pd.DataFrame({'Time':Tiem,
                  'x':Field1x,
                  'y':Field1y,
                  'z':Field1z,
                  'Temp':Temp1})
df2=pd.DataFrame({'Time':Tiem,
                  'hPa':pressure,
                  '%rH':humidity,
                  'Temp':temperature})
df.to_hdf('sanity_testB0.hdf5',key='df',mode='w')
df1.to_hdf('sanity_testB1.hdf5',key='df1',mode='w')
df2.to_hdf('sanity_test_pht.hdf5',key='df2',mode='w')
#Plotting 
plt.plot(Tiem,Fieldx, label='x')
plt.plot(Tiem,Fieldy, label='y')
plt.plot(Tiem,Fieldz, label='z')
plt.legend()
plt.xticks(rotation=90)
plt.xlabel('Date and Time') 
plt.ylabel('Magnetic Field (µT)') 
plt.title('Magnetic Field probe 0 Vs Time') 
plt.show() 
plt.plot(Tiem,Field1x, label='x')
plt.plot(Tiem,Field1y, label='y')
plt.plot(Tiem,Field1z, label='z')
plt.legend()
plt.xticks(rotation=90)
plt.xlabel('Date and Time') 
plt.ylabel('Magnetic Field (µT)') 
plt.title('Magnetic Field probe 1 Vs Time') 
plt.show() 
plt.plot(Tiem,pressure)
plt.xlabel('Date and Time')
plt.ylabel('Pressure (hPa)')
plt.title('Pressure vs Time')
plt.show()
plt.plot(Tiem, humidity)
plt.xlabel('Date and Time')
plt.ylabel('Humidity (%rH)')
plt.title('Humidity vs time')
plt.show()
plt.plot(Tiem,Temp,label='probe 0')
plt.plot(Tiem,Temp1,label='probe 1')
plt.plot(Tiem,temperature,label='PHT')
plt.xticks(rotation=90)
plt.xlabel('Date and Time') 
plt.ylabel('Temperature of probes')
plt.title('Temperature of Probes vs Time.')
plt.legend()
plt.show()
