import json
import sys
from itertools import groupby
from typing import Any, Callable, Generator, Iterable

Record = dict[str, Any]
Records = Iterable[Record]
Mapper = Callable[[Record], Generator[Record, None, None]]
Reducer = Callable[[str, Iterable[Record]], Generator[Record, None, None]]


def map_reduce(records: Records, key: str, mapper: Mapper, reducer: Reducer) -> Generator[Record, None, None]:
    mapped_records = (mapped for record in records for mapped in mapper(record))
    sorted_records = sorted(mapped_records, key=lambda x: x[key])
    for new_key, group in groupby(sorted_records, key=lambda x: x[key]):
        yield from reducer(new_key, group)


def mapper(record: Record) -> Generator[Record, None, None]:
    words = record["data"].split()
    for new_word in words:
        yield {"word": new_word, "weight": record["weight"]}


def reducer(key: str, records: Records) -> Generator[Record, None, None]:
    yield {"word": key, "weight": sum(record["weight"] for record in records)}


def main() -> None:
    records = (json.loads(line) for line in sys.stdin)
    results = map_reduce(records=records, key="word", mapper=mapper, reducer=reducer)
    result = sorted(results, key=lambda x: x["word"])
    for line in result:
        print(f"{line['word']} {line['weight']}")


if __name__ == "__main__":
    main()
