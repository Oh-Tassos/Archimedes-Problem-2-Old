import turtle, time, csv, colorsys
from matplotlib import cm

def lowpass(val, prev, bias):
	return ((val * (bias)) + (prev * (1 - bias)))

def mag(x, y):
	return ((x ** 2) + (y ** 2)) ** 0.5

t = turtle.Turtle()
s = turtle.Screen()
s.setworldcoordinates(-5000, -5000, 5000, 5000)
s.setup(1000, 1000)
s.bgcolor("black")
t.pencolor("red")
t.speed(-1)
t.ht()

colorcyclelength = 1871514121

colors = cm.get_cmap('viridis', 10592)
s.colormode(1)

minx=0
miny=0
maxx=0
maxy=0
camminx=0
camminy=0
cammaxx=0
cammaxy=0
scale = 10
lastscale = 0
maxscale = scale

framerate = 60 
lasttime = time.monotonic()
fpstargetratio = 1

num = 0
start = 0

t.pencolor(colorsys.hsv_to_rgb(0, 1, 1))
t.pencolor(tuple([float(c) for c in colors(0)[0:3]]))

with open("archimedes_p2_old copy.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        for num in range(start, 1871514121 + 1):      
            if num == int(row[0]):
                if int(row[2]) == 9633:
                    t.pencolor(colorsys.hsv_to_rgb((num / colorcyclelength), 1, 1))
                    t.pencolor(tuple([float(c) for c in colors(int(row[2]))[0:3]]))
                
                    for i in range(0, 800):
                        t.fd(38923)

                        minx = min(t.xcor(), minx)
                        miny = min(t.ycor(), miny)
                        maxx = max(t.xcor(), maxx)
                        maxy = max(t.ycor(), maxy)
                        camminx = lowpass(minx/2, camminx, 0.001 * (fpstargetratio))
                        camminy = lowpass(miny/2, camminy, 0.001 * (fpstargetratio))
                        cammaxx = lowpass(maxx/2, cammaxx, 0.001 * (fpstargetratio))
                        cammaxy = lowpass(maxy/2, cammaxy, 0.001 * (fpstargetratio))
                        maxscale = max(maxscale, mag(maxx - minx, maxy - miny)/2 )
                        scale = lowpass(maxscale, scale, 0.001 * (fpstargetratio))
                        if(time.monotonic() - lasttime >= 1/framerate):
                            if((scale-lastscale)/scale > 0.1):
                                s.setworldcoordinates(-scale + (camminx + cammaxx), -scale + (camminy + cammaxy), scale + (camminx + cammaxx), scale + (camminy + cammaxy))
                                lastscale = scale
                            else:
                                turtle.update()
                            turtle.tracer(n = 0, delay = 0)
                            fpstargetratio = ((time.monotonic() - lasttime)/(1/framerate)) 
                            lasttime = time.monotonic()
                        
                    t.rt(90 * int(row[1]))
                    start = num
                    print(row[2] + ",", num, "HEY!")

                else:
                    t.pencolor(colorsys.hsv_to_rgb((num / colorcyclelength), 1, 1))
                    t.pencolor(tuple([float(c) for c in colors(int(row[2]))[0:3]]))
            
                    t.fd(num - start)

                    minx = min(t.xcor(), minx)
                    miny = min(t.ycor(), miny)
                    maxx = max(t.xcor(), maxx)
                    maxy = max(t.ycor(), maxy)
                    camminx = lowpass(minx/2, camminx, 0.01 * (fpstargetratio))
                    camminy = lowpass(miny/2, camminy, 0.01 * (fpstargetratio))
                    cammaxx = lowpass(maxx/2, cammaxx, 0.01 * (fpstargetratio))
                    cammaxy = lowpass(maxy/2, cammaxy, 0.01 * (fpstargetratio))
                    maxscale = max(maxscale, mag(maxx - minx, maxy - miny)/2 )
                    scale = lowpass(maxscale, scale, 0.01 * (fpstargetratio))
                    if(time.monotonic() - lasttime >= 1/framerate):
                        if((scale-lastscale)/scale > 0.01):
                            s.setworldcoordinates(-scale + (camminx + cammaxx), -scale + (camminy + cammaxy), scale + (camminx + cammaxx), scale + (camminy + cammaxy))
                            lastscale = scale
                        else:
                            turtle.update()
                        turtle.tracer(n = 0, delay = 0)
                        fpstargetratio = ((time.monotonic() - lasttime)/(1/framerate)) 
                        lasttime = time.monotonic()
                        
                    t.rt(90 * int(row[1]))
                    start = num
                    print(row[2] + ",", num)
                    
                break

    print("Done")
    turtle.done()
