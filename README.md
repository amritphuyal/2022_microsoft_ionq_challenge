# 2022_microsoft_ionq_challenge
MIT iQuHACK 2022 x Microsoft x IonQ Challenge


<p align="left">
  <a href="https://azure.microsoft.com/en-us/solutions/quantum-computing/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488491-609828a4-cd1f-4076-b5b2-a8d9fc2d0fa4.png" width="30%"/> </a>
  <a href="https://ionq.com/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488159-da95eb05-9277-4abe-b1ba-b49871d563ed.svg" width="20%" style="padding: 1%;padding-left: 5%"/></a>
  <a href="https://iquhack.mit.edu/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151647370-d161d5b5-119c-4db9-898e-cfb1745a8310.png" width="8%" style="padding-left: 5%"/> </a>
  
</p>


# QUANTUM-CLASSICAL TIC-TAC-TOE

For the **MIT iQuHACK 2022 x Microsoft x IonQ Challenge** we decided to create a unique **Quantum-classical tic-tac-toe**.

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
