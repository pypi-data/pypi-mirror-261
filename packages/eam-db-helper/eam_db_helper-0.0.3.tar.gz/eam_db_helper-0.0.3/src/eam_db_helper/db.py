"""This module contains the DatabaseHelper class,
which is used to interact with the Azure Cosmos DB database.
It provides methods to query, insert, update, and delete data from the database."""

import logging
from azure.cosmos import CosmosClient

LOGGER = logging.getLogger("azure")
LOGGER.setLevel(logging.WARN)


class DatabaseHelper:
    """This class is used to interact with the Azure Cosmos DB database."""
    def __init__(self, cosmos_metadata, connection=CosmosClient):
        self.cosmos_metadata = {
            'account_uri': cosmos_metadata['account_uri'],
            'key': cosmos_metadata['key'],
            'db_name': cosmos_metadata['db_name'],
            'container_name': cosmos_metadata['container_name']
        }
        self.client = connection(
            self.cosmos_metadata["account_uri"], self.cosmos_metadata["key"]
        )
        self.data_base = self.client.get_database_client(self.cosmos_metadata["db_name"])
        self.container = self.data_base.get_container_client(self.cosmos_metadata["container_name"])

    # pylint: disable=dangerous-default-value
    def get_results(self, query: str, parameters: list = [], enable_cross_partition=False) -> list:
        """Return a list of results from the database."""
        try:
            items = self.container.query_items(
                query=query,
                parameters=parameters,
                enable_cross_partition_query=enable_cross_partition
            )
            return list(items)
        except ValueError as err:
            LOGGER.error("Error getting results: %s", err)
            return []

    # pylint: disable=dangerous-default-value
    def get_result(self, query: str, parameters: list = [], enable_cross_partition=False) -> dict:
        """Return a single result from the database."""
        try:
            items = self.container.query_items(
                query=query,
                parameters=parameters,
                enable_cross_partition_query=enable_cross_partition
            )
            items_list = list(items)

            if items_list:
                return items_list[0]

            return {}
        except (ValueError, IndexError, TypeError) as err:
            LOGGER.error("Error getting result: %s", err)
            return {}


    def get_column(self, column_name: str, query: str, parameters: list = []) -> list:
        """Return a list of a single column from the query results."""
        try:
            items = self.container.query_items(query=query, parameters=parameters)
            return [item[column_name] for item in items]
        except IndexError as err:
            LOGGER.error("Error getting column: %s", err)
            return []


    def delete_item(self, item_id: str, primary_key: str) -> None:
        """Delete an item from the database by id and partition key."""
        self.container.delete_item(item_id, partition_key=primary_key)


    def upsert(self, item: dict) -> dict:
        """Upsert an item into the database."""
        return self.container.upsert_item(item)
