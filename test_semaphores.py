###################################
#                                 #
#   Created by Federico Nicotra   #
#                                 #
###################################

import traci

## Setup commands to execute sumo (or sumo-gui eventually)
cmdSumo_ =   ["sumo", "-c", "C:/Users/Federico Nicotra/Sumo/2023-01-05-18-11-50/osm.sumocfg"] #created with osm web wizard
cmdSumo_S =  ["sumo", "-c", "C:/Users/Federico Nicotra/Sumo/Semaforo/incrocioSemplice.sumocfg"]
cmdSumo_A =  ["sumo", "-c", "C:/Users/Federico Nicotra/Sumo/Semaforo/incrocioSempliceA.sumocfg"]
cmdSumo_AM = ["sumo", "-c", "C:/Users/Federico Nicotra/Sumo/Semaforo/incrocioSempliceAM.sumocfg"]

## Choose one of the previous commands
cmdSumo = cmdSumo_A


traffic_light_ID = "J1"
# traffic_light_ID = "436205045"

test1 = test2 = test3 = 0

## Traffic scale factor 
scale = False
scale_factor = "1.5"

## Program IDs
first_program_number = "0"
second_program_number = "1"
third_program_number = "2"

################

## Loading simulation
traci.start(cmdSumo)
## Setting up the traffic light program
traci.trafficlight.setProgram(traffic_light_ID, first_program_number)
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
test1 = traci.simulation.getTime()

## Close simulation
traci.close()

################

traci.start(cmdSumo)
traci.trafficlight.setProgram(traffic_light_ID, second_program_number)
print("RUNNING SIM. PROG: ", traci.trafficlight.getProgram(traffic_light_ID))
if scale : 
    traci.simulation.setScale(scale_factor)
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

test2 = traci.simulation.getTime()
traci.close()

################

traci.start(cmdSumo)
traci.trafficlight.setProgram(traffic_light_ID, third_program_number)
print("RUNNING SIM. PROG: ", traci.trafficlight.getProgram(traffic_light_ID))
if scale : 
    traci.simulation.setScale(scale_factor)
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

test3 = traci.simulation.getTime()
traci.close()

################

print("PROG ", first_program_number,": " , test1, 
    "\nPROG ", second_program_number, ": ", test2,
    "\nPROG ", third_program_number, ": ", test3, sep='')
# print("PROG 0: ", test1)