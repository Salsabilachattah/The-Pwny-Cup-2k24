from math import gcd
from Crypto.Util.number import getPrime
import random
import time
import socket
from secret import FLAG

class Verifier:
    def __init__(self, seed, n, a, b):
        self.state = seed
        self.n = n
        self.a = a
        self.b = b
        self.previous_states = set()

    def next_state(self, x):
        new_state = (self.a * self.state + self.b * (1 - x)) % self.n
        self.state = new_state
        return new_state

    def get_secret_bit(self) -> int:
        return random.randrange(2)

    def verify(self, user_state, x, conn):
        if user_state in self.previous_states:
            conn.send(b"Error: repeated state\n")
            return False

        self.previous_states.add(user_state)

        self.next_state(x)

        if self.state != user_state:
            return False

        return True

def main(conn):
    conn.send(b"Welcome to our zkpwarmup challenge baby zkp!\n")

    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    conn.send(f"{n=}\n".encode())

    random.seed(int(time.time()))
    seed = random.randrange(1, n)
    a = random.randrange(1, n)
    b = random.randrange(1, n)
    conn.send(f"{b=}\n".encode())

    conn.send(b"Can you prove that you know the LCG seed without revealing it to the verifier?\n")
    verifier = Verifier(seed, n, a, b)
    n_rounds = 128
    for i in range(n_rounds):
        x = verifier.get_secret_bit()

        conn.send(b"Provide state: ")
        try:
            state = int(conn.recv(1024).strip()) % n
        except ValueError:
            conn.send(b"Invalid input!\n")
            continue
        except BrokenPipeError:
            conn.send(b"Connection Error!\n")
            continue

        if verifier.verify(state, x, conn):
            conn.send(f"Verification passed! {n_rounds - i - 1} rounds remaining\n".encode())
        else:
            conn.send(b"Verification failed!\n")
            return

    
    conn.send(f"You've convinced the verifier you know the LCG seed. {FLAG}\n".encode())

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 1337))
    server.listen(50)

    while True:
        client, addr = server.accept()
        main(client)
        client.close()
