# Example usage
logger = MongoDBLogger(
    mongo_uri="mongodb://mongodb1.example.com,mongodb2.example.com/?replicaSet=MyReplicaSet",
    db_name="your_custom_db_name",
    collection_name="logs"
)
try:
     # Your code here
     1 / 0
except Exception as e:
     args = { "doc_id":"", "app":"something" }
     logger.log_exception(e, LogLevel.CRITICAL, args)