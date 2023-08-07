from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    """ Sqlalchemy database connection """

    def __init__(self):
        self.__connection_string = "sqlite:///sensor_data.db"
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :parram - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def get_session(self, engine):
        """sdas"""

        session_maker = sessionmaker()
        session = session_maker(bind=engine)

        return session

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        self.session = self.get_session(engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
