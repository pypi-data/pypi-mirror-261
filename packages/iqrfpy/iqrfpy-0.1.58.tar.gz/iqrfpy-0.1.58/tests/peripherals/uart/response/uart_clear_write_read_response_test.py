import unittest
from typing import List
from parameterized import parameterized
from iqrfpy.enums.commands import UartResponseCommands
from iqrfpy.enums.message_types import UartMessages
from iqrfpy.enums.peripherals import EmbedPeripherals
from iqrfpy.exceptions import DpaResponsePacketLengthError
from iqrfpy.peripherals.uart.responses.clear_write_read import ClearWriteReadResponse
from tests.helpers.json import generate_json_response
from iqrfpy.response_factory import ResponseFactory

data_ok: dict = {
    'mtype': UartMessages.CLEAR_WRITE_READ,
    'msgid': 'clearWriteReadTest',
    'nadr': 3,
    'hwpid': 0,
    'rcode': 0,
    'dpa_value': 90,
    'readData': [1, 2, 3, 4, 5],
    'result': {
        'readData': [1, 2, 3, 4, 5],
    },
    'dpa': b'\x03\x00\x0c\x83\x00\x00\x00\x5a\x01\x02\x03\x04\x05'
}

data_ok_1: dict = {
    'mtype': UartMessages.CLEAR_WRITE_READ,
    'msgid': 'clearWriteReadTest',
    'nadr': 3,
    'hwpid': 1026,
    'rcode': 0,
    'dpa_value': 35,
    'readData': [10, 5, 1, 17, 2],
    'result': {
        'readData': [10, 5, 1, 17, 2],
    },
    'dpa': b'\x03\x00\x0c\x83\x02\x04\x00\x23\x0a\x05\x01\x11\x02'
}

data_error: dict = {
    'mtype': UartMessages.CLEAR_WRITE_READ,
    'msgid': 'clearWriteReadTest',
    'nadr': 1,
    'hwpid': 1028,
    'rcode': 1,
    'dpa_value': 35,
    'dpa': b'\x01\x00\x0c\x83\x04\x04\x01\x23'
}


class ClearWriteReadResponseTestCase(unittest.TestCase):

    @parameterized.expand([
        ['from_dpa', data_ok, ResponseFactory.get_response_from_dpa(data_ok['dpa']), False],
        ['from_dpa', data_ok_1, ResponseFactory.get_response_from_dpa(data_ok_1['dpa']), False],
        ['from_json', data_ok, ResponseFactory.get_response_from_json(generate_json_response(data_ok,)), True],
        ['from_json', data_ok_1, ResponseFactory.get_response_from_json(generate_json_response(data_ok_1)), True],
        ['from_dpa_error', data_error, ResponseFactory.get_response_from_dpa(data_error['dpa']), False],
        ['from_json_error', data_error, ResponseFactory.get_response_from_json(generate_json_response(data_error)), True]
    ])
    def test_factory_methods_ok(self, _, response_data, response, json):
        with self.subTest():
            self.assertEqual(response.nadr, response_data['nadr'])
        with self.subTest():
            self.assertEqual(response.pnum, EmbedPeripherals.UART)
        with self.subTest():
            self.assertEqual(response.pcmd, UartResponseCommands.CLEAR_WRITE_READ)
        with self.subTest():
            self.assertEqual(response.hwpid, response_data['hwpid'])
        with self.subTest():
            self.assertEqual(response.rcode, response_data['rcode'])
        if json:
            with self.subTest():
                self.assertEqual(response.mtype, UartMessages.CLEAR_WRITE_READ)
            with self.subTest():
                self.assertEqual(response.msgid, response_data['msgid'])

    def test_from_dpa_invalid(self):
        with self.assertRaises(DpaResponsePacketLengthError):
            ClearWriteReadResponse.from_dpa(b'\x03\x00\x0c\x82\x00')

    @parameterized.expand([
        ['from_dpa', data_ok['readData'], ClearWriteReadResponse.from_dpa(data_ok['dpa'])],
        ['from_dpa', data_ok_1['readData'], ClearWriteReadResponse.from_dpa(data_ok_1['dpa'])],
        ['from_json', data_ok['readData'], ClearWriteReadResponse.from_json(generate_json_response(data_ok))],
        ['from_json', data_ok_1['readData'], ClearWriteReadResponse.from_json(generate_json_response(data_ok_1))]
    ])
    def test_get_read_data(self, _, read_data: List[int], response: ClearWriteReadResponse):
        self.assertEqual(response.read_data, read_data)

    @parameterized.expand([
        ['from_dpa_error', ClearWriteReadResponse.from_dpa(data_error['dpa'])],
        ['from_json_error', ClearWriteReadResponse.from_json(generate_json_response(data_error))],
    ])
    def test_get_read_data_error(self, _, response: ClearWriteReadResponse):
        self.assertIsNone(response.read_data)
