import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        exit("ERROR")

    # TODO: Read database file into a variable
    database = dict()
    names = []
    count= 0
    try:
        with open(sys.argv[1], "r") as file:

            reader = csv.reader(file)

            row1 = next(reader)
            for row in reader:

                names.append(row[0])

                str_sequences = dict()


                for i in range(1, len(row)):
                        str_sequences[row1[i]] = row[i]

                database[count] = str_sequences
                count += 1
    except:
        exit("error")
    # TODO: Read DNA sequence file into a variable
    try:
        with open(sys.argv[2]) as file:
            sequences = file.read().replace('\n', '')
    except:
        exit("error")

    # TODO: Find longest match of each STR in DNA sequence
    length = len(row1)
    str_sequences = dict()
    for i in range(1, length):


        str_sequences[row1[i]] = longest_match(sequences, row1[i])


    # TODO: Check database for matching profiles
    winner = None
    count = 0
    length = len(str_sequences)
    for i in range(len(database)) :
        for sequence in str_sequences:
            value_database = database[i][sequence]
            str_value = str_sequences[sequence]
             
            if count < length:

                if int(value_database) is int(str_value):

                    winner = names[i]
                    count += 1
                    bool = False
            else:
                bool = True
                break
    if winner != None and bool == True:
        print(winner)
    else:
        print("No match")



def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
