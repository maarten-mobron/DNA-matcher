# DNA Matcher

## Description
The DNA Matcher is a program that compares a given DNA sequence with a database of profiles to determine if there is a match. It utilizes short tandem repeats (STR) markers, which are specific sequences of nucleotides that repeat consecutively, to identify potential matches in the database.

DNA is a sequence of molecules called nucleotides arranged in a double helix shape. Each nucleotide contains one of four bases: A, C, G, or T. While some parts of the DNA sequence are similar among humans, others vary more. Short Tandem Repeats (STRs) are short sequences of DNA that repeat consecutively at specific locations. The number of repeats varies among individuals. By analyzing multiple STRs, the accuracy of DNA profiling improves. The probability of two DNA samples matching purely by chance decreases significantly when multiple STRs are considered. If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other). The FBI's DNA database, called CODIS, uses 20 different STRs.

## How It Works

1. The program takes two command-line arguments: a CSV file containing the DNA database and a text file containing the DNA sequence to be matched.
2. The DNA sequence is compared with the profiles in the database using the STR markers.
3. For each STR marker, the program finds the longest consecutive run of the marker in the DNA sequence.
4. It then checks each person's profile in the database to see if their STR marker matches the extracted longest runs.
5. If all the STR markers match for a person, their name is considered a match.
6. If a match is found, the program prints the name of the matched person. Otherwise, it prints "No match".

DNA database:
```csv
Name, AGAT, AATG, TATC, TCTA, GATA, AGAG, CAGG, TAGA, ACTG, CGAT
David, 21, 25, 31, 18, 32, 16, 19, 28, 35, 24
Emma, 30, 38, 22, 15, 25, 29, 23, 19, 12, 27
Frank, 19, 31, 28, 42, 14, 18, 21, 33, 27, 30
```
DNA sequence/sample:
```txt
AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG
```

## Usage
To use the DNA Matcher, follow these steps:

1. Install Python if it's not already installed on your system.
2. Save the DNA database as a CSV file with the following format:
   - The first row should contain the column headers, including the STR markers.
   - Each subsequent row should represent a person's profile, with their name and corresponding STR marker values.
3. Save the DNA sequence as a text file, with the DNA sequence written on a single line.
4. Open a command prompt or terminal.
5. Navigate to the directory where the DNA Matcher program is saved.
6. Run the program using the following command:
`python dna.py data.csv sequence.txt`
Replace `data.csv` with the filename of your DNA database file, and `sequence.txt` with the filename of your DNA sequence file.
7. The program will compare the sequence with the profiles in the database and display the result: either the name of the matched person or "No match".

Note: Ensure that the DNA database and sequence files are in the same directory as the `dna.py` program file.

## License
You are free to use it for any purpose.
