import random

# Constants
total_packets = 100
bits = 100
error_prob_0_to_1 = 0.03
error_prob_1_to_0 = 0.01
error_threshold = 5

# Function to simulate packet transmission
def simulate_packet_transmission():
    packet = [random.choice([0, 1]) for i in range(bits)]
    received_packet = []

    for bit in packet:
        if bit == 0:
            error = random.random() < error_prob_0_to_1
            received_bit = 1 if error else 0
        else:
            error = random.random() < error_prob_1_to_0
            received_bit = 0 if error else 1
        
        received_packet.append(received_bit)

    return received_packet

# Function to decode a packet
def decode_packet(packet):
    error_count = sum(1 for bit in packet if bit != 0)
    return error_count <= error_threshold

# Simulate transmission and count correctly decoded packets
correctly_decoded_count = 0

for i in range(total_packets):
    received_packet = simulate_packet_transmission()
    if decode_packet(received_packet):
        correctly_decoded_count += 1

# Calculate relative frequency and theoretical probability
relative_frequency = correctly_decoded_count / total_packets
theoretical_probability = (1 - error_prob_0_to_1) ** (bits - error_threshold)

# Print results
print("Number of Correctly Decoded Packets:", correctly_decoded_count)
print("Relative Frequency of Correctly Decoded Packets:", relative_frequency)
print("Theoretical Probability of Correctly Decoded Packet:", theoretical_probability)

        
