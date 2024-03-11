from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .Quote import Quote


class DocxImporter(IngestorInterface):
    allowed_extensions = ['docx']

    def parse(cls, file_path: str) -> List[Quote]:
        if not cls.can_ingest(file_path):
            raise Exception('Cannot ingest file')

        quotes = []
        open_file = docx.Document(file_path)
        for x in open_file:
            if x.text != '':
                parse = x.text.split('-')
                new_quote = Quote(parse[1], parse[0])
                quotes.append(new_quote)
            return quotes
