import unittest
from langchain_integration.chat_service import ChatService

class TestChatService(unittest.TestCase):
    def test_get_response(self):
        response = ChatService.get_response('Hello')
        self.assertEqual(response, 'You said: Hello')

if __name__ == '__main__':
    unittest.main()
