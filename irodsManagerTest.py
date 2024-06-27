import unittest
import irodsManager

rods = irodsManager.manager('rods', 'rods', 'http://localhost:9001/irods-http-api/', '0.3.0')

class authenticationTests(unittest.TestCase):
    def testTrue(self):
        self.assertEqual(3, 3)
    
    def testFalse(self):
        self.assertEqual(3, 2)

    def testFloop(self):
        self.assertEqual(3, 4)

# Tests for collections operations
class collectionsTests(unittest.TestCase):
    def testCreate(self):
        rods.collections.remove('/tempZone/home/new')

        response = rods.collections.create('/tempZone/home/new')
        self.assertEqual('Success: [200] Created collection at /tempZone/home/new', response)
        response = rods.collections.create('/tempZone/home/new')
        self.assertAlmostEqual('Error: [500] ', response) #TODO: Set whole error message
    
    def testRemove(self):
        rods.collections.remove('/tempZone/home/new')

        response = rods.collections.create('/tempZone/home/new')
        self.assertEqual('Success: [200] Created collection at /tempZone/home/new', response)
        response = rods.collections.remove('/tempZone/home/new')
        self.assertEqual('Success: [200] Removed collection at /tempZone/home/new', response)
    
    def testStat(self):
        rods.collections.remove('/tempZone/home/new')
        
        response = rods.collections.stat()
    
    def testList(self):
        self.assertTrue(True)
    
    def testSetPermission(self):
        self.assertTrue(True)
    
    def testSetInheritance(self):
        self.assertTrue(True)
    
    def testModifyPermissions(self):
        self.assertTrue(True)

    def testModifyMetadata(self):
        self.assertTrue(True)
    
    def testRename(self):
        self.assertTrue(True)
    
    def testTouch(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()