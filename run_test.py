# coding: utf8
import os

import unittest

import card
import pesel

class TestPESEL(unittest.TestCase):

    def test_pesel_correct_20th_century(self):
        self.assertEqual(pesel.check_pesel('90090515836'), 'September 5, 1990')

    def test_pesel_correct_21st_century(self):
        self.assertEqual(pesel.check_pesel('01261051813'), 'June 10, 2001')

    def test_pesel_correct_19th_century(self):
        self.assertEqual(pesel.check_pesel('87832165181'), 'March 21, 1887')

    def test_pesel_incorrect(self):
        self.assertIsNone(pesel.check_pesel('90090525836'))
        self.assertIsNone(pesel.check_pesel('01261031813'))
        self.assertIsNone(pesel.check_pesel('87832165581'))

    def test_pesel_too_short(self):
        self.assertIsNone(pesel.check_pesel('123456789'))

    def test_pesels_in_file(self):
        directory = os.path.dirname(os.path.abspath(__file__))
        infilename = os.path.join(directory, 'data.txt')
        with open(infilename, 'w') as infile:
            infile.write("90090515836\n87832165181\n01261031813\n01261051813\n123456789\n")
        pesel.check_pesel_file(infilename)
        try:
            with open(os.path.join(directory, 'data.out')) as outfile:
                correct = ['September 5, 1990', 'March 21, 1887', '-', 'June 10, 2001', '-']
                self.assertEqual(correct, [line.rstrip() for line in outfile.readlines()])
        except FileNotFoundError:
            self.fail("File not found")


class TestCard(unittest.TestCase):

    def test_card_correct_16_digits(self):
        self.assertTrue(card.check_card('4929134138580797'))
        self.assertTrue(card.check_card('4152651010436721'))
        self.assertTrue(card.check_card('4539667947868665'))
        self.assertTrue(card.check_card('4024007164776170'))
        self.assertTrue(card.check_card('4485154991816266'))
        self.assertTrue(card.check_card('5443972305885927'))
        self.assertTrue(card.check_card('5114869172331548'))
        self.assertTrue(card.check_card('5578916533101687'))
        self.assertTrue(card.check_card('5406733474061897'))
        self.assertTrue(card.check_card('5419564871798376'))
        self.assertTrue(card.check_card('6011395236301055'))
        self.assertTrue(card.check_card('6011432269128210'))
        self.assertTrue(card.check_card('6011636118723985'))
        self.assertTrue(card.check_card('6011631220718007'))
        self.assertTrue(card.check_card('6011856166915099'))

    def test_card_correct_15_digits(self):
        self.assertTrue(card.check_card('370594756527911'))
        self.assertTrue(card.check_card('379451233726940'))
        self.assertTrue(card.check_card('341377872063524'))
        self.assertTrue(card.check_card('376766310514015'))
        self.assertTrue(card.check_card('375692442227519'))

    def test_card_correct_11_digits(self):
        self.assertTrue(card.check_card('79927398713'))

    def test_card_incorrect(self):
        self.assertFalse(card.check_card('79927398710'))
        self.assertFalse(card.check_card('79927398711'))
        self.assertFalse(card.check_card('79927398712'))
        self.assertFalse(card.check_card('79927398714'))
        self.assertFalse(card.check_card('79927398715'))
        self.assertFalse(card.check_card('79927398716'))
        self.assertFalse(card.check_card('79927398717'))
        self.assertFalse(card.check_card('79927398718'))
        self.assertFalse(card.check_card('79927398719'))
