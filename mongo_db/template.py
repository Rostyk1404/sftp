import datetime
from pymongo.errors import DuplicateKeyError
from mongo_db.mongo_db_connector import mongoDB_client
from typing import Optional, List


class Templates:
    """Provides interface for hashing and sending requests to Mongo database."""

    collection = mongoDB_client.mydatabase["templates"]

    @classmethod
    def creating_unique_field(cls):

        """Current function creating unique constraints for pymongo."""

        return cls.collection.create_index('username', unique=True)

    @classmethod
    def create(cls, hostname: str, username: str, password: str) -> Optional[str]:
        """
         :return: An ObjectId if user was created and None if wasn't.
         #https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/
        """

        try:
            data = {'hostname': hostname, 'username': username, 'password': password,
                    'created_on': datetime.datetime.now(), 'updated_on': datetime.datetime.now(),
                    }
            result = cls.collection.insert_one(data)
            return str(result.inserted_id)
        except DuplicateKeyError:
            return None

    @classmethod
    def get_all(cls) -> List[dict]:
        """:return: if user exist return list of dict if user does not exist return an empty list."""
        return list(cls.collection.find())

    @classmethod
    def delete_user(cls, hostname) -> bool:
        """:return:bool True if all user's was deleted and False if they were not or user does not exist."""
        delete = cls.collection.delete_one({"hostname": hostname})
        return True if delete.deleted_count else False
