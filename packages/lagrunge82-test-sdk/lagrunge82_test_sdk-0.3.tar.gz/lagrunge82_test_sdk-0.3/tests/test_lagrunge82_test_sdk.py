import unittest
from lagrunge82_test_sdk.api_client import ApiClient


class TestApiClient(unittest.TestCase):
    def setUp(self):
        self.api_key = "some_api_key"

    def test_singleton_instance_creation(self):
        # Test that only one instance is created for a specific API key
        instance1 = ApiClient(self.api_key)
        instance2 = ApiClient(self.api_key)
        self.assertIs(instance1, instance2)

    def test_different_api_keys_create_different_instances(self):
        # Test that different API keys create different instances
        instance1 = ApiClient("api_key_1")
        instance2 = ApiClient("api_key_2")
        self.assertIsNot(instance1, instance2)

    def test_mode_initialization(self):
        # Test that the instance is initialized with the correct mode
        on_demand_instance = ApiClient("api_key_3")
        polling_instance = ApiClient("api_key_4", mode='polling')

        self.assertEqual(on_demand_instance._mode, 'on-demand')
        self.assertEqual(polling_instance._mode, 'polling')

    def test_mode_change_exception(self):
        # Test that an exception is raised if trying to change the mode of an existing instance
        on_demand_instance = ApiClient(self.api_key)
        with self.assertRaises(ValueError):
            ApiClient(self.api_key, mode='polling')


if __name__ == '__main__':
    unittest.main()
