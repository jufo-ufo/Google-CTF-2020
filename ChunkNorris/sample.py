import random
from Crypto.Util.number import * # pylint: disable=unused-wildcard-import
import gmpy2
import sys

a = 0xe64a5f84e2762be5
chunk_size = 64
bits = 1024

def gen_prime(bits):
  s = random.getrandbits(chunk_size)

  while True:
    s |= 0xc000000000000001
    p = 0
    for _ in range(bits // chunk_size):
      p = (p << chunk_size) + s
      s = a * s % 2**chunk_size
    if gmpy2.is_prime(p):
      return p

def progressbar(sum, iteration, suffix="", prefix="", length=50):
    percent = ("{0:." + str(1) + "f}").format(100 * (iteration / sum))
    filledLength = int(length * iteration // sum)
    bar = "█" * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (suffix, bar, percent, prefix))
    sys.stdout.flush()

if len(sys.argv) < 3:
    sys.stderr.write("Usage: <file> <iterations>\n")
    sys.stderr.flush()
    exit()

iterations = int(sys.argv[2])
data = []

for i in range(iterations):
    data.append(gen_prime(bits))
    progressbar(iterations, i+1, "Generating :")

print()

with open(sys.argv[1], "w") as f:
    for i in range(iterations):
        f.write(hex(data[i]) + "\n")
        progressbar(iterations, i+1, "Saving     :")

print("\nDone")