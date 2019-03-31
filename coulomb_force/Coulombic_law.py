import numpy as np
from utils import *
from model import *


import matplotlib.pyplot as plt

unit_time = 0.1

h = molecule(molecule = 'h',
            mass = 1,
            charge_quantity = 5.0,
            pos = [2,2],
            name = 'hydrogen')

he = molecule(molecule = 'he',
            mass = 4,
            charge_quantity = 2.0,
            pos = [50,0],
            name = 'helium')

f = molecule(molecule = 'f-',
            mass = 9,
            charge_quantity = -5.0,
            pos = [6,6],
            name = 'fluorine')

system = system([10,10])
system.make_electric_field([h,f])

print(system.system_space)

fig, ax = plt.subplots()
q = ax.quiver(np.arange(0,system.system_size[0],1), np.arange(0,system.system_size[1],1), system.electric_field_space[:,:,0,1], system.electric_field_space[:,:,0,0], scale = 100)

plt.show()
'''
while 1: 
    h.pos[0] = (h.vector[0]/h.mass) * unit_time + h.pos[0]
    h.pos[1] = (h.vector[1]/h.mass) * unit_time + h.pos[1]
    print(h.pos)
'''