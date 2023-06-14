from heapsort import heapsort
from quicksort import quicksortTime
from shellsort import shellsort
import csv

with open('random.csv', 'r') as f:
    randomArray = list(csv.reader(f))
with open('sorted.csv', 'r') as f:
    sortedArray = list(csv.reader(f))
with open('reversed.csv', 'r') as f:
    reversedArray = list(csv.reader(f))

print("RANDOM")
quicksortTime(randomArray, 0, len(randomArray)-1)
heapsort(randomArray, len(randomArray))
shellsort(randomArray)

print("\nSORTED")
quicksortTime(sortedArray, len(sortedArray)-1, len(sortedArray)-1)
heapsort(sortedArray, len(sortedArray))
shellsort(sortedArray)

print("\nREVERSED")
quicksortTime(reversedArray, 0, len(reversedArray)-1)
heapsort(reversedArray, len(reversedArray))
shellsort(reversedArray)