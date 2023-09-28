from typing import List, Tuple, Dict  # , Iterable
from collections import defaultdict
import threading
import time


def mapper(line: str) -> List[Tuple[str, int]]:
    words = line.strip().split()
    return [(word, 1) for word in words]


def shuffle_and_sort(mapped_values: List[Tuple[str, int]]) -> Dict[str, List[int]]:
    intermediate = defaultdict(list)
    for word, count in mapped_values:
        intermediate[word].append(count)
    return dict(intermediate)


def reducer(key: str, values: List[int]) -> Tuple[str, int]:
    return key, sum(values)


def word_count(text: str) -> Dict[str, int]:
    mapped_values = []
    lines = text.split("\n")

    # Using threads for mapping phase
    threads = []
    for line in lines:
        t = threading.Thread(target=mapped_values.extend, args=(mapper(line),))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Shuffle and sort
    grouped_data = shuffle_and_sort(mapped_values)

    # Reducing phase
    return {key: reducer(key, values)[1] for key, values in grouped_data.items()}


# Test
if __name__ == "__main__":
    with open("src/3.txt", "r") as f:
        text = f.read()

    start_time = time.time()  # Capture the start time
    result = word_count(text)

    # Sort result by value
    result = {
        k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)
    }

    with open('output.txt', 'w') as f:
        for word, count in result.items():
            f.write(f"{word}: {count}\n")

    end_time = time.time()
    print("Done!")
    print(f"Execution time: {end_time - start_time:.3f} seconds")
