import csv
import io
import logging
from pathlib import Path
from typing import List

logger = logging.getLogger(__name__)


class MovieCsv:
    def __init__(self, year: int, title: str, studios: str, producers: str, winner: bool):
        self.year = year
        self.title = title
        self.studios = studios
        self.producers = producers
        self.winner = winner

    @classmethod
    def read_csv_file(cls, file_path: Path) -> List['MovieCsv']:
        with open(file_path, "r", encoding="utf-8") as f:
            csv_content = f.read()
            reader = csv.DictReader(io.StringIO(csv_content), delimiter=';')
            movies = []
            for row in reader:
                try:
                    winner = row['winner'].strip().lower() == 'yes'
                    movie = cls(
                        year=int(row['year']),
                        title=row['title'],
                        studios=row['studios'],
                        producers=row['producers'],
                        winner=winner
                    )
                    movies.append(movie)
                except Exception as e:
                    logger.error(f"Error processing CSV line {row}. Error: {str(e)}")

            return movies
