import random
K = 1
for N in range(0, 1000):
    K = ((0.2 * (1 - K / 100) + random.uniform(-0.15, 0.15)) * K) + K
    print(K)
def main():
