from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .Quote import Quote


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, file_path: str) -> List[Quote]:
        if not cls.can_ingest(file_path):
            raise Exception('Cannot ingest file')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', file_path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(',')
                new_quote = Quote(parsed[1], parsed[0])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
