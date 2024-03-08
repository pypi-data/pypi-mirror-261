import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import text

from .connection import Connection


class SQLiteConnection(Connection):
    def __init__(self, app=None, tunnel=None) -> None:
        super().__init__(app, tunnel)
        self._connection_details = self._set_details()

    def _set_details(self):
        connection_details = {
            "db_name": self.connection_conf.database,
            "db_user": self.connection_conf.db_user,
            "db_host": "localhost",
            "port": None,
            "db_password": self.connection_conf.db_password,
        }

        if self.tunnel:
            self.tunnel.start()
            connection_details["port"] = self.tunnel.local_bind_port

        if self.connection_conf.via_app_server and not self.tunnel:
            connection_details["db_host"] = self.connection_conf.db_host

        return connection_details

    def cursor(self, **kwargs):
        connection = psycopg2.connect(
            dbname=self._connection_details["db_name"],
            user=self._connection_details["db_user"],
            host=self._connection_details["db_host"],
            port=self._connection_details["port"],
            password=self._connection_details["db_password"],
            **kwargs,
        )

        return connection.cursor()

    def engine(self, **kwargs):
        return create_engine(
            (
                f"postgresql://{self._connection_details['db_user']}:"
                f"{self._connection_details['db_password']}@"
                f"{self._connection_details['db_host']}:"
                f"{self._connection_details['port']}/"
                f"{self._connection_details['db_name']}"
            ),
            **kwargs,
        )

    def session_maker(self, **kwargs):
        return sessionmaker(self.engine(), **kwargs)

    def session(self):
        return Session(self.engine())

    def connection_check(self):
        session = self.session()
        info = session.execute(text("""select version()""")).first()
        session.close()
        return (
            f"\nConnection to {self.app} successful. \nDatabase info: \n\t{info[0].split(',')[0]}"
            ""
        )
