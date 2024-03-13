import unittest
from parameterized import parameterized
from iqrfpy.enums.commands import OSResponseCommands
from iqrfpy.enums.message_types import OSMessages
from iqrfpy.enums.peripherals import EmbedPeripherals
from iqrfpy.exceptions import DpaResponsePacketLengthError
from iqrfpy.peripherals.os.responses.read import ReadResponse
from iqrfpy.peripherals.os.responses.os_read_data import OsReadData
from tests.helpers.json import generate_json_response
from iqrfpy.response_factory import ResponseFactory

data_ok: dict = {
    'mtype': OSMessages.READ,
    'msgid': 'readTest',
    'nadr': 0,
    'hwpid': 0,
    'rcode': 0,
    'dpa_value': 71,
    'result': {
        'mid': 2165406807,
        'osVersion': 70,
        'trMcuType': 36,
        'osBuild': 2264,
        'rssi': 0,
        'supplyVoltage': 3.0013793103448276,
        'flags': 32,
        'slotLimits': 117,
        'ibk': [
           228,
           130,
           127,
           38,
           186,
           44,
           106,
           194,
           118,
           84,
           88,
           173,
           52,
           27,
           86,
           46
        ],
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
        'flagsEnum': 5,
        'userPer': []
    },
    'dpa': b'\x00\x00\x02\x80\x00\x00\x00\x47\x57\x7c\x11\x81\x46\x24\xd8\x08\x00\x28\x20\x75\xe4\x82\x7f\x26\xba\x2c'
           b'\x6a\xc2\x76\x54\x58\xad\x34\x1b\x56\x2e\x17\x04\x00\xfd\x26\x00\x00\x00\x00\x00\x00\x05'
}

data_error: dict = {
    'mtype': OSMessages.READ,
    'msgid': 'readTest',
    'nadr': 0,
    'hwpid': 1028,
    'rcode': 7,
    'dpa_value': 35,
    'dpa': b'\x00\x00\x02\x80\x04\x04\x07\x23'
}


class ReadResponseTestCase(unittest.TestCase):

    @parameterized.expand([
        ['from_dpa', data_ok, ResponseFactory.get_response_from_dpa(data_ok['dpa']), False],
        ['from_json', data_ok, ResponseFactory.get_response_from_json(generate_json_response(data_ok)), True],
        ['from_dpa_error', data_error, ResponseFactory.get_response_from_dpa(data_error['dpa']), False],
        ['from_json_error', data_error, ResponseFactory.get_response_from_json(generate_json_response(data_error)), True]
    ])
    def test_factory_methods_ok(self, _, response_data, response, json):
        with self.subTest():
            self.assertEqual(response.nadr, response_data['nadr'])
        with self.subTest():
            self.assertEqual(response.pnum, EmbedPeripherals.OS)
        with self.subTest():
            self.assertEqual(response.pcmd, OSResponseCommands.READ)
        with self.subTest():
            self.assertEqual(response.hwpid, response_data['hwpid'])
        with self.subTest():
            self.assertEqual(response.rcode, response_data['rcode'])
        if json:
            with self.subTest():
                self.assertEqual(response.mtype, OSMessages.READ)
            with self.subTest():
                self.assertEqual(response.msgid, response_data['msgid'])

    def test_from_dpa_invalid(self):
        with self.assertRaises(DpaResponsePacketLengthError):
            ReadResponse.from_dpa(b'\x00\x00\x02\x80\x00\x00\x00\x47')

    @parameterized.expand([
        ['from_dpa', OsReadData(data_ok['result']), ReadResponse.from_dpa(data_ok['dpa'])],
        ['from_json', OsReadData(data_ok['result']), ReadResponse.from_json(generate_json_response(data_ok))]
    ])
    def test_get_os_read_data(self, _, data: OsReadData, response: ReadResponse):
        self.assertEqual(response.os_read_data, data)

    @parameterized.expand([
        ['from_dpa_error', ReadResponse.from_dpa(data_error['dpa'])],
        ['from_json_error', ReadResponse.from_json(generate_json_response(data_error))]
    ])
    def test_get_os_read_data_error(self, _, response: ReadResponse):
        self.assertIsNone(response.os_read_data)
