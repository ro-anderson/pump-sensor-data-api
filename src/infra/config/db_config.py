from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from fuzzywuzzy import fuzz
#import re

#def clean_string(value):
#    cleaned_value = re.sub(r'[^\w\s]', '', value)  # Remove all non-alphanumeric and non-whitespace characters
#    cleaned_value = cleaned_value.lower()          # Convert to lowercase
#    return cleaned_value
#
#def string_similarity(str1, str2):
#    return fuzz.ratio(str1, str2)

class DBConnectionHandler:
    """ Sqlalchemy database connection """

    def __init__(self):
        self.__connection_string = "sqlite:///sensor_data.db"
        self.session = None

        #connection.connection.create_function('clean_string', 1, clean_string)
        #connection.connection.create_function('string_similarity', 2, string_similarity)

    #def get_engine(self):
    #    """Return connection Engine
    #    :parram - None
    #    :return - engine connection to Database
    #    """
    #    engine = create_engine(self.__connection_string)
    #    return engine
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
        #session_maker = sessionmaker()
        #self.session = session_maker(bind=engine)
        self.session = self.get_session(engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
