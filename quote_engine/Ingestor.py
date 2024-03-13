from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import Quote
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    ingests = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, file_path: str) -> List[Quote]:
        for ingestor in cls.ingests:
            if ingestor.can_ingest(file_path):
                return ingestor.parse(file_path)