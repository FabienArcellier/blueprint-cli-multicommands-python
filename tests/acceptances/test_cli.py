# coding=utf-8

import unittest

import os

import fixtup
from click.testing import CliRunner
from mycommand.cli import cli

class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_main_exit_with_1_as_error_code_if_action_fails(self):
        # Assign
        runner = CliRunner()

        # Acts
        result = runner.invoke(cli, ['command1', '--name', 'fabien'])

        # Assert
        self.assertEqual(result.exit_code, 0)
        self.assertEqual('hello fabien\n', result.output)

    def test_scenario1_contains_file_txt(self):
        with fixtup.up('scenario1'):
            working_dir = os.getcwd()
            file_txt_path = os.path.join(working_dir, 'file.txt')
            self.assertTrue(os.path.isfile(file_txt_path))
