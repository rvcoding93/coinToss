import random
def cointoss ():
    flips_count = input("How many times would you like to flip the coin?: ")
    flip_results = []
    heads = 0
    tails = 0
    for amount in range(flips_count):
            flip = random.randint(0,1)
            if flip == 0 :
                print ("Heads! ")
            flip_results.append(heads+1)
            else: 
            print("Tails! ")
            flip_results.append(tails+1)
    print(str(flip_results))
