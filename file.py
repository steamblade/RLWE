from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,pair
import time

# Initialize a pairing group
group = PairingGroup('BN254')

# Define the points on the elliptic curve
g1 = group.random(G1)
g2 = group.random(G2)

# Start the timer
start_time = time.time()

# Perform the bilinear pairing operation
pairing_result = pair(g1, g2)

# End the timer
end_time = time.time()

# Calculate the time difference in nanoseconds
time_diff_ns = (end_time - start_time) * 1e9

print("The result of the bilinear pairing operation is:", pairing_result)
print("Time taken in nanoseconds:", time_diff_ns)

