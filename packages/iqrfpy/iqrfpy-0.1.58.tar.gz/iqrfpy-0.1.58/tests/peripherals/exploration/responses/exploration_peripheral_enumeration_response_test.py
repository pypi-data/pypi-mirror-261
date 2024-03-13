import unittest
from parameterized import parameterized
from iqrfpy.enums.commands import ExplorationResponseCommands
from iqrfpy.enums.message_types import ExplorationMessages
from iqrfpy.enums.peripherals import EmbedPeripherals
from iqrfpy.exceptions import DpaResponsePacketLengthError
from iqrfpy.peripherals.exploration.responses.peripheral_enumeration import PeripheralEnumerationResponse, \
    PeripheralEnumerationData
from tests.helpers.json import generate_json_response
from iqrfpy.response_factory import ResponseFactory

data_ok: dict = {
    'mtype': ExplorationMessages.ENUMERATE,
    'msgid': 'peripheralEnumerationTest',
    'nadr': 0,
    'hwpid': 0,
    'rcode': 0,
    'dpa_value': 0,
    'result': {
        'dpaVer': 1047,
        'perNr': 0,
        'embeddedPers': [
           0,
           2,
           3,
           4,
           5,
           6,
           7,
           9,
           10,
           13
        ],
        'hwpid': 0,
        'hwpidVer': 0,
        'flags': 5,
        'userPer': []
    },
    'dpa': b'\x00\x00\xff\xbf\x00\x00\x00\x00\x17\x04\x00\xfd\x26\x00\x00\x00\x00\x00\x00\x05'
}

data_ok_1: dict = {
    'mtype': ExplorationMessages.ENUMERATE,
    'msgid': 'peripheralEnumerationTest',
    'nadr': 3,
    'hwpid': 5122,
    'rcode': 0,
    'dpa_value': 84,
    'result': {
        'dpaVer': 1045,
        'perNr': 1,
        'embeddedPers': [
           1,
           2,
           3,
           4,
           5,
           6,
           7,
           9,
           10,
           12
        ],
        'hwpid': 5122,
        'hwpidVer': 2,
        'flags': 5,
        'userPer': [
           94
        ]
    },
    'dpa': b'\x03\x00\xff\xbf\x02\x14\x00\x54\x15\x04\x01\xfe\x16\x00\x00\x02\x14\x02\x00\x05\x00\x00\x00\x00\x00'
           b'\x00\x00\x40'
}

data_error: dict = {
    'mtype': ExplorationMessages.ENUMERATE,
    'msgid': 'peripheralEnumerationTest',
    'nadr': 0,
    'hwpid': 1028,
    'rcode': 7,
    'dpa_value': 35,
    'dpa': b'\x00\x00\xff\xbf\x04\x04\x07\x23'
}


class PeripheralEnumerationResponseTestCase(unittest.TestCase):

    @parameterized.expand([
        ['from_dpa', data_ok, ResponseFactory.get_response_from_dpa(data_ok['dpa']), False],
        ['from_dpa', data_ok_1, ResponseFactory.get_response_from_dpa(data_ok_1['dpa']), False],
        [
            'from_json',
            data_ok,
            ResponseFactory.get_response_from_json(generate_json_response(data_ok)),
            True,
        ],
        [
            'from_json',
            data_ok_1,
            ResponseFactory.get_response_from_json(generate_json_response(data_ok_1)),
            True,
        ],
        ['from_dpa_error', data_error, ResponseFactory.get_response_from_dpa(data_error['dpa']), False],
        [
            'from_json_error',
            data_error,
            ResponseFactory.get_response_from_json(generate_json_response(data_error)),
            True,
        ],
    ])
    def test_factory_methods_ok(self, _, response_data, response, json):
        with self.subTest():
            self.assertEqual(response.nadr, response_data['nadr'])
        with self.subTest():
            self.assertEqual(response.pnum, EmbedPeripherals.EXPLORATION)
        with self.subTest():
            self.assertEqual(response.pcmd, ExplorationResponseCommands.PERIPHERALS_ENUMERATION_INFORMATION)
        with self.subTest():
            self.assertEqual(response.hwpid, response_data['hwpid'])
        with self.subTest():
            self.assertEqual(response.rcode, response_data['rcode'])
        if json:
            with self.subTest():
                self.assertEqual(response.mtype, ExplorationMessages.ENUMERATE)
            with self.subTest():
                self.assertEqual(response.msgid, response_data['msgid'])

    def test_from_dpa_invalid(self):
        with self.assertRaises(DpaResponsePacketLengthError):
            PeripheralEnumerationResponse.from_dpa(b'\x00\x00\xff\xbf\x00\x00\x00\x00\x17\x04\x00\xfd\x26')

    @parameterized.expand([
        [
            'from_dpa',
            PeripheralEnumerationData(data_ok['result']),
            PeripheralEnumerationResponse.from_dpa(data_ok['dpa'])
        ],
        [
            'from_dpa',
            PeripheralEnumerationData(data_ok_1['result']),
            PeripheralEnumerationResponse.from_dpa(data_ok_1['dpa'])
        ],
        [
            'from_json',
            PeripheralEnumerationData(data_ok['result']),
            PeripheralEnumerationResponse.from_json(generate_json_response(data_ok)),
        ],
        [
            'from_json',
            PeripheralEnumerationData(data_ok_1['result']),
            PeripheralEnumerationResponse.from_json(generate_json_response(data_ok_1)),
        ],
    ])
    def test_get_per_enum_data(self, _, data: PeripheralEnumerationData, response: PeripheralEnumerationResponse):
        self.assertEqual(response.per_enum_data, data)

    @parameterized.expand([
        ['from_dpa_error', PeripheralEnumerationResponse.from_dpa(data_error['dpa'])],
        ['from_json_error', PeripheralEnumerationResponse.from_json(generate_json_response(data_error))],
    ])
    def test_get_per_enum_data_error(self, _, response: PeripheralEnumerationResponse):
        self.assertIsNone(response.per_enum_data)
