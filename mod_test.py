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

  def test_existing_folder_and_rsync(self):
     '''
     Tests to see if the mod properly initializes if there exists
     a folder with a '.rsync' folder inside of it.
     '''
     self.mod = Mod("rsync_test_dir")

if __name__ == "__main__":
  unittest.main()
