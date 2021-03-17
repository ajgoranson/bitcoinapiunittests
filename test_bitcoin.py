import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin_price

class TestExchangeRate(TestCase):

    @patch('builtins.input', side_effect=[2])
    def test_valid_user_input(self, mock_input):
        example = bitcoin_price.user_input(mock_input)
        self.assertEqual(2, example)
    
    @patch(bitcoin_price.api_call)
    def test_json_response(self, mock_requests_json):
        mock_rate = 1
        example_api_response = {"rates":{"bpi": mock_rate},"base":"USD","date":"2020-10-02"}
        mock_requests_json.return_value = example_api_response
        converted = bitcoin_price.api_call(100, 'bpi')
        expected = 100
        self.assertEqual(expected, converted)

    @patch('builtins.print')
    def test_display_total(self, mock_print):
        bitcoin_price.display_exchange_rate(123, 123)
        mock_print.assert_called_once_with('123 Bitcoin is worth $123')

        



if __name__ == '__main__':
    unittest.main()
