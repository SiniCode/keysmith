from time import time
import services.keys

def creating_keys_of_n_bits_test(n):
    seconds = []

    for _ in range(100):
        start = time()
        services.keys.create_keys(n)
        finish = time()
        seconds.append(finish - start)

    print(f"The average {n}-bit key creation time: {sum(seconds)/100} seconds")

if __name__ == "__main__":

    creating_keys_of_n_bits_test(1024)
    creating_keys_of_n_bits_test(2048)
