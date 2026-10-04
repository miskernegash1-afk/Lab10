"""
Program Name: Word Count
Author: Misker Negash
Purpose: This program allows the user to select one of four text files,
         analyzes the selected file, counts the frequency of each word,
         and prints the results alphabetically.
Starter Code: No starter code used.
Date: October 3, 2026
"""
from pathlib import Path
import string


class WordAnalyzer:

    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        try:
            # Check if the file exists
            if not self.__filepath.exists():
                raise FileNotFoundError

            # Create translation table to remove punctuation
            translator = str.maketrans("", "", string.punctuation)

            # Open and read the file line by line
            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:

                    # Convert line to lowercase
                    line = line.lower()

                    # Remove punctuation
                    line = line.translate(translator)

                    # Split line into words
                    words = line.split()

                    # Count each word
                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True

        except FileNotFoundError:
            print(f"\nError: The file '{self.__filepath}' was not found.")
            return False


    