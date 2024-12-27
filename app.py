#   DNA Sequence Matching
#   Importing responsories
import csv, sys, os

def main():
    try:

        #   Compare statements for command-line arguments
        if len(sys.argv) != 3:
            raise ValueError("Only two arguments allowed !")
        
        if not str(sys.argv[1]).endswith(".csv"):
            raise ValueError("First argument must end with '.csv' !")
        
        if not str(sys.argv[2]).endswith(".txt"):
            raise ValueError("Second argument must end with .txt !")

        if not os.path.isfile(sys.argv[1]) or not os.path.isfile(sys.argv[2]):
            raise FileNotFoundError("File not found !")

    except (FileNotFoundError, ValueError) as e:
        print(f"Error : {e}\nUseage: python app.py <data.csv> <sequence.txt>")
        sys.exit(1)

    #   Read Database sequence & DNA Sequence into memory
    with open(sys.argv[1], "r") as DatabaseSequenceFile, open(sys.argv[2], "r") as DNASequenceFile:
        
        #   Read Database sequence into memory
        DatabaseSequence = [i for i in csv.DictReader(DatabaseSequenceFile)]

        #   Create a list
        SequenceKeys = [i for i in DatabaseSequence[0] if i != "name"]

        #   Read DNA Sequence into memory
        DNA = DNASequenceFile.read().strip()

    #   Declare a dictionaries
    result = {}
    string = ""

    #   Iteration over the Database Sequence & Find longest match
    for i in SequenceKeys:
        result[i] = longest_match(DNA, i)

    #   Compare the Database and Sequence
    for i in range(len(DatabaseSequence)):
        keyCount = 0

        #   For each key in SequenceKeys
        for key in SequenceKeys:

            #   Compare the keys
            if str(result[key]) == str(DatabaseSequence[i][key]):
                keyCount += 1

                #   If Counted keys match the list length
                if keyCount == len(SequenceKeys):
                    string = f"{DatabaseSequence[i]['name']}"

    print(string) if string else print("no match")

    return

def longest_match(sequence, subsequence):
    """
        *   Returns length of longest run of subsequence in sequence.
        *  Adopted from: https://cs50.harvard.edu/x/2024/psets/6/dna/
    """

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

if __name__ == "__main__":
    main()
