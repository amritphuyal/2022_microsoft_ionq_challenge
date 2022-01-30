#!/usr/bin/env python
# coding: utf-8

# In[3]:


from azure.quantum import Workspace
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from azure.quantum.qiskit import AzureQuantumProvider
from qiskit import assemble


provider = AzureQuantumProvider (
    resource_id = "/subscriptions/b1d7f7f8-743f-458e-b3a0-3e09734d716d/resourceGroups/aq-hackathons/providers/Microsoft.Quantum/Workspaces/aq-hackathon-01",
    location = "eastus"
)
workspace = Workspace (
    subscription_id = "b1d7f7f8-743f-458e-b3a0-3e09734d716d",
    resource_group = "aq-hackathons",
    name = "aq-hackathon-01",
    location = "eastus"
)

### tic toc toe ###

######################################
#           #             #          #   
#     6     #     7       #    8     # 
#           #             #          # 
######################################
#           #             #          # 
#     3     #     4       #    5     # 
#           #             #          # 
######################################
#           #             #          #  
#     0     #     1       #     2    #   
#           #             #          # 
######################################

l_player_1 = [0] #list of qbits cell numbers inicialized to 0
l_player_2 = [2,3] #list of qbits cell numbers inicialized to 1
l_entangled = [(1,6),(7,8),(4,5)] #list of pairs of cells that need to be entangled to |01>+|10>

#translate from lists to initial state matrix
l_initial_ordered = [0,0,0,0,0,0,0,0,0]
for inx in range(len(l_player_1)):
    l_initial_ordered[l_player_1[inx]]=0
for inx in range(len(l_player_2)):
    l_initial_ordered[l_player_2[inx]]=1  
entg_num = 1  
for inx in range(len(l_entangled)):
    l_initial_ordered[l_entangled[inx][0]]='e'+str(entg_num )   
    l_initial_ordered[l_entangled[inx][1]]='e'+str(entg_num  )
    entg_num +=1

print('This the initial table state inputed by the user:\n0 corresponds to player 1, 1 corresponds to player 2,\n e1,e2,e3... corresponds to entangled tiles')
print('-----\n'+str(l_initial_ordered[6])+'|'+str(l_initial_ordered[7])+'|'+str(l_initial_ordered[8]))
print('-----\n'+str(l_initial_ordered[3])+'|'+str(l_initial_ordered[4])+'|'+str(l_initial_ordered[5]))
print('-----\n'+str(l_initial_ordered[0])+'|'+str(l_initial_ordered[1])+'|'+str(l_initial_ordered[2]))
print('-----')


# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(9, 9)
circuit.name = "Tic toc toe"

for inx  in range(len(l_player_2)):
    circuit.x(l_player_2[inx])

for inx in range(len(l_entangled)):
    circuit.h(l_entangled[inx][0])
    circuit.x(l_entangled[inx][1])
    circuit.cx(l_entangled[inx][0],l_entangled[inx][1])




#circuit.h(0)
#circuit.cx(0, 1)
#circuit.cx(1, 2)
circuit.measure(list(range(9)), list(range(9)))

# Print out the circuit
circuit.draw()



# In[ ]:


#simulator_backend = provider.get_backend("ionq.simulator")
simulator_backend = provider.get_backend("ionq.qpu")
job = simulator_backend.run(circuit, shots=1)
job_id = job.id()
print("quantum tic", job_id)
job_monitor(job)
result = job.result()
print(result.get_counts())


# In[ ]:


l_final_ordered=list(map(lambda x: int(x),list(list(result.get_counts().keys())[0][::-1])))
print(l_final_ordered)
#list with ordered cells
print('The colapsed state is:')
print('-----\n'+str(l_final_ordered[6])+'|'+str(l_final_ordered[7])+'|'+str(l_final_ordered[8]))
print('-----\n'+str(l_final_ordered[3])+'|'+str(l_final_ordered[4])+'|'+str(l_final_ordered[5]))
print('-----\n'+str(l_final_ordered[0])+'|'+str(l_final_ordered[1])+'|'+str(l_final_ordered[2]))
print('-----')
print('Player 2 won!')

