import unittest
from parameterized import parameterized
from iqrfpy.exceptions import RequestParameterInvalidValueError
from iqrfpy.peripherals.uart.requests.open import OpenRequest
from iqrfpy.utils.dpa import BaudRates


class OpenRequestTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.dpa = b'\x01\x00\x0C\x00\xff\xff\x03'
        self.json = {
            'mType': 'iqrfEmbedUart_Open',
            'data': {
                'msgId': 'openTest',
                'req': {
                    'nAdr': 1,
                    'hwpId': 65535,
                    'param': {
                        'baudRate': BaudRates.B9600,
                    }
                },
                'returnVerbose': True
            }
        }

    @parameterized.expand([
        ['baud_rate', BaudRates.B9600, b'\x01\x00\x0c\x00\xff\xff\x03'],
        ['baud_rate', BaudRates.B115200, b'\x01\x00\x0c\x00\xff\xff\x07'],
    ])
    def test_to_dpa(self, _, baud_rate: BaudRates, expected):
        request = OpenRequest(nadr=1, baud_rate=baud_rate)
        self.assertEqual(
            request.to_dpa(),
            expected
        )

    @parameterized.expand([
        ['baud_rate', BaudRates.B9600],
        ['baud_rate', BaudRates.B115200],
    ])
    def test_to_json(self, _, baud_rate: BaudRates):
        request = OpenRequest(nadr=1, baud_rate=baud_rate, msgid='openTest')
        self.json['data']['req']['param']['baudRate'] = baud_rate
        self.assertEqual(
            request.to_json(),
            self.json
        )

    @parameterized.expand([
        [BaudRates.B9600, b'\x01\x00\x0c\x00\xff\xff\x03'],
        [BaudRates.B115200, b'\x01\x00\x0c\x00\xff\xff\x07'],
    ])
    def test_set_baud_rate(self, baud_rate: BaudRates, dpa):
        request = OpenRequest(nadr=1, baud_rate=BaudRates.B9600, msgid='openTest')
        self.assertEqual(
            request.to_dpa(),
            self.dpa
        )
        self.assertEqual(
            request.to_json(),
            self.json
        )
        request.baud_rate = baud_rate
        self.json['data']['req']['param']['baudRate'] = baud_rate
        self.assertEqual(
            request.to_dpa(),
            dpa
        )
        self.assertEqual(
            request.to_json(),
            self.json
        )

    @parameterized.expand([
        [-1],
        [256],
        [1000]
    ])
    def test_invalid_params(self, baud_rate: int):
        with self.assertRaises(RequestParameterInvalidValueError):
            OpenRequest(nadr=1, baud_rate=baud_rate)
