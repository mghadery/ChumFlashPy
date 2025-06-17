import json
import sys
from typing import Any


class UserData:
    """
    Implements a dictionary for storing key value pairs that is persisted in a text file.

    Attributes:
       user_data_file_name: File name of the text file used for storing the dictionary.
    """

    def __init__(self, user_data_file_name: str):
        self.user_data_file_name: str = user_data_file_name
        try:
            with open(self.user_data_file_name):
                pass
        except FileNotFoundError:
            with open(self.user_data_file_name, mode="w"):
                pass
        except Exception as e:
            sys.exit(str(e))

    def write(self, key: str, value: Any) -> None:
        """
        Writes a new key value pair or modifies the current value.

        Parameters
        -------------
        key: str
            Key.
        value: Any
            Value.

        Returns
        -------------
        None
        """
        try:
            with open(self.user_data_file_name) as file:
                lines = file.readlines()
                d = {}
                if len(lines):
                    s = "\n".join(lines)
                    d = json.loads(s)
                d[key] = value

            with open(self.user_data_file_name, mode="w") as file:
                s = json.dumps(d, sort_keys=True, indent=4)
                file.write(s)
        except Exception as e:
            sys.exit(str(e))

    def read(self, key: str, default: Any = None) -> Any:
        """
        Reads the value assigned to a key.

        Parameters
        -------------
        key: str
            Key.
        default: Any
            Default value used when the key does not exist.

        Returns
        -------------
        Any
            The value of the input key or default value.
        """
        try:
            with open(self.user_data_file_name) as file:
                lines = file.readlines()
                d = {}
                if len(lines):
                    s = "\n".join(lines)
                    d = json.loads(s)
                if key in d:
                    return d[key]
                if default is not None:
                    d[key] = default
                    with open(self.user_data_file_name, mode="w") as file:
                        s = json.dumps(d, sort_keys=True, indent=4)
                        file.write(s)
                    return default
        except Exception as e:
            sys.exit(str(e))
