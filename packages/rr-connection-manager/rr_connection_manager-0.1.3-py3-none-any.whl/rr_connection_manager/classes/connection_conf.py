from dotenv import dotenv_values
from pykeepass import PyKeePass
import json


class ConnectionConf:
    def __init__(self, app) -> None:
        self.app = app
        self.conf = dotenv_values(".env")
        self.via_app_server = self.conf["VIA_APP_SERVER"].lower()
        self.app_host = None
        self.db_host = None
        self.db_user = None
        self.database = None
        self.db_password = None
        self.tunnel_user = None
        self.db_port = None
        self.tunnel_port = None
        self._set_attributes()

    def _set_attributes(self):
        if ("KEEPASS_FILE_PATH" in self.conf) ^ ("KEEPASS_PASSWORD" in self.conf):
            raise ValueError(
                "Either the keepass password or file path are missing from the env file"
            )

        if "KEEPASS_FILE_PATH" in self.conf and "KEEPASS_PASSWORD" in self.conf:
            kp = PyKeePass(
                self.conf["KEEPASS_FILE_PATH"],
                password=self.conf["KEEPASS_PASSWORD"],
            )

            group = kp.find_groups(name=self.app, first=True)
            db_server = next((e for e in group.entries if "db_server" in e.path))
            db_user = next((e for e in group.entries if "db_user" in e.path))

            self.db_host = db_server.url
            self.db_user = db_user.username
            self.database = json.loads(db_user.notes)["DATABASE"][0]
            self.db_password = db_user.password
            self.db_port = json.loads(db_server.notes)["PORTS"]["DB_PORT"]

            if self.via_app_server == "true":
                app_server = next((e for e in group.entries if "app_server" in e.path))
                self.app_host = app_server.url
                self.tunnel_user = app_server.username
                self.tunnel_port = json.loads(app_server.notes)["PORTS"]["SSH_PORT"]
            else:
                self.tunnel_user = db_server.username
                self.tunnel_port = json.loads(db_server.notes)["PORTS"]["SSH_PORT"]

        else:
            self._check_envs()
            self.app_host = self.conf["APP_HOST"]
            self.db_host = self.conf["DB_HOST"]
            self.db_user = self.conf["DB_USER"]
            self.database = self.conf["DATABASE"]
            self.db_password = self.conf["DB_PASSWORD"]
            self.tunnel_user = self.conf["TUNNEL_USER"]
            self.db_port = self.conf["DB_PORT"]
            self.tunnel_port = self.conf["TUNNEL_PORT"]

    def _check_envs(self):
        # Not all of these fields are required for all connections
        # Might want to scale back and only look for essentials
        # Might be better checking each field individually
        fields = [
            "APP",
            "APP_HOST",
            "DB_HOST",
            "DB_USER",
            "DATABASE",
            "DB_PASSWORD",
            "TUNNEL_USER",
            "DB_PORT",
            "TUNNEL_PORT",
        ]

        messages = [
            f"Missing env variable {field}"
            for field in fields
            if field not in self.conf
        ]

        if len(messages) == 9:
            raise ValueError(
                """
                    No connection details provided. 
                    Either add a path and password to a keepass file or supply the required fields
                    """
            )

        if len(messages) > 0:
            raise ValueError("\n".join(messages))

        if "APP" in self.conf:
            if self.app != self.conf["APP"]:
                raise ValueError(
                    "Your trying to connect to a different server than indicated by your env file"
                )

        return True
