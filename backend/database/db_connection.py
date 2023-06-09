from .config import database_credentials, database_config
from firebase_admin import db, firestore
import firebase_admin

class DbConnection:
    def __init__(self):
        self.app = firebase_admin.initialize_app(
            database_credentials, database_config
        )
    
    def get_all_data(self, collection: str):
        """
        Returns all the data in the collection as a dict.
        """
        return db.reference(f"/{collection}/").get()

    def get_data_by_value(self, collection: str, comparinson_key: str, comparinson_value, limit: int = 10000):
        """
        Returns the data where the value stored in the comparinson key is the same
        as the comparinson value.
        Optionally, a limit can be passed to cut the response to the first x entries.
        """
        return (
            db.reference(f"/{collection}/")
            .order_by_child(comparinson_key)
            .equal_to(comparinson_value)
            .limit_to_first(limit)
            .get()
        )

    def get_data_by_key(self, collection: str, key: str, limit: int = 10000):
        """
        Returns the data with the same key.
        Optionally, a limit can be passed to cut the response to the first x entries.
        """
        response = None
        try:
            response = (
            db.reference(f"/{collection}/")
            .order_by_key()
            .equal_to(key)
            .limit_to_first(limit)
            .get()
        )
        except Exception as e:
            print(e)
        return response

    def push_data(self, collection: str, data: dict):
        """
        """
        response = None
        try:
            response = db.reference(f"/{collection}/").push(data)
        except Exception as e:
            print(e)
        return response

    def update_data_by_key(self, collection: str, key: str, new_data: dict):
        """
        uses the unique key to update the values in new_data on the db.
        Not all values need to be passed in new_data, just the ones being updated.
        """
        try:
            db.reference(f"/{collection}/").child(key).update(new_data)
        except Exception as e:
            print(e)
    
    def add_to_array_data_by_key(self, collection: str, key: str, new_data: dict):
        """
        uses the unique key to update the values in new_data on the db.
        """
        response = None
        try:
            response = db.reference(f"/{collection}/").child(key).child("logs").push(new_data)
        except Exception as e:
            print(e)
        return response
    
    def delete_data_by_key(self, collection: str, key: str):
        """
        Deletes the data present in the entry with the given key.
        """
        db.reference(f"/{collection}/").child(key).set({})