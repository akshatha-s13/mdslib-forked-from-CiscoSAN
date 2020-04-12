import unittest

from mdslib.zone import Zone
from mdslib.vsan import Vsan
from mdslib.connection_manager.errors import CLIError
from mdslib.fc import Fc
from mdslib.devicealias import DeviceAlias
from mdslib.portchannel import PortChannel

class TestZoneRemoveMembers(unittest.TestCase):

    # device alias related cli errors
    def test_remove_members_dict(self):
        i = self.vsan_id[0]
        v = Vsan(self.switch,i)
        v.create()
        z = Zone(self.switch, v, self.zone_name[0])
        z.create()
        self.switch.config('fcalias name somefcalias vsan '+str(i))
        members = self.members_dict
        z.add_members(members)
        self.assertIsNotNone(z.members)
        z.remove_members(members)
        self.assertIsNone(z.members)
        z.delete()
        v.delete()

    def test_remove_members(self):
        v = Vsan(self.switch,self.vsan_id[1])
        v.create()
        z = Zone(self.switch, v, self.zone_name[1])
        z.create()
        members = self.members_list
        z.add_members(members)
        self.assertIsNotNone(z.members)
        z.remove_members(members)
        self.assertIsNone(z.members)
        z.delete()
        v.delete()









