from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    charitycoin=math.Object(
        PARENT=networks.nets['charitycoin'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=12, # blocks
        IDENTIFIER='e037d5b8c6923410'.decode('hex'),
        PREFIX='7208c1a53ef629b0'.decode('hex'),
        P2P_PORT=9343,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=9342,
        BOOTSTRAP_ADDRS='78.137.98.88'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Litecoin to >=0.8.5.1!' if v < 80501 else None,
    ),
    charitycoin_testnet=math.Object(
        PARENT=networks.nets['charitycoin_testnet'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=20*60//3, # shares
        REAL_CHAIN_LENGTH=20*60//3, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=12, # blocks
        IDENTIFIER='cca5e24ec6408bdf'.decode('hex'),
        PREFIX='ad9614f6466a39de'.decode('hex'),
        P2P_PORT=19343,
        MIN_TARGET=0,
        MAX_TARGET=2**256//50 - 1,
        PERSIST=False,
        WORKER_PORT=19342,
        BOOTSTRAP_ADDRS='',
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    einsteinium=math.Object(
        PARENT=networks.nets['einsteinium'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=30, # blocks
        IDENTIFIER='e037d5b8c6923411'.decode('hex'),
        PREFIX='7208c1a53ef629b1'.decode('hex'),
        P2P_PORT=41877,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=41876,
        BOOTSTRAP_ADDRS='78.137.98.88 p2pool-bootstrap.einsteinium.org einsteinium-eu.cloudapp.net einsteinium-us.cloudapp.net'.split(' '),
        ANNOUNCE_CHANNEL='#einsteinium.org',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Einsteinium to >=0.8.6.2!' if v < 80602 else None,
    ),
    einsteinium_testnet=math.Object(
        PARENT=networks.nets['einsteinium_testnet'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=20*60//3, # shares
        REAL_CHAIN_LENGTH=20*60//3, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=30, # blocks
        IDENTIFIER='cca5e24ec6408be0'.decode('hex'),
        PREFIX='ad9614f6466a39df'.decode('hex'),
        P2P_PORT=31877,
        MIN_TARGET=0,
        MAX_TARGET=2**256//50 - 1,
        PERSIST=False,
        WORKER_PORT=31876,
        BOOTSTRAP_ADDRS='',
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
