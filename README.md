# learning-MapReduce
Going through the basic paradigms of MapReduce.
This example is a word count tally of a text file.

I've written a basic mapper and reducer in Python. 

- Mapper Function: Generates key-value pairs for each word with a count of 1.
- Shuffle and Sort: Organizes data for efficient reduction.
- Reducer Function: Calculates word counts by summing mapper outputs.
- Output: Writes word frequency results to a file and displays execution time.

Also tried implementing a threading version of it. Alas, it slows down as the overhead of creating threads exceeds the time saved by parallel processing (which is honestly not much since it's just tallying words in O(n)).

But it is there nonetheless to show the concept. Plus, Global Interpreter Lock (GIL) in Python prevents true parallelism espeically in CPU-bound tasks. Threading is more for an I/O bound thing.

## Timings
|                    | Text 1 (short) | Text 2 (very large line count, short lines) | Text 3 (large line count, long lines) |
|--------------------|----------------|------------------------------------------|-------------------------------------|
| Without Threading  | 0.027s         | 0.031s                                   | 0.05s                               |
| Threading          | 0.012s         | 0.360s                                   | 0.172s                              |


## Improvements
- Proper testing system
- Use a non-GIL language or framework
- Another example: movie dataset, tally count for 1-5 star ratings (less bins 1-5 instead of large vocabulary)
