# coding: utf-8

"""
    gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sarus_proxy.api.events_api import EventsApi


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EventsApi()

    def tearDown(self) -> None:
        pass

    def test_create_event(self) -> None:
        """Test case for create_event

        Create Event
        """
        pass

    def test_create_feedback(self) -> None:
        """Test case for create_feedback

        Create Feedback Event
        """
        pass

    def test_create_feedback_native(self) -> None:
        """Test case for create_feedback_native

        Create Feedback Native Event
        """
        pass

    def test_delete_event(self) -> None:
        """Test case for delete_event

        Delete Event
        """
        pass

    def test_read_event(self) -> None:
        """Test case for read_event

        Read Event
        """
        pass

    def test_read_events(self) -> None:
        """Test case for read_events

        Read Events
        """
        pass

    def test_read_feedbacks(self) -> None:
        """Test case for read_feedbacks

        Get Feedback Events
        """
        pass


if __name__ == '__main__':
    unittest.main()
