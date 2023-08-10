#contoh koneksi ke PLC Modbus TCP
#baca Register : 40064
#tampilkan GUI dengan TKinter
#tombol on off Coil 00003

#module : easymodbus
#install -> pip install easymodbus

#PLC simulator dengan Speed PLC
#download di channel EldikonFulmatic7

#address ip : 127.0.0.1 adalah address local host.


import easymodbus.modbusClient
from tkinter import *

#----------------------------mulai fungsi ---------------------------------
#fungsi baca plc
def bacaplc():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.read_holdingregisters(64,1) #QW128 --> 40064
    modbusclient.close()
    QW128s = "Data QW128 : " + str(QW128)
    lblDataQW128.config(text=QW128s,
                    font=('arial', 28, 'bold'),
                    bg=bg,fg='blue') 
    root.after(500, bacaplc)

#fungsi tulis plc
def tulisplcon():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(3,True)
    modbusclient.close()
def tulisplcoff():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(3,False)
    modbusclient.close()
#----------------------------akhir fungsi ---------------------------------


#--------------------------mulai gui-------------------------------------
root = Tk()
lebar = 400
tinggi = 600
bg = 'powder blue'
fgLbl = 'black'
geo=str(lebar)+'x'+str(tinggi)
root.geometry(geo)
root.title("pt. Eldikon Engineering")
root.config(bg=bg)

#tampilan data plc
lblDataQW128=Label(root)
lblDataQW128.place(x=20,y=190)

#tombol tulis plc
btTulisPLCOn = Button(root,text='Turn ON Q0.3',
                        width=15,height=1,
                        font=('arial',10,'bold'),
                        bg='light blue',fg='black',bd=4,
                        command=tulisplcon)                     
btTulisPLCOn.place(x=20,y=300)
btTulisPLCOff = Button(root,text='Turn OFF Q0.3',
                        width=15,height=1,
                        font=('arial',10,'bold'),
                        bg='light blue',fg='black',bd=4,
                        command=tulisplcoff)                     
btTulisPLCOff.place(x=180,y=300)

#--------------------------akhir gui-------------------------------------

#looping
root.after(250, bacaplc)
root.mainloop()