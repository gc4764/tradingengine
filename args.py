import argparse


parser = argparse.ArgumentParser()

parser.add_argument("fname", type=str)
parser.add_argument("lname", type=str)
parser.add_argument("--mob", action= "store_true")
#parser.add_argument('-m', "--mob", type=int)



args = parser.parse_args()


print(args)
print()
print(args.fname)
print(args.lname)
print(args.mob)
