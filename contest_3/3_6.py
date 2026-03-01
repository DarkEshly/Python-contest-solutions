import json
import sys
from typing import Generator, Iterable, List, TextIO, TypeVar

T = TypeVar("T")


def read_tsv(file: TextIO) -> Generator[dict[str, str], None, None]:
    keys = next(file).strip().split("\t")
    for line in file:
        values = line.strip().split("\t")
        yield {key: value for key, value in zip(keys, values)}


def make_batches(sequence: Iterable[T], n: int) -> Generator[List[T], None, None]:
    current_batch: list[T] = []
    for item in sequence:
        current_batch.append(item)
        if len(current_batch) == n:
            yield current_batch
            current_batch = []
    if current_batch:
        yield current_batch


if __name__ == "__main__":
    for batch in make_batches(read_tsv(sys.stdin), 4):
        print(json.dumps(batch, ensure_ascii=False))
