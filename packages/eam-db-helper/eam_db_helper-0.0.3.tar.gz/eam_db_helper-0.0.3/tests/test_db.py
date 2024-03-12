"""This module is used to test the DatabaseHelper class."""

from unittest import TestCase

from src.eam_db_helper.db import DatabaseHelper


# pylint: disable=unused-argument
class CosmosClientMock:
    """This class is used to mock the CosmosClient class."""
    def __init__(self, uri, key):
        self.results = []

    def get_database_client(self, data_base: str):
        """Return the database client."""
        return self

    def get_container_client(self, container: str):
        """Return the container client."""
        return self

    def query_items(
            self, query: str,
            parameters: list = None,
            enable_cross_partition_query: bool = False):
        """Return the query results."""
        results = self.results
        self.results = []

        return results

    def upsert_item(self, body):
        """Add an item to the results."""
        self.results.append(body)
        return body

    def delete_item(self, item_id, partition_key):
        """Delete an item from the results."""
        self.results = None

DATABASE = DatabaseHelper(
    {
        'account_uri': 'test_uri',
        'key': 'test_key',
        'db_name': 'test_database',
        'container_name': 'test_container'
    },
    CosmosClientMock
)

class TestDatabaseHelper(TestCase):
    """This class is used to test the DatabaseHelper class."""
    def test_get_results(self):
        """Test the get_results method."""
        DATABASE.client.results = [{'id': '1'}, {'id': '2'}]
        results = DATABASE.get_results('SELECT * FROM c')
        self.assertEqual(results, [{'id': '1'}, {'id': '2'}])

    def test_get_result(self):
        """Test the get_result method."""
        DATABASE.client.results = [{'id': '1'}]
        result = DATABASE.get_result('SELECT * FROM c')
        self.assertEqual(result, {'id': '1'})

    def test_get_column(self):
        """Test the get_column method."""
        DATABASE.client.results = [{'id': '1'}, {'id': '2'}]
        column = DATABASE.get_column('id', 'SELECT * FROM c')
        self.assertEqual(column, ['1', '2'])

    def test_delete_item(self):
        """Test the delete_item method."""
        DATABASE.delete_item('1', '2')
        self.assertEqual(DATABASE.client.results, None)

    def test_upsert(self):
        """Test the upsert method."""
        DATABASE.upsert({'id': '1', 'partition_key': '2'})
        self.assertEqual(DATABASE.client.results, [{'id': '1', 'partition_key': '2'}])
