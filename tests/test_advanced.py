# -*- coding: utf-8 -*-

from .context import py_aws_create_pro

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(c_creator.main())


if __name__ == '__main__':
    unittest.main()