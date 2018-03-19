import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from suncoind import SunCoinDaemon
from suncoin_config import SunCoinConfig


def test_suncoind():
    config_text = SunCoinConfig.slurp_config_file(config.suncoin_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'00000af2155f3005af28552632db7153ffb0c891bbb0da258b2ab3e688c9d56b'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c'

    creds = SunCoinConfig.get_rpc_creds(config_text, network)
    suncoind = SunCoinDaemon(**creds)
    assert suncoind.rpc_command is not None

    assert hasattr(suncoind, 'rpc_connection')

    # SunCoin testnet block 0 hash == 00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c
    # test commands without arguments
    info = suncoind.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert suncoind.rpc_command('getblockhash', 0) == genesis_hash
