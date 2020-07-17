"""Function to process and print produce summaries"""

def read_produce_summary(day, file):
    """Function to read text file"""

    for line in file:
        line = line.rstrip()
        tokens = line.split('|')

        print_produce_summary(day, tokens)


def print_produce_summary(day, tokens):
    """Function to tokenize and print summary"""

    melon = tokens[0]
    count = int(tokens[1])
    amount = tokens[2]

    print(f"Delivered {count} {melon}s for a total of ${amount}")



def process_produce_summary(day, filename):
    """Main function to produce report"""

    file = open(filename)

    print(f"Day {day}:")

    read_produce_summary(day, file)

    file.close()


process_produce_summary(1, "um-deliveries-20140519.txt")
process_produce_summary(2, "um-deliveries-20140520.txt")
process_produce_summary(3, "um-deliveries-20140521.txt")









