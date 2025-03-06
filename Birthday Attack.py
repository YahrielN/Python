import random
import hashlib


# Variables/setup
n = 80  # value of 'n' used in equation
count = 1
hashToMsg = {}  # Matches the correct mi with ti
file = open("hash.csv", "w")  # Making file for random values and hashes


# Function to takes in Hex string and encodes it using <hashlib>
# Returning Badhash40 = 40-bits or 10 hex values
def BadHash40(hexInput):
   encode = bytes.fromhex(hexInput)
   hash40 = hashlib.sha256(encode).hexdigest()
   return hash40[0:10]


# If collision occurs run this function
def collision():
   print("\t\tFOUND COLLISION!")
   print(f"Found collision after: {count} iterations\n")
   print(f"BadHash40({hexMsg}) = {hash40}")
   print("AND")
   print(f"BadHash40({hashToMsg[hash40]}) = {hash40}\n")
   print(f"Collides with the Hash = {hash40}")
   print("---------------------------------------------")


for i in range(0, int(2 ** (n / 2))):
	# Random number generator for mi set to 256-bits
	randomMsg = random.getrandbits(256)

	# Converting random message to hex and removing the prefix
	hexMsg = hex(randomMsg)[2:]

	# Check if Hex is 64 char with no leading zero.
	while len(hexMsg) != 64:
		hexMsg = "0" + hexMsg

	# Calling BadHash40 to get the hash and writing into our file
	hash40 = BadHash40(hexMsg)
	file.write(f"{hexMsg}, {hash40}\n")

	# If hash found in the message, trigger collision and print results
	if hash40 in hashToMsg:
		collision()
		# Close file and exit program after collision
		file.close()
		exit()

	hashToMsg[hash40] = hexMsg
	count = count + 1

# If no collision happens after loop ends close file
print("Found 'NO' collision in the hash functions.")
print("\tRun the program again!")
print("---------------------------------------------")
file.close()
