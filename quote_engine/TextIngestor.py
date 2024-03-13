from typing import List
import os

from .IngestorInterface import IngestorInterface
from .Quote import Quote


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, file_path: str) -> List[Quote]:
        if not cls.can_ingest(file_path):
            raise Exception('Cannot ingest file')

        file_ref = open(file_path, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(',')
                new_quote = Quote(parsed[1], parsed[0])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(file_path)
        return quotes
