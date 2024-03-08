from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound

from models.sentiment_analysis import SentimentAnalysisDB


class SentimentAnalysisFacade:

    class NoResultFound(Exception):
        pass

    def __init__(self, *, db_session):
        self.db_session = db_session

    def get_one_by_id(self, id):

        try:
            sentiment_analysis = self.db_session.execute(
                select(SentimentAnalysisDB).where(id=id)
            ).scalar_one()
        except NoResultFound:
            raise SentimentAnalysisFacade.NoResultFound

        # return SentimentAnalysis.from_orm(sentiment_analysis)
        return sentiment_analysis