from pwn import *
import time
import random

class Verifier:
    def __init__(self, seed, n, a, b):
        self.state = seed
        self.n = n
        self.a = a
        self.b = b
        self.previous_states = set()

    def next_state(self, x):
        new_state = (self.a * self.state  + self.b * (1 - x)) % self.n
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

conn = remote('localhost', 1337)  # Replace with the actual IP and port
k = int(time.time())
conn.recvuntil(b"n=")
n = int(conn.recvline().strip().decode())
print(f"{n=}")
conn.recvuntil(b"b=")
b = int(conn.recvline().strip().decode())
print(f"{b=}")
print(conn.recvline())

while True:
    random.seed(k)
    seed = random.randrange(1, n)
    a = random.randrange(1, n)
    guess = random.randrange(1, n)
    if guess == b:
        break
    k+=1
    print(k)

state = seed
verifier = Verifier(seed, n, a, b)
for i in range(128):
    
    # Get the secret bit
    x = verifier.get_secret_bit()

    # Calculate the user state based on LCG logic
    state = verifier.next_state(x)

    # Receive the prompt for the round
    conn.recvuntil(b"Provide state: ")

    # Send the calculated state back to the verifier
    conn.sendline(str(state).encode())
    print(conn.recvline())

print(conn.recvline())
# print(conn.recvline())

# Close the connection
conn.close()