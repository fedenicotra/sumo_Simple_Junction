###################################
#                                 #
#   Created by Federico Nicotra   #
#                                 #
###################################

import traci
import numpy as np
import matplotlib.pyplot as plt

cmdSumo_osm = ["sumo", "-c", "C:/Users/Federico Nicotra/Sumo/2023-01-05-18-11-50/osm.sumocfg"]
cmdSumo_S  =  ["sumo", "-c", "C:/Users/Federico Nicotra/Sumo/Semaforo/incrocioSemplice.sumocfg"]

cmdSumo = cmdSumo_S
traci.start(cmdSumo)
vehicle = "t_1.0"
sp = []
ac = []
found = False
steps = 0
while traci.simulation.getMinExpectedNumber() > 0:
    vehicles = traci.vehicle.getIDList()
    # if steps % 50: print(vehicles)
    if vehicle in vehicles:
        s = traci.vehicle.getSpeed(vehicle)
        a = traci.vehicle.getAcceleration(vehicle)
        if(s >= 0): 
            sp.append(s)
            found = True
        ac.append(a)
    else:
        if found:
            break
    traci.simulationStep()
    steps += 1

traci.close()
x_sp = np.arange(0, len(sp), 1)
x_ac = np.arange(0, len(ac), 1)

plt.plot(x_sp, sp, 'b-', label='Speed (m/s)')
plt.plot(x_ac, ac, 'r-', label='Acceleration (m/s^2)')
plt.legend(loc='best')
plt.title('Velocity and acceleration plot: ' + vehicle)
plt.xlabel('Time since depart (s)')
plt.show()