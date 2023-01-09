#initialization
import matplotlib.pyplot as plt
import numpy as np

# importing Qiskit
from qiskit import IBMQ, Aer, assemble, transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.ibmq import least_busy

# import basic plot tools
from qiskit.visualization import plot_histogram

from qiskit import execute
from quantuminspire.qiskit import QI
from getpass import getpass

def get_authentication():
    """Gets the authentication for connecting to the
       Quantum Inspire API.
    """
    print('Enter email:')
    email = input()
    print('Enter password')
    password = getpass()
    return email, password 


def initialize_s(qc, qubits):
    """Apply a H-gate to 'qubits' in qc"""
    for q in qubits:
        qc.h(q)
    return qc

if __name__ == '__main__':
    if 'authentication' not in vars().keys():
        authentication = get_authentication()
    QI.set_authentication_details(*authentication)
    qi_backend = QI.get_backend('QX single-node simulator')

    n = 2
    grover_circuit = QuantumCircuit(n)
    grover_circuit = initialize_s(grover_circuit, [0,1])

    # Oracle
    grover_circuit.cz(0,1) 

    # Diffusion operator (U_s)
    grover_circuit.h([0,1])
    grover_circuit.z([0,1])
    grover_circuit.cz(0,1)
    grover_circuit.h([0,1])
    grover_circuit.draw()

    print(grover_circuit)

    #q_obj = execute(grover_circuit, backend=qi_backend, shots=256)
    # q_result = q_obj.restult()
    # histogram = q_result.get_counts(grover_circuit)
    # plot_histogram(histogram)
