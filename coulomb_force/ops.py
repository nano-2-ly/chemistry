def coulomb_force(q1, q2):
    r = np.sqrt(pow(q1.pos[0] - q2.pos[0], 2) + pow(q1.pos[1] - q2.pos[1], 2))

    return q1.charge_quantity * q2.charge_quantity / (r**2)