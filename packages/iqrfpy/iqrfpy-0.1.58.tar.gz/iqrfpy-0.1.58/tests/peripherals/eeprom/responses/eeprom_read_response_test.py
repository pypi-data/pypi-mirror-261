import unittest
from parameterized import parameterized
from iqrfpy.enums.commands import EEPROMResponseCommands
from iqrfpy.enums.message_types import EEPROMMessages
from iqrfpy.enums.peripherals import EmbedPeripherals
from iqrfpy.peripherals.eeprom.responses import ReadResponse
from tests.helpers.json import generate_json_response
from iqrfpy.response_factory import ResponseFactory

data_ok: dict = {
    'mtype': EEPROMMessages.READ,
    'msgid': 'readTest',
    'nadr': 0,
    'hwpid': 0,
    'rcode': 0,
    'dpa_value': 90,
    'result': {
        'pData': [10, 20, 30, 40, 1, 12]
    },
    'dpa': b'\x00\x00\x03\x80\x00\x00\x00\x5a\x0a\x14\x1e\x28\x01\x0c'
}

data_ok_1: dict = {
    'mtype': EEPROMMessages.READ,
    'msgid': 'readTest',
    'nadr': 0,
    'hwpid': 1026,
    'rcode': 0,
    'dpa_value': 35,
    'result': {
        'pData': [10, 20, 30, 40, 1, 12]
    },
    'dpa': b'\x00\x00\x03\x80\x02\x04\x00\x5a\x0a\x14\x1e\x28\x01\x0c'
}

data_error: dict = {
    'mtype': EEPROMMessages.READ,
    'msgid': 'readTest',
    'nadr': 0,
    'hwpid': 1028,
    'rcode': 4,
    'dpa_value': 35,
    'dpa': b'\x00\x00\x03\x80\x04\x04\x04\x23'
}


class ReadResponseTestCase(unittest.TestCase):

    @parameterized.expand([
        ['from_dpa', data_ok, ResponseFactory.get_response_from_dpa(data_ok['dpa']), False],
        ['from_dpa', data_ok_1, ResponseFactory.get_response_from_dpa(data_ok_1['dpa']), False],
        ['from_json', data_ok, ResponseFactory.get_response_from_json(generate_json_response(data_ok)), True],
        ['from_json', data_ok_1, ResponseFactory.get_response_from_json(generate_json_response(data_ok_1)), True],
        ['from_dpa_error', data_error, ResponseFactory.get_response_from_dpa(data_error['dpa']), False],
        ['from_json_error', data_error, ResponseFactory.get_response_from_json(generate_json_response(data_error)), True]
    ])
    def test_factory_methods_ok(self, _, response_data, response, json):
        with self.subTest():
            self.assertEqual(response.nadr, response_data['nadr'])
        with self.subTest():
            self.assertEqual(response.pnum, EmbedPeripherals.EEPROM)
        with self.subTest():
            self.assertEqual(response.pcmd, EEPROMResponseCommands.READ)
        with self.subTest():
            self.assertEqual(response.hwpid, response_data['hwpid'])
        with self.subTest():
            self.assertEqual(response.rcode, response_data['rcode'])
        if json:
            with self.subTest():
                self.assertEqual(response.mtype, EEPROMMessages.READ)
            with self.subTest():
                self.assertEqual(response.msgid, response_data['msgid'])

    @parameterized.expand([
        ['from_dpa', data_ok['result']['pData'], ReadResponse.from_dpa(data_ok['dpa'])],
        ['from_dpa', data_ok_1['result']['pData'], ReadResponse.from_dpa(data_ok_1['dpa'])],
        ['from_json', data_ok['result']['pData'], ReadResponse.from_json(generate_json_response(data_ok))],
        ['from_json', data_ok_1['result']['pData'], ReadResponse.from_json(generate_json_response(data_ok_1))]
    ])
    def test_get_data(self, _, data, response: ReadResponse):
        self.assertEqual(response.data, data)

    @parameterized.expand([
        ['from_dpa_error', ReadResponse.from_dpa(data_error['dpa'])],
        ['from_json_error', ReadResponse.from_json(generate_json_response(data_error))]
    ])
    def test_get_data_error(self, _, response: ReadResponse):
        self.assertIsNone(response.data)
