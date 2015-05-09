import numpy
import matplotlib.pyplot as plt
import math

def matflow(t=20, materials="Cd", module="CdTe", peak = 10000.0, mean=20.0, std= 1.0, random=False):
    '''
    Returns end-of-life material flow at time t years
    time t is integer unit years
    material is string
    module is string
    peak is a interger units watts
    mean lifetime is integer unit: years
    standard deviation lifetime is  integer unit: years
    random is binary assigns random number to composition
    '''
    #lookup up and print material values - density, composition
    comp = 0.001 #g/m2 dens = 39 #g/cm3
    #lookup up  and print module values - efficiency, growth alpha & beta, capacity factor
    alpha = 0.4; beta = 0.2; eff = 0.14; capf = 0.9 #watt/m2; 
    
    #initialize values - k ,m, lambda, curve, availability
    k  = len(module); m = len(materials)
    d = list() #lambda list
    curve = list()
    a = numpy.zeros((t,t)) #availabilty matrix
    
    #for loop calculate lambda
    for j in range(1,t+1):
        print j
        d.append(math.exp((j-mean)/(2*(std)**2))/(2*math.pi*(std)**2))
    
    # for loop calculate product growth curve
    for j in range(1,t+1):
        print j
        curve.append(peak/(1+alpha*math.exp(-1*beta*j)))
             
    # calcaulate material availability
    for j in range(0,t,1):
        print j
        for i in range(0,t,1):
            print a
            a[i,j]=d[j]*curve[i]*comp/capf
    #sum rows of availability
    #plot scurve each row
    #plot availability row summary
    x = range(0,t,1)
    y = list(a[:,1])
    return plt.scatter(x,y)
    plt.show()