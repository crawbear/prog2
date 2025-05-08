""" MA3.py

Student: Christian Steen Aune
Mail: 
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
import numpy as np

#Ex 1
def approximate_pi(n): 
    nc = []
    in_ = 0
    ns = []
    out_ = 0
    r = 1.0
    for k in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if m.sqrt(x**2 + y**2) <= r:
            nc.append([x, y])
            in_ += 1
        else:
            ns.append([x, y])
            out_+= 1
    
    plt.scatter([p[0] for p in nc], [p[1] for p in nc], c='red')
    plt.scatter([p[0] for p in ns], [p[1] for p in ns], c='blue')
             
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    pi_eval = 4 * (in_ / n)
    print(f"Pi for {n} is {pi_eval}")
    print( in_, out_)
    return pi_eval

def sphere_volume(n, d, r=1): #Ex2, approximation
    in_ = 0
    
    for k in range(n):
        x = [random.uniform(-r, r) for x in range(d)]
        if sum(map(lambda xi: xi**2, x )) < r**2:
            in_ += 1 
    volume = (2 * r) ** d * (in_ / n)
    print(len(x))
    print(f'amount of inside points {in_}')
    print(f'volume: {volume}')
    return volume

def hypersphere_exact(d): #Ex2, real value
    # d is the number of dimensions of the sphere
    v = (m.pi ** (d/2))/m.gamma((d/2)+1)  
    return v

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
    
    with future.ProcessPoolExecutor(max_workers=np) as executor:
        na = [n] * np
        dim = [d] * np
        
        volume = executor.map(sphere_volume, na, dim)
        volumes = list(volume)
        volumex = sum(volumes) / np
        
        #print(f'volume:{volume}')        
        #print(f'time: {stop - start}')
    return volumex

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d, r=1,np=10):
    
    with future.ProcessPoolExecutor(max_workers=np) as ex:
        n_parts = n // np
        ni = [n_parts] * np
        dim = [d] * np   
        points_inside = list(ex.map(sphere_volume, ni, dim))
        
        mean = sum(points_inside) / np
        
    print(f'amount of inside points {points_inside}')
    print(f'volume: {mean}')
    return mean
    
def main():
    '''#Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
    #Ex2
    n = 100000
    d = 2
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    #Ex3
    n = 100000
    d = 11
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")
    
    sphere_volume_parallel1(n, d)'''

    #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    sphere_volume_parallel2(n, d)
    

if __name__ == '__main__':
	main()
