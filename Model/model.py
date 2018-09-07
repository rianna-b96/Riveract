import pandas as pd
import numpy as np
from gr4j import gr4j

params = { 'X1': 303.627616, 'X2': 0.32238919, 'X3': 6.49759466, 'X4': 0.294803885 }
states = { 'production_store': 0.60 * params['X1'], 'routing_store': 0.70 * params['X3'] }

rainfall = []
potential_evap =[]
simulated_flow = []

catchment_size = 2965

input_data = pd.read_csv(r"C:\Users\elija\Desktop\Maker Games\March 2001 GR4J Input.csv")

for i in range(len(input_data)):
    rainfall.append([input_data.iloc[i, 0]])
    potential_evap.append([input_data.iloc[i, 1]])
    simulated_flow.append(gr4j(rainfall[i], potential_evap[i], params, states))

output_data = np.c_[rainfall, potential_evap, np.array(simulated_flow)*catchment_size]

np.savetxt(r"C:\Users\elija\Desktop\Maker Games\March 2001 GR4J output.csv", output_data
           , header="Rainfall (mm),Potential Evaporation (mm),Simulated Flow (ML/day)", delimiter=',', comments='')