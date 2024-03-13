from typing import List
import csv

from .IngestorInterface import IngestorInterface
from .Quote import Quote


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, file_path: str) -> List[Quote]:
        if not cls.can_ingest(file_path):
            raise Exception('Cannot ingest file')

        quotes = []
        with open(file_path) as x:
            reader = csv.reader(x)
            next(reader, None)
            for line in reader:
                quotes.append(Quote(line[1], line[0]))

            return quotes
