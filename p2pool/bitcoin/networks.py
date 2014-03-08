import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

nets = dict(
    charitycoin=math.Object(
        P2P_PREFIX='caf2edd2'.decode('hex'),
        P2P_PORT=9667,
        ADDRESS_VERSION=28,
        RPC_PORT=9666,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'charitycoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: (500*100000000)*((9/10)**(height//100000)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=150, # s
        SYMBOL='CHA',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'CharityCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/CharityCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.charitycoin'), 'charitycoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://www.coincrawler.de:55/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://www.coincrawler.de:55/address/',
        TX_EXPLORER_URL_PREFIX='http://www.coincrawler.de:55/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
        CHARITY_ADDRESS='1864597a1e6f7e83555b4ec5913d455f4a5002a5'.decode('hex')
    ),
    charitycoin_testnet=math.Object(
        P2P_PREFIX='fcc1b7dc'.decode('hex'),
        P2P_PORT=19667,
        ADDRESS_VERSION=111,
        RPC_PORT=19666,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'charitycoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        #SUBSIDY_FUNC=lambda height: 500*100000000 >> (height + 1)//100000,
        SUBSIDY_FUNC=lambda height: (500*100000000)*((9/10)**(height//100000)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=150, # s
        SYMBOL='tCHA',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'CharityCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/CharityCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.charitycoin'), 'charitycoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://nonexistent-litecoin-testnet-explorer/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://nonexistent-litecoin-testnet-explorer/address/',
        TX_EXPLORER_URL_PREFIX='http://nonexistent-litecoin-testnet-explorer/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
        CHARITY_ADDRESS='1864597a1e6f7e83555b4ec5913d455f4a5002a5'.decode('hex')
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
