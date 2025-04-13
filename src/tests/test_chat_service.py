import unittest
from langchain_integration.chat_service import ChatService

class TestChatService(unittest.TestCase):
    def setUp(self):
        self.service = ChatService()

    def test_get_response(self):
        response = self.service.get_response('Hello')
        self.assertIsInstance(response, str)

if __name__ == '__main__':
    unittest.main()
