from vpython import *
from rabboni import *
import timeit
def average(lis):
    out = []
    b = (lis[0]+lis[1]+lis[2])/3
    for x in lis:
        out.append(x-b)
    return out

rabo = Rabboni(mode = "USB") #先宣告一個物件(這邊宣告它叫rabo)
rabo.connect() #透過USB連接裝置,若抓不到會報錯 (void)
print ("Status(0->unconnected,1->connected):",rabo.Status)
rabo.read_data() 
start=timeit.default_timer()
start1=timeit.default_timer()
#Xa = [0.6724853515625, 0.67578125, 0.68670654296875, 0.71429443359375, 0.4764404296875, 0.8358154296875, 0.92279052734375, 0.78057861328125, 0.83380126953125, 0.77325439453125, -0.1719970703125, -0.18206787109375, -0.07611083984375, -0.01971435546875, 1.99993896484375, 1.5758056640625, 0.824951171875, 1.25970458984375, 1.90838623046875, 1.08160400390625, 0.37457275390625, 1.07452392578125, 1.18634033203125, 0.41851806640625, 0.02740478515625, 0.6025390625, 0.82373046875, 0.27410888671875, 0.78912353515625, 0.67803955078125, -0.22900390625, -0.2232666015625, -0.06103515625, 0.02081298828125, 0.68499755859375, 1.63140869140625, 1.60986328125, 1.99993896484375, 1.09344482421875, 1.02197265625, 0.72735595703125, 0.83251953125, 0.73101806640625, 0.52618408203125, 0.38037109375, 0.2310791015625, 0.47259521484375, 0.42510986328125, 0.5626220703125, 0.52947998046875, -0.3397216796875, -0.1419677734375, -0.0361328125, 0.06756591796875, 0.61883544921875, 1.61322021484375, 1.200439453125, 1.642333984375, 0.921630859375, 0.8321533203125, 0.86041259765625, 0.48590087890625, 0.8460693359375, 0.6151123046875, 0.5513916015625, 0.5447998046875, 0.32501220703125, 0.4207763671875, 0.61041259765625, 0.58697509765625, 0.57122802734375, 0.28460693359375, -0.25201416015625, -0.07635498046875, 0.00518798828125, 0.0404052734375, 1.39141845703125, 0.2271728515625, 0.19976806640625, 0.66229248046875, 0.51202392578125, 0.35791015625, 0.58953857421875, 0.81060791015625, 0.64990234375, 0.60107421875, 0.5880126953125, 0.54083251953125, 0.42694091796875, 0.36419677734375, 0.53662109375, 0.561767578125, 0.37554931640625, -0.20220947265625, -0.07244873046875, -0.05133056640625, -0.55670166015625, 0.53240966796875, 1.036865234375, 1.84112548828125, 0.55657958984375, 0.74652099609375, 0.29400634765625, 0.41082763671875, 0.3414306640625, 0.52056884765625, 0.617431640625, 0.91363525390625, 1.0614013671875, 1.10662841796875, 0.99615478515625, 0.91412353515625, 0.9378662109375, 0.937255859375, 0.91802978515625, 0.89727783203125, 0.9862060546875, 0.8973388671875, 0.87353515625, 0.9010009765625, 1.00701904296875, 0.95428466796875, 0.95880126953125, 1.0394287109375, 1.04437255859375, 1.0355224609375, 0.94830322265625, 0.81585693359375, 0.73236083984375, 0.671142578125, 0.81341552734375, 1.015380859375, 1.1419677734375, 0.9969482421875, 0.76153564453125, 0.29736328125, 0.31402587890625, 0.3404541015625, 0.37884521484375, 0.5615234375, 0.51068115234375, 0.4708251953125, 0.525634765625, 0.54345703125, 0.578369140625, -0.27386474609375, -0.08355712890625, -0.051513671875]
#Ya = [0.71533203125, 0.67999267578125, 0.66473388671875, 0.6728515625, 0.67022705078125, 1.01617431640625, 0.7950439453125, 0.38262939453125, 0.24200439453125, 0.21771240234375, -0.3619384765625, 0.00054931640625, -0.05059814453125, -0.090576171875, -1.37255859375, -0.2962646484375, 0.075439453125, 0.233642578125, 0.15106201171875, 1.16680908203125, 0.33099365234375, 0.28802490234375, 0.61981201171875, 0.51416015625, 0.62103271484375, 0.4957275390625, 0.314697265625, 0.4298095703125, 0.5826416015625, 0.59332275390625, -0.46044921875, -0.188232421875, -0.00030517578125, -0.024658203125, 0.191650390625, 0.4078369140625, 1.60888671875, 1.17279052734375, 0.8800048828125, 1.0672607421875, 0.9246826171875, 0.80859375, 0.4940185546875, 0.342529296875, 0.537353515625, 0.6148681640625, 0.6322021484375, 0.44464111328125, 0.703369140625, 0.74517822265625, -0.37579345703125, -0.0179443359375, 0.02459716796875, 0.12945556640625, -1.0960693359375, 0.70452880859375, 0.65338134765625, 0.58331298828125, 0.70684814453125, 0.46099853515625, 0.29931640625, 0.6431884765625, 0.66351318359375, 1.8084716796875, 0.7713623046875, 0.38916015625, 0.47222900390625, 0.4403076171875, 0.71636962890625, 0.5948486328125, 0.54290771484375, 0.28399658203125, -0.17633056640625, -0.04632568359375, -0.04168701171875, 1.4400634765625, -0.1195068359375, 1.4541015625, 1.8314208984375, 1.3690185546875, 0.65289306640625, 0.8009033203125, 0.64599609375, 0.50347900390625, 0.675537109375, 0.8172607421875, 0.45257568359375, 0.56195068359375, 0.563720703125, 0.622314453125, 0.4462890625, 0.84375, 0.19140625, -0.1495361328125, -0.03631591796875, 0.0328369140625, 1.99993896484375, 1.519775390625, 0.97369384765625, 0.42974853515625, 0.40869140625, 0.5308837890625, 0.29986572265625, 0.2967529296875, 0.36395263671875, 0.5091552734375, 0.3125, 0.23193359375, 0.13958740234375, 0.16961669921875, 0.10943603515625, 0.1820068359375, 0.16778564453125, 0.13983154296875, 0.12896728515625, 0.113525390625, 0.21002197265625, 0.17608642578125, 0.1678466796875, 0.1766357421875, 0.18402099609375, 0.139892578125, 0.16156005859375, 0.22283935546875, 0.38604736328125, 0.39117431640625, 0.31658935546875, 0.386962890625, 0.52447509765625, 0.610107421875, 0.744140625, 0.9443359375, 0.42095947265625, 0.88018798828125, 0.57403564453125, 1.04150390625, 0.6578369140625, 0.56201171875, 0.4849853515625, 0.690673828125, 0.656005859375, 0.72479248046875, 0.623291015625, 0.85467529296875, 0.65386962890625, -0.3673095703125, -0.084716796875, 0.036376953125]
#Za = [-0.2275390625, -0.2586669921875, -0.310791015625, -0.2840576171875, 0.01055908203125, -0.59130859375, -0.57672119140625, -0.43731689453125, -0.1473388671875, -0.2879638671875, -0.374755859375, -0.01214599609375, 0.0994873046875, 0.07623291015625, -1.081298828125, -0.4417724609375, -0.65533447265625, 1.5311279296875, 0.50238037109375, -0.2005615234375, -0.30224609375, -0.60760498046875, -0.15106201171875, -0.55426025390625, -0.27178955078125, 0.26763916015625, -0.28802490234375, 0.2608642578125, -0.1568603515625, 0.2286376953125, 0.039794921875, -0.0059814453125, 0.08355712890625, 0.05633544921875, 1.692138671875, 0.35150146484375, 0.5389404296875, 0.51116943359375, 1.01751708984375, 0.32049560546875, 0.05731201171875, -0.11163330078125, 0.3089599609375, 0.08685302734375, -0.40966796875, -0.56134033203125, 0.01824951171875, -0.19586181640625, -0.0899658203125, -0.1751708984375, -0.0462646484375, 0.1004638671875, -0.00762939453125, -0.18426513671875, 1.99993896484375, 0.64410400390625, 1.6990966796875, 1.83642578125, 0.98919677734375, 0.02618408203125, 0.54119873046875, 0.26458740234375, 0.47723388671875, -0.0718994140625, -0.33062744140625, -0.08319091796875, -0.2310791015625, -0.16986083984375, -0.15972900390625, -0.3216552734375, -0.40130615234375, -0.32177734375, 0.10101318359375, 0.01824951171875, 0.0526123046875, 1.99993896484375, -0.09564208984375, 1.0924072265625, 1.44256591796875, 1.02044677734375, 0.6395263671875, 0.53076171875, 0.05841064453125, -0.0496826171875, -0.22637939453125, 0.459228515625, -0.21905517578125, -0.2261962890625, -0.36639404296875, -0.18115234375, -0.22515869140625, -0.3685302734375, -0.25323486328125, 0.01055908203125, 0.0205078125, 0.1070556640625, 1.99993896484375, -1.7266845703125, 1.99993896484375, 1.99993896484375, 1.34710693359375, 0.78814697265625, 0.34075927734375, 0.27618408203125, 0.12701416015625, 0.0391845703125, 0.0718994140625, -0.17327880859375, -0.25323486328125, -0.3489990234375, -0.3370361328125, -0.373291015625, -0.35272216796875, -0.384033203125, -0.38934326171875, -0.39312744140625, -0.39422607421875, -0.348388671875, -0.334716796875, -0.36724853515625, -0.405517578125, -0.45111083984375, -0.38037109375, -0.25384521484375, -0.17852783203125, -0.28509521484375, -0.3505859375, -0.3238525390625, 0.1318359375, -0.15667724609375, -0.11981201171875, -0.24530029296875, 0.1005859375, 0.06396484375, 0.02252197265625, -0.35546875, -0.28460693359375, -0.07171630859375, -0.2183837890625, -0.1148681640625, -0.1776123046875, -0.2705078125, -0.33111572265625, -0.22100830078125, -0.2252197265625, 0.03692626953125, -0.11676025390625, 0.02655029296875]
try:
    while True:
        rabo.print_data()

except KeyboardInterrupt:
    rabo.disconnect()
    Xa=rabo.Accx_list
    Ya=rabo.Accy_list
    Za=rabo.Accz_list
    end=timeit.default_timer()
    datasize=len(Xa)
    Vx = 0
    Vy = 0
    Vz = 0
    dt = (end-start)/datasize #畫面更新時間(sec)
    t = 0
    tim = 0
    i=1
    Xa=average(Xa)
    Ya=average(Ya)
    Za=average(Za)


    scene = canvas(title='1', width=800, height=800, x=0, y=0, center=vector(0,0.06,0), background=vector(0.5,0.6,0.5))
    floor = box(pos=vector(0,-(0.005)/2,0), length=0.3, height=0.005, width=0.1)
    ball = sphere(pos=vector(0,0,0), radius=0.5)
    pointer1 = arrow(pos=vector(0,0,0),axis=vector(10,0,0),shaftwidth=0.05,color=color.red)
    pointer2 = arrow(pos=vector(0,0,0),axis=vector(0,10,0),shaftwidth=0.05,color=color.blue)
    pointer3 = arrow(pos=vector(0,0,0),axis=vector(0,0,10),shaftwidth=0.05,color=color.green)
    gdx = graph(title="x-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
    #gd2x = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
    gdy = graph(title="x-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
    #gd2y = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
    gdz = graph(title="x-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
    #gd2z = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
    xt = gcurve(graph=gdx, color=color.red)
    yt = gcurve(graph=gdy, color=color.red)
    zt = gcurve(graph=gdz, color=color.red)
    #vt = gcurve(graph=gd2, color=color.red)
    for i in range(datasize):
        rate(20)
        #if(abs(Xa[i])<abs(Za[i])and abs(Ya[i])<abs(Za[i])):
        #    pt = points(color=color.black,pos=vector(0,0,0),shape="quare")
        xt.plot(pos = (start1-timeit.default_timer(), ball.pos.x))
        #vt.plot(pos = (start1-timeit.default_timer(), cube.v.x))
        ball.pos.x +=  Xa[i]*dt* dt *50
        ball.pos.y +=  (Ya[i]-0.98)*dt* dt *50
        # Vx += (Xa[i+1]-Xa[i]) * dt 
        # Vy += (Ya[i+1]-Ya[i]) * dt 
        # Vz += (Za[i+1]-Za[i]) * dt 
        # print(Vx,' ',Vy,' ',Vz)            
        # ball.pos.x += Vx * dt *50
        # ball.pos.y += Vy * dt *50
        # ball.pos.z += Vz * dt *50
        # tim += dtball.pos.x +=  (Xa[i+1]-Xa[i])*dt* dt *500
        # i+=1
    ball.pos.x=0
    ball.pos.y=0
    ball.pos.z=0
    print('finish')
    rabo.disconnect()
    rabo.stop()