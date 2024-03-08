import os
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor
from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, connection_scheme: str = '', host: str = '', username: str = '', password: str = '', database: str = ''):
        
        self.default_limit = int(os.environ.get('DEFAULT_LIMIT', 60))
        self.connection_string_scheme = connection_scheme if connection_scheme else os.environ.get('MONGODB_CONNECTION_SCHEME', '')
        self.host = host if host else os.environ.get('MONGODB_HOST', 'localhost')
        self.username = username if username else os.environ.get('MONGODB_USERNAME')
        self.password = password if password else os.environ.get('MONGODB_PASSWORD')
        self.database = database if database else os.environ.get('MONGODB_DATABASE')
        self.database_client = None
        self.database_collection_set = {}


    def connect(self):
        try:
            # uri = "mongodb+srv://zyad-samy:EOrX8gRUXTV3fYhX@tt-dev-cluster.i5vfg.mongodb.net/?retryWrites=true&w=majority"

            uri = f"mongodb{self.connection_string_scheme}://{self.username}:{self.password}@{self.host.rstrip('/')}"
            client = MongoClient(uri)

            self.database_client = client[self.database]

            ping_result = self.database_client.command('ping')

            if ping_result['ok'] == 1:
                print("connected to mongodb successfully")
                self.update_database_collection_set()
                
            else:
                raise ConnectionError("Invalid database connection information, failed to connect to mongodb.")
            
        except Exception as e:
            print(f"Error occurred while connecting to MongoDB: {e}")


    def update_database_collection_set(self):
        if self.database_client is not None:
            self.database_collection_set = set(self.database_client.list_collection_names())


    def collection_exists(self, collection_name: str):
        if collection_name not in self.database_collection_set:
            self.update_database_collection_set()
        
        return collection_name in self.database_collection_set


    def query_collections_parallel(self, queries):
        with ThreadPoolExecutor() as executor:
            # Execute query_collection for each query in parallel
            futures = [executor.submit(self.query_collection_from_tuple_or_dict, *query) for query in queries]
            
            # Retrieve results from futures
            results = []
            for future in futures:
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    # Handle any exceptions raised by individual queries
                    print(f"Error occurred during parallel query execution: {e}")
                    results.append([])  # Add an empty list as placeholder for failed query
            return results


    def query_collection_from_tuple_or_dict(self, *args):
        if type(args) is tuple:
            return self.query_collection(args[0], args[1], args[2], args[3], args[4], args[5])
        elif isinstance(args, dict) and 'collection' in args:
            collection = args['collection']
            query =  args['filters'] if 'filters' in args else []
            limit = args['limit'] if 'limit' in args else self.default_limit

            return self.query_collection(database, collection, query, limit)
        else:
            raise ValueError("Invalid arguments. Expected arguments are: collection name, query, and optionally limit) with that order in a tuple or dict (in which case ). instead got", args)


    def query_collection(self, collection: str, feature_vector: List[float] = [], filters:  List[Dict[str, List[str]]]= [], selected_fields: List[str]= [], limit = None, similarity_score: bool= False):
        try:  
            if self.database_client is None:
                self.connect()
            
            if self.database_client is None:
                return []
            
            if not limit:
                limit = self.default_limit

            if not self.collection_exists(collection):
                print(f"Error mongo collection not found. collection:{collection}, database:{self.database}, host: {self.host}.")
                print("maybe the username and password used have no access to the collection requested.")
                return []
        
            collection_obj = self.database_client[collection]
            print("filters: ", filters)
            query = self.convert_query_to_mongo_filter(filters)
            print("mongo_filters: ", query)


            if feature_vector:
                stages = []
                vector_search_stage = {
                    "index": os.getenv("VECTOR_INDEX_NAME", "FeatureVectorSearch"),
                    "path": os.getenv("FEATURE_VECTOR_PATH", "features"),
                    "limit": limit,
                    "numCandidates": limit * 15,
                    "queryVector": feature_vector
                }

                if query:
                    vector_search_stage["filter"] = query

                stages.append({"$vectorSearch": vector_search_stage})

                if selected_fields:
                    selected_fields_stage = {"_id": 0}
                    for field in selected_fields:
                        selected_fields_stage[field] = 1
                    
                    if similarity_score:
                        selected_fields_stage["score"] = {"$meta": "vectorSearchScore"}
                    
                    stages.append({"$project": selected_fields_stage})

                print("mongo stages:", stages)
                results = collection_obj.aggregate(stages)
            else:
                results = collection_obj.find(query).limit(limit)
            
            return list(results)
        except Exception as e:
            print(f"Error occurred during query: {e}")
            return []


    def convert_query_to_mongo_filter(self, filters: List[Dict[str, List[str]]] = []):
        result = []
        for filter in filters:
            if len(filter) > 0:
                query = {}
                key = list(filter.keys())[0]
                value = filter[key]

                if isinstance(value, list) and len(value) > 1:
                    if '$or' not in query:
                        query['$or'] = []
                    
                    for option in value:
                        query['$or'].append({key: option})
                elif isinstance(value, list) and len(value) == 1:
                    query[key] = value[0]
                elif not isinstance(value, list):
                    query[key] = value

                result.append(query)

        if result:
            return result[0] if len(result) == 2 else {"$and": result}
        else:
            return {}