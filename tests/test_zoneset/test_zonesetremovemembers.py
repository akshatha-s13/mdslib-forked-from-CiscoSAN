import unittest

from mdslib.zoneset import ZoneSet
from mdslib.zone import Zone
from mdslib.vsan import Vsan
from mdslib.connection_manager.errors import CLIError

class TestZoneSetRemoveMembers(unittest.TestCase):

    def test_remove_members_nonexisting(self):
        i = self.vsan_id[0]
        v = Vsan(self.switch, i)
        v.create()
        zone = Zone(self.switch, v, self.zone_name[0])
        zone.create()
        zoneset = ZoneSet(self.switch, v, self.zoneset_name[0])
        self.assertIsNone(zoneset.members)
        with self.assertRaises(CLIError) as e:
            zoneset.remove_members([zone])
        self.assertEqual('The command " zoneset name '+str(zoneset.name)+' vsan '+str(i)+' ; no member '+str(zone.name)+' " gave the error " Zone not present ".',str(e.exception))
        zone.delete()
        zoneset.delete()
        v.delete()

    def test_remove_members(self):
        v = Vsan(self.switch, self.vsan_id[1])
        v.create()
        zone1 = Zone(self.switch, v, self.zone_name[1])
        zone2 = Zone(self.switch, v, self.zone_name[2])
        zone1.create()
        zone2.create()
        zoneset = ZoneSet(self.switch, v, self.zoneset_name[1])
        zoneset.add_members([zone1, zone2])
        self.assertIsNotNone(zoneset.members)
        zoneset.remove_members([zone1, zone2])
        self.assertIsNone(zoneset.members)
        zoneset.delete()
        zone1.delete()
        zone2.delete()
        v.delete()









