###################################
#                                 #
#   Created by Federico Nicotra   #
#                                 #
###################################

import traci

## Setup commands to execute sumo (or sumo-gui alternatively)
cmdSumo_OSM =   ["sumo", "-c", "C:/Users/Federico Nicotra/Sumo/2023-01-05-18-11-50/osm.sumocfg"] #created with osm web wizard
cmdSumo_S =  ["sumo", "-c", "C:/Users/Federico Nicotra/Sumo/Semaforo/incrocioSemplice.sumocfg"]
cmdSumo_A =  ["sumo", "-c", "C:/Users/Federico Nicotra/Sumo/Semaforo/incrocioSempliceA.sumocfg"]
cmdSumo_AM = ["sumo", "-c", "C:/Users/Federico Nicotra/Sumo/Semaforo/incrocioSempliceAM.sumocfg"]

## Choose one of the previous commands
cmdSumo = cmdSumo_AM

## Set your program IDs
prog_numbers = ["0", "1", "2"]
# prog_numbers = ["0"]

traffic_light_ID = "J1"
# traffic_light_ID = "436205045"

## Every element will contain the "simulation end time"
results = []

## Traffic scale factor
## "scale" variable turns on the scale factor for the traffic
scale = False
scale_factor = "1.5"

################

for prog_number in prog_numbers:
    ## Loading simulation
    traci.start(cmdSumo)

    ## Setting up the traffic light program
    traci.trafficlight.setProgram(traffic_light_ID, prog_number)
    print("RUNNING SIM. PROG: ", traci.trafficlight.getProgram(traffic_light_ID))

    ## Setting scale factor
    if scale : 
        traci.simulation.setScale(scale_factor)
    
    ## Running simulation ##
    ## Loops until all vehicles in the configuration had arrived
    ## The command   traci.simulationStep()   steps forword the simulation.
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

    ## Saves simulation time
    results.append([prog_number, traci.simulation.getTime()])

    ## Close simulation
    traci.close()

output_str = "\n"
if scale:
    output_str = output_str + "Scale factor: " + scale_factor + "\n"

for result in results:
    output_str = output_str + "Prog. " + result[0] + ": " + str(result[1]) + " s\n"

print(output_str)
