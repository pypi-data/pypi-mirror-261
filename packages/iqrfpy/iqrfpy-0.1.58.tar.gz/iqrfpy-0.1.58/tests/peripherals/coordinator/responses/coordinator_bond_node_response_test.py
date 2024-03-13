import unittest
from parameterized import parameterized
from iqrfpy.enums.commands import CoordinatorResponseCommands
from iqrfpy.enums.message_types import CoordinatorMessages
from iqrfpy.enums.peripherals import EmbedPeripherals
from iqrfpy.peripherals.coordinator.responses.bond_node import BondNodeResponse
from tests.helpers.json import generate_json_response
from iqrfpy.response_factory import ResponseFactory

data_ok: dict = {
    'mtype': CoordinatorMessages.BOND_NODE,
    'msgid': 'bondNodeTest',
    'nadr': 0,
    'hwpid': 0,
    'rcode': 0,
    'dpa_value': 71,
    'result': {
        'bondAddr': 1,
        'devNr': 2
    },
    'dpa': b'\x00\x00\x00\x84\x00\x00\x00\x47\x01\x02'
}

data_ok_1: dict = {
    'mtype': CoordinatorMessages.BOND_NODE,
    'msgid': 'bondNodeTest',
    'nadr': 0,
    'hwpid': 1026,
    'rcode': 0,
    'dpa_value': 35,
    'result': {
        'bondAddr': 10,
        'devNr': 100
    },
    'dpa': b'\x00\x00\x00\x84\x02\x04\x00\x23\x0a\x64'
}

data_error: dict = {
    'mtype': CoordinatorMessages.BOND_NODE,
    'msgid': 'bondNodeTest',
    'nadr': 0,
    'hwpid': 1028,
    'rcode': 7,
    'dpa_value': 35,
    'dpa': b'\x00\x00\x00\x84\x04\x04\x07\x23'
}


class BondNodeResponseTestCase(unittest.TestCase):

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
            self.assertEqual(response.pnum, EmbedPeripherals.COORDINATOR)
        with self.subTest():
            self.assertEqual(response.pcmd, CoordinatorResponseCommands.BOND_NODE)
        with self.subTest():
            self.assertEqual(response.hwpid, response_data['hwpid'])
        with self.subTest():
            self.assertEqual(response.rcode, response_data['rcode'])
        if json:
            with self.subTest():
                self.assertEqual(response.mtype, CoordinatorMessages.BOND_NODE)
            with self.subTest():
                self.assertEqual(response.msgid, response_data['msgid'])

    def test_from_dpa_invalid(self):
        with self.assertRaises(ValueError):
            BondNodeResponse.from_dpa(b'\x00\x00\x00\x84\x00\x00\x00\x22')

    @parameterized.expand([
        ['from_dpa', data_ok['result']['bondAddr'], BondNodeResponse.from_dpa(data_ok['dpa'])],
        ['from_dpa', data_ok_1['result']['bondAddr'], BondNodeResponse.from_dpa(data_ok_1['dpa'])],
        ['from_json', data_ok['result']['bondAddr'], BondNodeResponse.from_json(generate_json_response(data_ok))],
        ['from_json', data_ok_1['result']['bondAddr'], BondNodeResponse.from_json(generate_json_response(data_ok_1))]
    ])
    def test_get_bond_addr(self, _, bond_addr, response: BondNodeResponse):
        self.assertEqual(response.bond_addr, bond_addr)

    @parameterized.expand([
        ['from_dpa_error', BondNodeResponse.from_dpa(data_error['dpa'])],
        ['from_json_error', BondNodeResponse.from_json(generate_json_response(data_error))]
    ])
    def test_get_bond_addr_error(self, _, response: BondNodeResponse):
        self.assertIsNone(response.bond_addr)

    @parameterized.expand([
        ['from_dpa', data_ok['result']['devNr'], BondNodeResponse.from_dpa(data_ok['dpa'])],
        ['from_dpa', data_ok_1['result']['devNr'], BondNodeResponse.from_dpa(data_ok_1['dpa'])],
        ['from_json', data_ok['result']['devNr'], BondNodeResponse.from_json(generate_json_response(data_ok))],
        ['from_json', data_ok_1['result']['devNr'], BondNodeResponse.from_json(generate_json_response(data_ok_1))]
    ])
    def test_get_dev_nr(self, _, dev_nr, response: BondNodeResponse):
        self.assertEqual(response.dev_nr, dev_nr)

    @parameterized.expand([
        ['from_dpa_error', BondNodeResponse.from_dpa(data_error['dpa'])],
        ['from_json_error', BondNodeResponse.from_json(generate_json_response(data_error))]
    ])
    def test_get_dev_nr_error(self, _, response: BondNodeResponse):
        self.assertIsNone(response.dev_nr)
