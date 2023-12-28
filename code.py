import numpy as np
import time
import hashlib

# System parameter and prime q
n = 1024
q = 12289

# Function to measure execution time
def measure_execution_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# Operations
def sample_gaussian_distribution():
    # Gaussian sampling with logβ = 17.1
    return np.random.normal(0, np.exp(17.1), n)

def componentwise_mul_scalar(arr, scalar):
    return (arr * scalar) % q

def componentwise_mul(arr1, arr2):
    return (arr1 * arr2) % q

def componentwise_mul_add(arr1, arr2, add):
    return (arr1 * arr2 + add) % q

def characteristic_function(arr):
    return np.array([1 if x == 0 else 0 for x in arr])

def sha3_hash(data):
    hasher = hashlib.sha3_512()
    hasher.update(data)
    return hasher.digest()

# Generate random arrays for testing
arr1 = np.random.randint(low=0, high=q, size=n)
arr2 = np.random.randint(low=0, high=q, size=n)
add = np.random.randint(low=0, high=q, size=n)
scalar = np.random.randint(low=0, high=q)

# Function to measure average execution time over multiple runs
def measure_average_execution_time(func, runs, *args):
    total_time = 0
    for _ in range(runs):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / runs

# Number of runs for each operation
runs = 10000

# Measure average execution times
average_times = {}
average_times['T(Ge)'] = measure_average_execution_time(sample_gaussian_distribution, runs)
average_times['T(smul)'] = measure_average_execution_time(componentwise_mul_scalar, runs, arr1, scalar)
average_times['T(pmul)'] = measure_average_execution_time(componentwise_mul, runs, arr1, arr2)
average_times['T(pma)'] = measure_average_execution_time(componentwise_mul_add, runs, arr1, arr2, add)
average_times['T(cha)'] = measure_average_execution_time(characteristic_function, runs, arr1)
average_times['T(h)'] = measure_average_execution_time(sha3_hash, runs, b"Sample Data for Hashing")

# Convert average times from seconds to nanoseconds
average_times_ns = {key: value * 1e9 for key, value in average_times.items()}
for i in average_times_ns:
    print(f"{i}:{average_times_ns[i]}")
