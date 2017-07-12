# -*- coding: utf-8 -*-
import json
import unittest
import requests

class RobotTestCase(unittest.TestCase):

    def testRobotServerRest200(self):
        response = requests.post(url='http://localhost:8080/rest/mars/MML')
        self.assertEqual(requests.codes.ok, response.status_code)

    def testRobotServerText200(self):
        response = requests.post(url='http://localhost:8080/text/mars/MML')
        self.assertEqual(requests.codes.ok, response.status_code)

    def testRobotWorkingWellResponseJson(self):
        content = requests.post(url='http://localhost:8080/rest/mars/MMRMMRMM')
        self.assertEqual(2, json.loads(content.text)['x'])
        self.assertEqual(0, json.loads(content.text)['y'])
        self.assertEqual('S', json.loads(content.text)['d'])

    def testRobotWorkingWellResponseText(self):
        content = requests.post(url='http://localhost:8080/text/mars/MMRMMRMM')
        self.assertEqual('(2, 0, S)', content.text)

    def testRobotCompleteCircleToLeft(self):
        content = requests.post(url='http://localhost:8080/rest/mars/LLLL')
        self.assertEqual(0, json.loads(content.text)['x'])
        self.assertEqual(0, json.loads(content.text)['y'])
        self.assertEqual('N', json.loads(content.text)['d'])

    def testRobotCompleteCircleToRight(self):
        content = requests.post(url='http://localhost:8080/rest/mars/RRRR')
        self.assertEqual(0, json.loads(content.text)['x'])
        self.assertEqual(0, json.loads(content.text)['y'])
        self.assertEqual('N', json.loads(content.text)['d'])

    def testRobotWalkingOnTheBoardAndBackToOrigin(self):
        content = requests.post(url='http://localhost:8080/rest/mars/MMMMMRMMMMMRMMMMMRMMMMMR')
        self.assertEqual(0, json.loads(content.text)['x'])
        self.assertEqual(0, json.loads(content.text)['y'])
        self.assertEqual('N', json.loads(content.text)['d'])

    def testRobotOutOfBounds(self):
        response = requests.post(url='http://localhost:8080/rest/mars/MMLMMMMMMMMMMM')
        self.assertEqual(requests.codes.bad, response.status_code)

    def testRobotNotRecognizedMove(self):
        response = requests.post(url='http://localhost:8080/rest/mars/AAA')
        self.assertEqual(requests.codes.bad, response.status_code)

if __name__ == '__main__':
    unittest.main()
