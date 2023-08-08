from src.infra.config.db_config import DBConnectionHandler
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session
from sqlalchemy import text

def test_db_connection_handler():
    # Create an instance of DBConnectionHandler
    handler = DBConnectionHandler()

    # Test if the engine is created and is an instance of Engine
    engine = handler.get_engine()
    assert isinstance(engine, Engine)

    # Test if the session is created and is an instance of Session
    session = handler.get_session(engine)
    assert isinstance(session, Session)

    # Wrap the query string inside the text() function
    query = text("SELECT name FROM sqlite_master WHERE type='table' AND name='sensor_data';")
    result = session.execute(query)
    assert result.fetchone() is not None

    # Closing the session
    session.close()
