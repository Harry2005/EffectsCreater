##########################################################
#       Minecraft Redstone Music Effects Creater         #
#              作者:Harry     Ver:1.0.0                  #
##########################################################


import math
import os

def DrawLine(x1, y1, z1, x2, y2, z2, λ):
    function_dir = "DrawLine("+ str(x1) + "," + str(y1)  + "," + str(z1) + ")" + "to(" + str(x2) + "," + str(y2) + "," + str(z2) + ")"
    if os.path.exists(function_dir)==False:
        os.mkdir(function_dir)
    delta_t = abs(x1 - x2)
    vz = (z2 - z1) / delta_t
    vy = (y2 - y1) / delta_t
    vx = (x2 - x1) / delta_t
    for t in range(0, delta_t):
        function_name = str(t)
        fp = open(function_dir + "\\" + function_name +".mcfunction",'w')
        for i in range(0, λ):
            zi = z1 + vz * (t + i / λ)
            yi = y1 + vy * (t + i / λ)
            xi = x1 + vx * (t + i / λ)
            print("particle endRod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0 1 force".format(xi, yi, zi))
            fp.write("particle endRod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0 1 force \n".format(xi, yi, zi))
            fp.close

def DrawParabola(x1, z1, x2, z2, ymin, ymax, λ):
    function_dir = "DrawParabola("+ str(x1) + "," + str(ymin)  + "," + str(z1) + ")" + "to(" + str(x2) + "," + str(ymax) + "," + str(z2) + ")"
    if os.path.exists(function_dir)==False:
        os.mkdir(function_dir)
    delta_t = abs(x1 - x2)
    vx = (x2 - x1) / delta_t
    vz = (z2 - z1) / delta_t
    for t in range(0, delta_t):
        function_name = str(t)
        fp = open(function_dir + "\\" + function_name +".mcfunction",'w')
        for i in range(0, λ):
            zi = z1 + vz * (t + i / λ)
            yi = ymin + ((4 * ymax) / delta_t) * (t + i / λ) - ((4 * ymax) / (delta_t * delta_t)) * (t + i/λ) * (t + i/λ)
            xi = x1 + vx * (t + i / λ)
            print("particle endRod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0 1 force".format(xi, yi, zi))
            fp.write("particle endRod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0 1 force \n".format(xi, yi, zi))
            fp.close

def DrawSpiral(x1, y1, z1, x2, y2, z2, r, ω, λ):
    function_dir = "DrawSpiral("+ str(x1) + "," + str(y1)  + "," + str(z1) + ")" + "to(" + str(x2) + "," + str(y2) + "," + str(z2) + ")"
    if os.path.exists(function_dir)==False:
        os.mkdir(function_dir)
    delta_t = abs(x1 - x2)
    vz = (z2 - z1) / delta_t
    vy = (y2 - y1) / delta_t
    vx = (x2 - x1) / delta_t
    s = ((z1 - z2) * (z1 - z2) + (x1 - x2) * (x1 - x2)) ** 0.5
    θ = math.atan((x2 - x1) / (z2 - z1))
    φ = math.atan((y2 - y1) / s)
    for t in range(0, delta_t):
        function_name = str(t)
        fp = open(function_dir + "\\" + function_name +".mcfunction",'w')
        for i in range(0, λ):
            zi = z1 + vz * (t + i / λ) 
            yi = y1 + vy * (t + i / λ) 
            xi = x1 + vx * (t + i / λ) 
            zr = r * (math.sin(θ) * math.cos(ω * (t + i / λ)) - math.cos(θ) * math.sin(φ) * math.sin(ω * (t + i / λ)))
            yr = r * (math.cos(φ) * math.sin(ω * (t + i / λ)))
            xr = - r * (math.cos(θ) * math.cos(ω * (t + i / λ)) + math.sin(θ) * math.sin(φ) * math.sin(ω * (t + i / λ)))
            print("particle endRod {0:.10f} {1:.10f} {2:.10f} {3:.10f} {4:.10f} {5:.10f} 0.4 0 force".format(xi, yi, zi, xr, yr, zr))
            fp.write("particle endRod {0:.10f} {1:.10f} {2:.10f} {3:.10f} {4:.10f} {5:.10f} 0.4 0 force \n".format(xi, yi, zi, xr, yr, zr))
            fp.close
    
def DrawParabola_Draspiral(x1, y1, z1, x2, y2, z2, r, ω, n, λ):
    function_dir = "DrawParabola_Draspiral("+ str(x1) + "," + str(y1)  + "," + str(z1) + ")" + "to(" + str(x2) + "," + str(y2) + "," + str(z2) + ")"
    if os.path.exists(function_dir)==False:
        os.mkdir(function_dir)
    delta_t = abs(x1 - x2)
    vz = (z2 - z1) / delta_t
    ymin = min(y1, y2)
    vx = (x2 - x1) / delta_t
    s = ((z1 - z2) * (z1 - z2) + (x1 - x2) * (x1 - x2)) ** 0.5
    ymax = s * n
    θ = (x2 - x1) / (z2 - z1)
    for t in range(0,delta_t):
        function_name = str(t)
        fp = open(function_dir + "\\" + function_name +".mcfunction",'w')
        for i in range(0, λ):
            φ = 4 * n * s * (1 - 2 * (t + i / λ) / delta_t) / s
            zi = z1 + vz * (t + i / λ) 
            yi = ymin + ((4 * ymax) / delta_t) * (t + i / λ) - ((4 * ymax) / (delta_t * delta_t)) * (t + i/λ) * (t + i/λ)
            xi = x1 + vx * (t + i / λ)
            zr_1 = r * (math.sin(θ) * math.cos(ω * (t + i / λ)) - math.cos(θ) * math.sin(φ) * math.sin(ω * (t + i / λ)))
            yr_1 = r * (math.cos(φ) * math.sin(ω * (t + i / λ)))
            xr_1 = - r * (math.cos(θ) * math.cos(ω * (t + i / λ)) + math.sin(θ) * math.sin(φ) * math.sin(ω * (t + i / λ)))
            zr_2 = r * (math.sin(θ) * math.cos(ω * (t + i / λ) + math.pi - math.cos(θ) * math.sin(φ) * math.sin(ω * (t + i / λ) + math.pi)))
            yr_2 = r * (math.cos(φ) * math.sin(ω * (t + i / λ) + math.pi))
            xr_2 = - r * (math.cos(θ) * math.cos(ω * (t + i / λ) + math.pi + math.sin(θ) * math.sin(φ) * math.sin(ω * (t + i / λ) + math.pi)))
            print("particle endRod {0:.10f} {1:.10f} {2:.10f} {3:.10f} {4:.10f} {5:.10f} 0.4 0 force".format(xi, yi, zi, xr_1, yr_1, zr_1))
            print("particle endRod {0:.10f} {1:.10f} {2:.10f} {3:.10f} {4:.10f} {5:.10f} 0.4 0 force".format(xi, yi, zi, xr_2, yr_2, zr_2))
            fp.write("particle endRod {0:.10f} {1:.10f} {2:.10f} {3:.10f} {4:.10f} {5:.10f} 0.4 0 force \nparticle endRod {6:.10f} {7:.10f} {8:.10f} {9:.10f} {10:.10f} {11:.10f} 0.4 0 force \n".format(xi, yi, zi, xr_1, yr_1, zr_1, xi, yi, zi, xr_2, yr_2, zr_2))
            fp.close
                        
#DrawLine(10,5,10,50,10,20,10)
#DrawParabola(5,5,10,10,5,7,50)
#DrawSpiral(10,5,10,50,10,50,1,5,50)
#DrawParabola_Draspiral(10,5,10,20,5,20,0.1,5,0.3,20)