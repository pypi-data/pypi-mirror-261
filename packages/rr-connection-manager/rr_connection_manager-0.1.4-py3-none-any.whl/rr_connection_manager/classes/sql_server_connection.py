import os

import pyodbc

from .connection import Connection


# TODO: Add alchemy functionality
class SQLServerConnection(Connection):
    def __init__(self, app=None, tunnel=None, alchemy=None) -> None:
        super().__init__(app, tunnel, alchemy)
        self.connection = self._connect()
        self.session = self._create_session()

    def _connect(self):
        try:
            dbname = self.app_conf["DATABASE"]
            host = "localhost" if self.tunnel else self.app_conf["DB_HOST"]
            return pyodbc.connect(
                driver="SQL Server",
                server=host,
                database=dbname,
                trusted_connection="Yes",
            )

        except pyodbc.Error as err:
            raise err

    def _create_session(self):
        return self.connection.cursor()

    def connection_check(self):
        if self.alchemy:
            info = self.session.execute(text("""select @@version""")).first()
        else:
            self.session.execute("select @@version")
            info = self.session.fetchone()
        return (
            f"\nConnection to {self.app} successful. \nDatabase info: \n\t{info[0].split(',')[0]}"
            ""
        )

    def commit(self):
        self.session.commit()

    def close(self):
        self.session.close()
        if self.tunnel:
            self.tunnel.stop()
