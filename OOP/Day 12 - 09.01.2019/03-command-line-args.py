# Command Line Arguments
import sys

# Print Arguments 
# argv = argument vector
print("Number of arguments: ", len(sys.argv), ' arguments.')


# here we print all the arguments
print("Arguments ", sys.argv)

# Remove Arguments
sys.argv.remove(sys.argv[0])

# here we print only the extra arguments
print("Arguments", sys.argv)

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum = sum + number
    except Exception:
        print("Bad input")

print(sum)


"""
first run:
________________________________

Day 12 - 09.01.2018> py .\03-command-line-args.py
Number of arguments:  1  arguments.
Arguments  ['.\\03-command-line-args.py']
Arguments []
0

second run:
________________________________
Day 12 - 09.01.2018> py .\03-command-line-args.py hello
Number of arguments:  2  arguments.
Arguments  ['.\\03-command-line-args.py', 'hello']
Arguments ['hello']
Bad input
0


third run:
________________________________
Day 12 - 09.01.2018> py .\03-command-line-args.py 2
Number of arguments:  2  arguments.
Arguments  ['.\\03-command-line-args.py', '2']
Arguments ['2']
2


fourth run:
________________________________
Day 12 - 09.01.2018> py .\03-command-line-args.py 2 5
Number of arguments:  3  arguments.
Arguments  ['.\\03-command-line-args.py', '2', '5']
Arguments ['2', '5']
7
"""