from vpython import *
from rabboni import *
import timeit
import time
class rabo():


    def __init__(self):
        self.rabo = Rabboni(mode = "USB") #先宣告一個物件(這邊宣告它叫rabo)
        self.rabo.connect() #透過USB連接裝置,若抓不到會報錯 (void)
        print ("Status(0->unconnected,1->connected):",self.rabo.Status)
        self.Vx = 0
        self.Vy = 0
        self.Vz = 0
        self.dt= 0


    def mean_filter(self,lis,noice):
        
        temp = []
        bias = 0.0
        for x in range(20):
            bias += lis[x]
        bias /= 20
        for x in range(len(lis)-2):
            avr = (lis[x]+lis[x+1]+lis[x+2])/3
            avr -= bias
            if avr < noice:
                temp.append(0)
            else:
                temp.append(avr)
        self.processed_data.append(temp)


    def scan(self):
        self.start_t = time.time()
        self.rabo.read_data()
        while 1:
            try:
                self.rabo.print_data()
            except:
                break
        self.end_t = time.time()
        self.rabo.disconnect()
        self.data = []
        self.data.append(self.rabo.Accx_list)
        self.data.append(self.rabo.Accy_list)
        self.data.append(self.rabo.Accz_list)
        self.data.append(self.rabo.Gyrx_list)
        self.data.append(self.rabo.Gyry_list)
        self.data.append(self.rabo.Gyrz_list)
        self.dt = self.end_t - self.start_t
        print(self.data)


    def data_process(self):
        self.processed_data = []
        for x in self.data:
            self.mean_filter(x,0.03) #到時候放lis的lis,noise
        self.dT = self.dt/ len(self.processed_data) #一秒幾筆資料
        self.dt = len(self.processed_data)/self.dt #畫面更新時間（sec)

    def XYZt_graph(self):
        self.gdx = graph(title="x-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
        #gd2x = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
        self.gdy = graph(title="y-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="y(m)")
        #gd2y = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
        self.gdz = graph(title="z-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="z(m)")
        #gd2z = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
        self.xt = gcurve(graph=gdx, color=color.red)
        self.yt = gcurve(graph=gdy, color=color.red)
        self.zt = gcurve(graph=gdz, color=color.red)
    def the_canvas(self):
        self.scene = canvas(title='1', width=800, height=800, x=0, y=0, center=vector(1.5,0.8,0), background=vector(0.5,0.6,0.5))
        self.floor = box(pos=vector(0,-(0.005)/2,0), length=0.3, height=0.005, width=0.1)
        self.ball = sphere(pos=vector(0,0,0), radius=0.5)
        self.pointer1 = arrow(pos=vector(-10,0,0),axis=vector(20,0,0),shaftwidth=0.05,color=color.red)
        self.pointer2 = arrow(pos=vector(0,-10,0),axis=vector(0,20,0),shaftwidth=0.05,color=color.blue)
        self.pointer3 = arrow(pos=vector(0,0,-10),axis=vector(0,0,20),shaftwidth=0.05,color=color.green)
        self.gdx = graph(title="x-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
        #gd2x = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
        self.gdy = graph(title="y-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
        #gd2y = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
        self.gdz = graph(title="z-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
        #gd2z = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
        self.xt = gcurve(graph=self.gdx, color=color.red)
        self.yt = gcurve(graph=self.gdy, color=color.red)
        self.zt = gcurve(graph=self.gdz, color=color.red)
        #vt = gcurve(graph=gd2, color=color.red)


    def draw_canvas(self):
        self.datasize = len(self.processed_data[0])
        print(len(self.data), self.datasize,len(self.processed_data),len(self.processed_data[0]),'\n')
        for i in range(self.datasize):
            rate(int(1 / self.dT))
            #if(abs(Xa[i])<abs(Za[i])and abs(Ya[i])<abs(Za[i])):
            #    pt = points(color=color.black,pos=vector(0,0,0),shape="quare")
            self.xt.plot(pos = (1, self.ball.pos.x))
            self.yt.plot(pos = (1, self.ball.pos.y))
            self.zt.plot(pos = (1, self.ball.pos.z))
            #vt.plot(pos = (start1-timeit.default_timer(), cube.v.x))
            print(i,'\n')
            self.ball.pos.x +=  self.processed_data[0][i]*self.dt* self.dt *50
            self.ball.pos.y +=  (self.processed_data[1][i]-0.98)*self.dt* self.dt *50
            # Vx += (Xa[i+1]-Xa[i]) * dt 
            # Vy += (Ya[i+1]-Ya[i]) * dt 
            # Vz += (Za[i+1]-Za[i]) * dt 
            # print(Vx,' ',Vy,' ',Vz)            
            # ball.pos.x += Vx * dt *50
            # ball.pos.y += Vy * dt *50
            # ball.pos.z += Vz * dt *50
            # tim += dtball.pos.x +=  (Xa[i+1]-Xa[i])*dt* dt *500
            # i+=1
        # ball.pos.x=0
        # ball.pos.y=0
        # ball.pos.z=0
    def stop_rab(self):
        self.rabo.disconnect()
        self.rabo.stop()

Rab = rabo()
Rab.scan()
Rab.data_process()
Rab.the_canvas()
Rab.draw_canvas()
# Rab.stop_rab()
print("finish!!")