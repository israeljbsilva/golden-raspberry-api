from sqlmodel import Session, select

from app.csv_reader import MovieCsv
from app.models import Movie
from app.schemas import ProducerInterval, ProducerIntervalsResponse


def load_csv_to_db(movies: list[MovieCsv], session: Session):
    for movie_csv in movies:
        movie_model = Movie(
            year=movie_csv.year,
            title=movie_csv.title,
            studios=movie_csv.studios,
            producers=movie_csv.producers,
            winner=movie_csv.winner
        )

        session.add(movie_model)

    session.commit()


def get_producer_intervals(session: Session) -> ProducerIntervalsResponse:
    query = select(Movie)
    query = query.where(Movie.winner.is_(True))
    winners = session.exec(query).all()

    producer_wins = {}
    for movie in winners:
        producers = []
        for part in movie.producers.split(','):
            for subpart in part.split(' and '):
                producer = subpart.strip()
                if producer:
                    producers.append(producer)

        for producer in producers:
            if producer:
                if producer not in producer_wins:
                    producer_wins[producer] = []
                producer_wins[producer].append(movie.year)

    intervals = []
    for producer, years in producer_wins.items():
        years = sorted(set(years))
        if len(years) >= 2:
            for i in range(len(years) - 1):
                interval = years[i + 1] - years[i]
                intervals.append(ProducerInterval(
                    producer=producer,
                    interval=interval,
                    previousWin=years[i],
                    followingWin=years[i + 1]
                ))

    if not intervals:
        return ProducerIntervalsResponse(min=[], max=[])

    min_interval = min(intervals, key=lambda x: x.interval).interval
    max_interval = max(intervals, key=lambda x: x.interval).interval

    min_intervals = [i for i in intervals if i.interval == min_interval]
    max_intervals = [i for i in intervals if i.interval == max_interval]

    return ProducerIntervalsResponse(min=min_intervals, max=max_intervals)
