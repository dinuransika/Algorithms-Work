import statistics

fo = open("p059_cipher.txt", "r")
read = fo.read()
lis = read.split(",")
lis = [int(x) for x in lis]
print(min(lis), statistics.mode(lis))
read = fo.close()
