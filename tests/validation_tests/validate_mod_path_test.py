import os
import sys
import unittest
from util.test import (
    ValidationException,
    _validate_mod_path as v,
    get_mod_version as g
)

class RsyncFolderCheck(unittest.TestCase):

  def test_nonexistant_folder(self):
    '''
    Tests to see if the mod properly sends an exception
    if given a folder that doesn't exist.
    '''
    with self.assertRaises(ValidationException):
      v("this_folder_is_not_real_hopefully")

  def test_existing_folder_rsync_version(self):
     '''
     Tests to see if the mod properly initializes if there exists
     a folder with a '.rsync' folder inside of it.

     '''
     v("rsync_test_dir/good_dir")

  def test_existing_folder_rsync(self):
    '''
    Tests to see if an exception is thrown if there is not any data
    for versioning within an rsync folder.
    '''
    with self.assertRaises(ValidationException):
      v("rsync_test_dir/bad_dir_no_version")

  def test_existing_folder_version(self):
    '''
    Tests to see if an exception is thrown if there is not any data
    for rsync within an rsync folder.
    '''
    with self.assertRaises(ValidationException):
      v("rsync_test_dir/bad_dir_no_rsync")

class VersionCheck(unittest.TestCase):

    def test_good_dir(self): # The version should have 57 written in it.
        self.assertEqual(57, g("rsync_test_dir/good_dir"))

if __name__ == "__main__":
  unittest.main()
