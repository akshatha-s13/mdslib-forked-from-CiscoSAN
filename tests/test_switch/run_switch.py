from mdslib.switch import Switch
import unittest

import logging
logging.StreamHandler().setLevel(logging.CRITICAL)
logging.getLogger().addHandler(logging.FileHandler("test_switch.log"))

import json
with open('../credentials.json', 'r') as j:
		json_data = json.load(j)

user = json_data['username']
pw = json_data['password']
ip_address = json_data['ip_address']

p = 8443
sw = Switch(ip_address=ip_address,username=user,password=pw,connection_type='https',port=p,timeout=30,verify_ssl=False)

import sys
sys.stdout = open('test_switch_output.txt','wt')

from test_switchshow import *
TestSwitchShow.switch = sw
TestSwitchShow.commands = "show vsan usage"

from test_switchshowlist import *
TestSwitchShowList.switch = sw
TestSwitchShowList.commands = ["show vsan usage", "show module"]

from test_switchconfig import *
TestSwitchConfig.switch = sw
TestSwitchConfig.commands = "vsan database ; vsan 2 ; terminal dont-ask ; no vsan 2 ; no terminal dont-ask"
TestSwitchConfig.commands_clierror = "terminal dont-ask ; vsan database ; no vsan 2 "

from test_switchconfiglist import *
TestSwitchConfigList.switch = sw
TestSwitchConfigList.commands = ["vsan database ; vsan 2 ; terminal dont-ask ; no vsan 2 ", "no terminal dont-ask"]
TestSwitchConfigList.commands_clierror = ["vsan database ; terminal dont-ask ; no vsan 2 "]

from test_switchattripaddr import *
TestSwitchAttrIpAddr.switch = sw
TestSwitchAttrIpAddr.ip_address = ip_address

from test_switchattrformfactor import *
TestSwitchAttrFormFactor.switch = sw

from test_switchattrtype import *
TestSwitchAttrType.switch = sw

from test_switchattrname import *
TestSwitchAttrName.switch = sw
TestSwitchAttrName.name_max32 = "switch12345678912345678912345678" # len 32
TestSwitchAttrName.name_beyondmax = "switch123456789123456789123456789" # len 33
TestSwitchAttrName.invalid_name = "1" # starts with digit

from test_switchattrversion import *
TestSwitchAttrVersion.switch = sw

from test_switchattrmodel import *
TestSwitchAttrModel.switch = sw

from test_switchattrmodules import *
TestSwitchAttrModules.switch = sw

from test_switchattrnpv import *
TestSwitchAttrNpv.switch = sw

from test_switchattrimagestring import *
TestSwitchAttrImageString.switch = sw

from test_switchattrkickstartimage import *
TestSwitchAttrKickstartImage.switch = sw

from test_switchattrsystemimage import *
TestSwitchAttrSystemImage.switch = sw

from test_switchattrvsans import *
TestSwitchAttrVsans.switch = sw

from test_switchattrinterfaces import *
TestSwitchAttrInterfaces.switch = sw

from test_switchattranalytics import *
TestSwitchAttrAnalytics.switch = sw

suite = unittest.TestLoader().discover('.','test_switch*.py')
unittest.TextTestRunner(verbosity=2).run(suite)

