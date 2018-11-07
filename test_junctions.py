import unittest

from junctions.core import app


class test_junction(unittest.TestCase):
    def setUp(self):
        app.debug = True
        self.test_client = app.test_client()

    def test_coordinates(self):
        resp = self.test_client.get("/v0/coordinates")

        self.assertEqual(resp.json[0]["id"], 0)
        self.assertEqual(resp.json[0]["coordinates"][0], -77.60431855916977)
        self.assertEqual(resp.json[0]["coordinates"][1], 43.15761560347455)

    def test_coordinates_comments(self):
        resp = self.test_client.get("/v0/coordinates")

        self.assertEqual(resp.json[0]["id"], 0)

        resp = self.test_client.get("/v0/coordinate/0/comments")

        self.assertEqual(resp.status_code, 200)

        self.assertEqual(len(resp.json), 2)
        self.assertEqual(resp.json[0]["user"], "skroh")
