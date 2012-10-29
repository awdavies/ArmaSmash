import os
import sys
import unittest
from mod import Mod

class RsyncFolderCheck(unittest.TestCase):

  def test_nonexistant_folder(self):
    '''
    Tests to see if the mod properly sends an exception
    if given a folder that doesn't exist.
    '''
    with self.assertRaises(Exception):
      self.mod = Mod("cow")

  def test_existing_folder_rsync_version(self):
     '''
     Tests to see if the mod properly initializes if there exists
     a folder with a '.rsync' folder inside of it.

     '''
     self.mod = Mod("rsync_test_dir/good_dir")

  def test_existing_folder_rsync(self):
    '''
    Tests to see if an exception is thrown if there is not any data
    for versioning within an rsync folder.
    '''
    with self.assertRaises(Exception):
      self.mod = Mod("rsync_test_dir/bad_dir_no_version")

  def test_existing_folder_version(self):
    '''
    Tests to see if an exception is thrown if there is not any data
    for rsync within an rsync folder.
    '''
    with self.assertRaises(Exception):
      self.mod = Mod("rsync_test_dir/bad_dir_no_rsync")

if __name__ == "__main__":
  unittest.main()
