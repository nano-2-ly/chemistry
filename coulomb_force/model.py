from ops import *
import numpy as np
class molecule(object):
    def __init__(self,
    molecule = None,
    mass = None,
    charge_quantity = 0,
    pos = None,
    name = None):

        self.molecule = molecule
        self.mass = mass
        self.charge_quantity = charge_quantity
        self.pos = np.array(pos, dtype = float)

        self.vector = np.array([0,0], dtype = float)

class system(object):
    def __init__(self,
    size):
        self.system_space = np.zeros(size,dtype = float)
        self.gravitation_field_space = np.array(size,dtype = float)
        self.electric_field_space = np.zeros([size[0], size[1], 1 ,2],dtype = float)

        self.system_size = size

    def make_electric_field(self, molecule_list):
        for molecule in molecule_list:
            for i in range(self.system_size[0]):
                for j in range(self.system_size[1]):
                    vector = self.calculate_electric_field(molecule,[float(i),float(j)])
                    self.electric_field_space[i,j,0] += vector

    def calculate_electric_field(self, molecule, pos):
        r = np.sqrt(pow(molecule.pos[0] - pos[0], 2) + pow(molecule.pos[1] - pos[1], 2))
        direction_vector = [pos[0] - molecule.pos[0] , pos[1] - molecule.pos[1]]
        #direction_vector_size = np.sqrt(pow(direction_vector[0],2) + pow(direction_vector[1],2))
        direction_vector = direction_vector / r 

        coulomb_force_value = molecule.charge_quantity / pow(r,2)
        electric_field = direction_vector * coulomb_force_value

        return electric_field