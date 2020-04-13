import unittest

from mdslib.zoneset import ZoneSet
from mdslib.zone import Zone
from mdslib.vsan import Vsan

class TestZoneSetIsActive(unittest.TestCase):

    def test_is_active(self):
        v = Vsan(self.switch, self.vsan_id[0])
        v.create()
        zoneset = ZoneSet(self.switch, v, self.zoneset_name[0] )
        zoneset.create()
        zone = Zone(self.switch, v, self.zone_name[0])
        zone.create()
        zone.add_members(self.zone_members)
        zoneset.add_members([zone])

        zoneset.activate(True)
        self.assertTrue(zoneset.is_active())

        zoneset.activate(False)
        self.assertFalse(zoneset.is_active())

        zone.delete()
        zoneset.delete()
        v.delete()









