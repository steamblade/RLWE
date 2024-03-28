import numpy as np
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
import timeit

# System parameter and prime q
n = 1024
q = 12289

# Original operations
def sample_gaussian_distribution():
    np.random.normal(0, np.exp(17.1), n)

def componentwise_mul_scalar(arr, scalar):
    (arr * scalar) % q

def componentwise_mul(arr1, arr2):
    (arr1 * arr2) % q

def componentwise_mul_add(arr1, arr2, add):
    (arr1 * arr2 + add) % q

def characteristic_function(arr):
    np.array([1 if x == 0 else 0 for x in arr])

# Cryptographic operations
def generate_ec_key():
    ec.generate_private_key(ec.SECP384R1(), default_backend())

def ec_sign_operation():
    private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
    private_key.sign(b"test data", ec.ECDSA(hashes.SHA256()))

def sha256_hash():
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(b"test data")
    digest.finalize()

# Generate random arrays for testing
arr1 = np.random.randint(low=0, high=q, size=n)
arr2 = np.random.randint(low=0, high=q, size=n)
add = np.random.randint(low=0, high=q, size=n)
scalar = np.random.randint(low=0, high=q)

# Measure and print average times using timeit
operations = [
    ('sample_gaussian_distribution', lambda: sample_gaussian_distribution()),
    ('componentwise_mul_scalar', lambda: componentwise_mul_scalar(arr1, scalar)),
    ('componentwise_mul', lambda: componentwise_mul(arr1, arr2)),
    ('componentwise_mul_add', lambda: componentwise_mul_add(arr1, arr2, add)),
    ('characteristic_function', lambda: characteristic_function(arr1)),
    ('generate_ec_key', generate_ec_key),
    ('sha256_hash', sha256_hash),
    ('ec_sign_operation', ec_sign_operation)
]

for name, func in operations:
    avg_time_ns = timeit.timeit(func, number=1000) * 1e6  # Convert to nanoseconds
    print(f"{name}: {avg_time_ns:.2f} ns")
