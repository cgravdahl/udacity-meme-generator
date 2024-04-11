from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .Quote import Quote


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, file_path: str) -> List[Quote]:
        if not cls.can_ingest(file_path):
            raise Exception('Cannot ingest file')

        quotes = []
        open_file = pandas.read_csv(file_path, header=0)
        for index, row in open_file.iterrows():
            new_quote = Quote(row['author'], row['body'])
            quotes.append(new_quote)

            return quotes
