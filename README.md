# 2022_microsoft_ionq_challenge
MIT iQuHACK 2022 x Microsoft x IonQ Challenge


<p align="left">
  <a href="https://azure.microsoft.com/en-us/solutions/quantum-computing/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488491-609828a4-cd1f-4076-b5b2-a8d9fc2d0fa4.png" width="30%"/> </a>
  <a href="https://ionq.com/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488159-da95eb05-9277-4abe-b1ba-b49871d563ed.svg" width="20%" style="padding: 1%;padding-left: 5%"/></a>
  <a href="https://iquhack.mit.edu/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151647370-d161d5b5-119c-4db9-898e-cfb1745a8310.png" width="8%" style="padding-left: 5%"/> </a>
  
</p>


# QUANTUM-CLASSICAL TIC-TAC-TOE (QUICK QUACK TOE )

## TEAM : QUICK QUACK TOE ![QUA](https://user-images.githubusercontent.com/68440833/151708447-089d7cc1-dff2-41fa-b1b8-e8d48d321952.png)


For the **MIT iQuHACK 2022 x Microsoft x IonQ Challenge** we decided to create a unique **Quantum-classical tic-tac-toe**.

[Presentation Slides](https://docs.google.com/presentation/d/1tBLsqmwnBltVq_fbVn21o7O-7fPXAK1HzJ5LmiDLOyc/edit?usp=sharing)

The game explores superposition properties of qubits as follows:


 - The game has 2 players, player1 and player2
 - The tiles can be marked in a Classical way or in a Quantum way.
 - The game allows a player to switch between two modes: **Quantum mode** or **Classical mode**.
 - By default, Player1 makes a tile with a |0> and player2 makes a tile with a |1>.
 - Quantum mode has an interesting twist,  During a player turn, a player can decide to entangle two tiles instead of marking a tile.
 -  If that is the case, then the entangled tiles can not be marked for any other player during the game.
 - Once all the tiles are marked or entangled the quantum circuit of the game is initialized and the qubits are measured reviling the final state of the game.
 - We then run an Error-correcting algorithm by repetition.
 - Who ever has 3 in a line wins. If both will then the code is run again until one one wins.


The repository consists of two main project files : 
- game_interface.py
- back-end.py


The maiin component of the game is **back-end.py**

We used 9 different qubits to represent the tiles and then designed an algorithm to allow entaglement when players switch to Quantum mode.


| 6 | 7 | 8 |
|---|---|---|
| 3 | 4 | 5 |
| 0 | 1 | 2 |


We take the inputs of both player and respresent them as Quantum states, such that we have a list of marking by player_1 (whose states are *|0>* ) and list of inputs from Player_2 whose states are *|1>*)

```
l_player_1 = [0] #list of qbits cell numbers inicialized to 0
l_player_2 = [2,3] #list of qbits cell numbers inicialized to 1
l_entangled = [(1,6),(7,8),(4,5)] #list of pairs of cells that need to be entangled to |01>+|10>

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(9, 9)
circuit.name = "Tic tac toe"


for inx  in range(len(l_player_2)):
    circuit.x(l_player_2[inx])
for inx in range(len(l_entangled)):
    circuit.h(l_entangled[inx][0])
    circuit.x(l_entangled[inx][1])
    circuit.cx(l_entangled[inx][0],l_entangled[inx][1])
circuit.measure(list(range(9)), list(range(9)))

# Print out the circuit
circuit.draw()
```
This generates the quantum circuits representing the tic toc toe game, based on the 3 input lists.

![image](https://user-images.githubusercontent.com/68440833/151706963-23be38d3-669f-4aeb-b389-0745b07988e8.png)





![image (1)](https://user-images.githubusercontent.com/68440833/151707525-40dd0ba4-3e33-4e8b-9dfd-677cacf672c8.png)




print(result.get_counts())
print(list(map(lambda x: int(x),list(list(result.get_counts().keys())[0][::-1]))))


We then transform  output register string into a list of integers in the right order so the first element corresponds to the first tile
```
print(result.get_counts())
print(list(map(lambda x: int(x),list(list(result.get_counts().keys())[0][::-1]))))

result:
{'010011110': 1}
[0, 1, 1, 1, 1, 0, 0, 1, 0]
```
0 0 1

1 0 1

0 1 1

In this case Player 2 win : )



## Team Experience (MIT iQuHACK 2022).

MIT iQUHACK 2022 was a really amzing experience. We all are from diverse communities  and educational  background but this hackathon had bring us together  to work on a single goal. We made some new friends , explored the operation on real Quantum hardware, Strengthen our knowledge on Quantum computing and Qiskit as a whole.
It is really an honour to participate in the Hackathon.







## TEAM : QUICK QUACK TOE ![QUA](https://user-images.githubusercontent.com/68440833/151708447-089d7cc1-dff2-41fa-b1b8-e8d48d321952.png) TEAM




<table>
<tr>
    <td align="center"><a href="https://github.com/jofa5499"><img src="https://github.com/jofa5499.png" width="100px;" alt=""/><br /><sub><b>Josep Fargas</b></sub></a><br /><a href="https://github.com/physiopy/phys2bids/commits?author=viacovella" title="Code">💻</a></td>
</tr>
<tr>
    <td align="center"><a href="https://github.com/amritphuyal"><img src="https://github.com/amritphuyal.png" width="100px;" alt=""/><br /><sub><b>Amrit Prasad Phuyal</b></sub></a><br /><a href="https://github.com/physiopy/phys2bids/commits?author=viacovella" title="Code">💻</a></td>
</tr>
<tr>
    <td align="center"><a href="https://github.com/Chakhriya-c"><img src="https://github.com/Chakhriya-c.png" width="100px;" alt=""/><br /><sub><b>Chakhriya Chantharakhami</b></sub></a><br /><a href="https://github.com/physiopy/phys2bids/commits?author=viacovella" title="Code">💻</a></td>
</tr>
<tr>
    <td align="center"><a href="https://github.com/rohittbhusal/"><img src="https://github.com/rohittbhusal/.png" width="100px;" alt=""/><br /><sub><b>Rohit Bhusal</b></sub></a><br /><a href="https://github.com/physiopy/phys2bids/commits?author=viacovella" title="Code">💻</a></td>
</tr>
<tr>
    <td align="center"><a href="https://github.com/Alfaxad"><img src="https://github.com/Alfaxad.png" width="100px;" alt=""/><br /><sub><b>Alfaxad Eyembe</b></sub></a><br /><a href="https://github.com/physiopy/phys2bids/commits?author=viacovella" title="Code">💻</a></td>
</tr>
</table>






