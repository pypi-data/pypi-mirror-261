import boto3
from finalsa.dynamo.client.interface import SyncDynamoClient
from typing import List, Dict


class DynamoClientImpl(SyncDynamoClient):

    def __init__(self):
        self.client = boto3.client("dynamodb")

    def __write_transaction__(self, transactions: List):
        self.client.transact_write_items(TransactItems=transactions)

    def __query__(self, TableName: str, **kwargs):
        return self.client.query(TableName=TableName, **kwargs)

    def __put__(self, TableName: str, item: Dict):
        self.client.put_item(TableName=TableName, Item=item)

    def __get__(self, TableName: str, key: Dict):
        return self.client.get_item(TableName=TableName, Key=key)

    def __delete__(self, TableName: str, key: Dict):
        self.client.delete_item(TableName=TableName, Key=key)

    def __scan__(self, TableName: str, **kwargs):
        return self.client.scan(TableName=TableName, **kwargs)

    def __update__(self, TableName: str, key: Dict, item: Dict):
        self.client.update_item(TableName=TableName, Key=key, AttributeUpdates=item)
