from pymongo.database import Database
from mongo_db import connect_mongo
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
from streamlit import secrets

class MongoDBConnection(ExperimentalBaseConnection):
    # Setup methods for connect, cursor, and query

    ## Connect Method
    def _connect(self, **kwargs) -> Database:
        # Setup connection
        mongo_map = secrets['sample_mongo']
        db, uri = mongo_map['db'], mongo_map['uri']
        
        return connect_mongo(uri, db)
    
    ## Cursor Method
    def cursor(self) -> Database:
        return self._connect()
    
    ## Query Method
    def query(self, query: str, collection: str, ttl: int = 3600, **kwargs) -> list:
        # Cache the results
        @cache_data(ttl=ttl)
        def _query(query: dict, collection: str, **kwargs) -> list:
            # Get the database
            db = self.cursor()

            # Connect to a collection
            col = db[collection]

            # # Parse the filter query as a dictionary
            # parsed_query = eval(query)

            # Query using the .find() method in Mongo
            results = [doc for doc in col.find(filter=query)]

            return results
        
        return _query(query, collection, **kwargs)

    
    
