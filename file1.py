from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,pair
import time

# Initialize a pairing group
group = PairingGroup('BN254')

# Define the points on the elliptic curve
g = group.random(G1)

# Define a random exponent
exp = group.random(ZR)

# Start the timer
start_time = time.time()

# Perform the exponentiation operation
result = g ** exp

# End the timer
end_time = time.time()

# Calculate the time difference in nanoseconds
time_diff_ns = (end_time - start_time) * 1e9

print("The result of the exponentiation operation is:", result)
print("Time taken in nanoseconds:", time_diff_ns)

