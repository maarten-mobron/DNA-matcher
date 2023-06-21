import csv
import sys

def main():

    # Check for command-line usage
    if (len(sys.argv) != 3):
        print("Usage: python dna.py data.csv sequence.txt")

    # Read database file into a variable
    with open(sys.argv[1], newline='') as file:
        reader = csv.DictReader(file)
        DB = []
        for row in reader:
            DB.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], newline='') as file:
        reader = csv.reader(file)
        for data in reader:
            DNA = data

    # Find longest match of each STR in DNA sequence
    # extract str markers from DB
    with open(sys.argv[1], newline='') as file:
        reader = csv.reader(file)
        str_markers = next(reader)[1:]

    # find longest STR matches
    STR_match = {}
    for STR in str_markers:
        STR_match.update({STR: str(longest_match(DNA[0], STR))})

    # Check database for matching profiles
    match = ""
    for person in DB:
        if all(key in person and person[key] == STR_match[key] for key in STR_match):
            match = person['name']

    if match:
        print(match)
    else:
        print("No match")

    return


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
