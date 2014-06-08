import unittest
from appliance_collector_gateway import ApplianceCollector

class TestApplianceCollectorGateway(unittest.TestCase):

  def testGetAppliancesWithEmptyAC_Expect_NoAppl(self):
    ac = ApplianceCollector()
    self.assertEqual(len(ac.getAppliances()), 0)
