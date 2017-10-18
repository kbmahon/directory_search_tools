import unittest
import suffix_finder


class TestSuffixFinder(unittest.TestCase):

    directory_of_interest = '../test_files'
    directories_with_filesuffix = (
        {
            '../test_files/sub_dir/sub_sub_dir',
            '../test_files'
        }
    )

    def test_get_all_fies(self):
        all_files = suffix_finder.get_file_dirs_with_suffix(TestSuffixFinder.directory_of_interest, 'abc')
        self.assertEqual(TestSuffixFinder.directories_with_filesuffix, all_files)


if __name__ == '__main__':
    unittest.main()