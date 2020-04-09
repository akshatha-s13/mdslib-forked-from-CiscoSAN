import unittest

from mdslib.fc import Fc
from mdslib.connection_manager.errors import CLIError

class TestFcAttrStatus(unittest.TestCase):

    def test_status_read(self):
        fc = Fc(self.switch, self.fc_name[0])
        self.assertIsNotNone(fc.status)

    def test_status_write(self):
        fc = Fc(self.switch, self.fc_name[1])
        status = "shutdown"
        fc.status = status
        self.assertEqual("down", fc.status)
        status1 = "no shutdown"
        fc.status = status1
        self.assertEqual("inactive", fc.status)

    def test_status_write_invalid(self):
        fc = Fc(self.switch, self.fc_name[2])
        status = "asdf"
        with self.assertRaises(CLIError) as e:
            fc.status = status
        self.assertEqual("The command \" terminal dont-ask ; interface "+str(fc.name)+" ; "+str(status)+" ; no terminal dont-ask \" gave the error \" % Invalid command \".",str(e.exception))
        
