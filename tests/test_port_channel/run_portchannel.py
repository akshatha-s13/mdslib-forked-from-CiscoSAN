from mdslib.switch import Switch
import unittest

import logging
logging.basicConfig(filename='test_portchannel.log', filemode='w', level=logging.DEBUG, format="[%(asctime)s] [%(module)-14.14s] [%(levelname)-5.5s] %(message)s")

import json
with open('../switch_details.json', 'r') as j:
		data = json.load(j)

sw = Switch(ip_address = data['ip_address'], username = data['username'], password = data['password'], connection_type = data['connection_type'], port = data['port'], timeout = data['timeout'], 
verify_ssl = False )

import sys
sys.stdout = open('test_portchannel_output.txt','wt')

from mdslib.constants import VALID_PC_RANGE
existing_id = [15]
pc_id = [i for i in range(245,256)]

from test_portchanneladdmembers import *
TestPortChannelAddMembers.switch = sw
TestPortChannelAddMembers.pc_id = pc_id
TestPortChannelAddMembers.fc_name = ['fc1/'+str(i) for i in range(31,37)] 
TestPortChannelAddMembers.invalid_fc = "fc3/3"

from test_portchannelremovemembers import *
TestPortChannelRemoveMembers.switch = sw
TestPortChannelRemoveMembers.pc_id = pc_id
TestPortChannelRemoveMembers.fc_name = ['fc1/'+str(i) for i in range(31,38)] 

from test_portchannelcreate import *
TestPortChannelCreate.switch = sw
TestPortChannelCreate.pc_id = pc_id[0]
TestPortChannelCreate.valid_pc_id = [i for i in VALID_PC_RANGE if i not in existing_id]
TestPortChannelCreate.invalid_pc_id = [0, 257]

from test_portchanneldelete import *
TestPortChannelDelete.switch = sw
TestPortChannelDelete.pc_id = pc_id

from test_portchannelattrcounters import *
TestPortChannelAttrCounters.switch = sw
TestPortChannelAttrCounters.pc_id = pc_id

from test_portchannelattrdescription import *
TestPortChannelAttrDescription.switch = sw
TestPortChannelAttrDescription.pc_id = pc_id

from test_portchannelattrid import *
TestPortChannelAttrId.switch = sw
TestPortChannelAttrId.pc_id = pc_id

from test_portchannelattrchannelmode import *
TestPortChannelAttrChannelMode.switch = sw
TestPortChannelAttrChannelMode.pc_id = pc_id
TestPortChannelAttrChannelMode.channel_mode = ["active","on"]

from test_portchannelattrmembers import *
TestPortChannelAttrMembers.switch = sw
TestPortChannelAttrMembers.pc_id = pc_id
TestPortChannelAttrMembers.fc_name = ['fc1/'+str(i) for i in range(31,34)] 

from test_portchannelattrmode import *
TestPortChannelAttrMode.switch = sw
TestPortChannelAttrMode.pc_id = pc_id
TestPortChannelAttrMode.modes_allowed = [] #['E', 'F', 'Fx', 'NP', 'SD', 'auto']

from test_portchannelattrname import *
TestPortChannelAttrName.switch = sw
TestPortChannelAttrName.pc_id = pc_id

from test_portchannelattrspeed import *
TestPortChannelAttrSpeed.switch = sw
TestPortChannelAttrSpeed.pc_id = pc_id
TestPortChannelAttrSpeed.speeds_allowed = [] #[1000, 16000, 2000, 32000, 4000, 8000]

from test_portchannelattrstatus import *
TestPortChannelAttrStatus.switch = sw
TestPortChannelAttrStatus.pc_id = pc_id

from test_portchannelattrtrunk import *
TestPortChannelAttrTrunk.switch = sw
TestPortChannelAttrTrunk.pc_id = pc_id
TestPortChannelAttrTrunk.trunk_values = ['on','off','auto']

suite = unittest.TestLoader().discover('.','test_portchannel*.py')
unittest.TextTestRunner(verbosity=2).run(suite)

