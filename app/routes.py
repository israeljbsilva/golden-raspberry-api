import logging
from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlmodel import Session, select

from app.database import get_session
from app.models import Movie
from app.schemas import ProducerIntervalsResponse
from app.services import get_producer_intervals

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/producers/intervals", response_model=ProducerIntervalsResponse)
def get_intervals(session: Session = Depends(get_session)):
    try:
        return get_producer_intervals(session)
    except Exception as e:
        logger.error(f"Error processing ranges: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


@router.get("/movies", response_model=List[Movie])
def get_movies(session: Session = Depends(get_session)):
    try:
        movies = session.exec(select(Movie)).all()
        return movies
    except Exception as e:
        logger.error(f"Error getting movies: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
