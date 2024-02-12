# I developed a quantum circuit simulator in Python using Qiskit, featuring gate application and state vector visualization.
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector

# Initializing a quantum circuit
qc = QuantumCircuit(2)  # 2 qubits

# Applying Quantum Gates 
qc.h(0)  # Hadamard gate on qubit 0
qc.cx(0, 1)  # CNOT gate on control qubit 0 and target qubit 1

# Visualizing the quantum circuit
print(qc) # Print the quantum circuit

#Simulating the quantum circuit
simulator = Aer.get_backend('statevector_simulator') # Getting the statevector simulator
job = execute(qc, simulator) # Executing the quantum circuit
result = job.result() # Getting the result

# Measuring the Qubits 
statevector = result.get_statevector() # Getting the statevector
print(statevector) # Print the statevector
