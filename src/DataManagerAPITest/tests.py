import unittest
import os
import sys

sys.path.append('../DataManagerAPI')
import wikidata_museums
import gdb_operations

#import requests
#from SPARQLWrapper import SPARQLWrapper, JSON
#from rdflib import Graph, Literal, Namespace, RDF, URIRef

# Приклад простого тесту для перевірки рівності
class TestInteractionWithGraphDB(unittest.TestCase):

    def test_upload_data(self):
        status_code = gdb_operations.upload_data()
        self.assertEqual(status_code, 204)

    def test_get_all_museums(self):
        # Checks if there is more than 10 records in answer and each of them have valid set of keys
        response = gdb_operations.get_all_museums()
        self.assertGreater(len(response), 10)
        flag = True
        for i in range(10):
            if 'museum_url' not in response[i] or 'museum' not in response[i] or 'museum_type' not in response[i] or\
                    'region' not in response[i] or 'settlement' not in response[i]:
                flag = False
        self.assertTrue(flag)

    def test_get_museum(self):
        # Checks if response has valid set of keys and museum_url is the same
        museum_url = "http://www.wikidata.org/entity/Q105751941"
        response = gdb_operations.get_museum(museum_url)
        flag = True
        if 'museum_url' not in response or 'museum' not in response or 'museum_type' not in response or \
                'region' not in response or 'settlement' not in response  or 'adress' not in response \
                or 'inception' not in response or 'site' not in response or 'geo' not in response\
                or 'map_link' not in response:
            flag = False
        self.assertTrue(flag)
        self.assertEqual(museum_url, response['museum_url'])


class TestWikidataMuseums(unittest.TestCase):

    def test_get_museums_from_wikidata(self):
        #file_path = "../DataManagerAPI/museums.ttl"
        file_path = "museums.ttl"

        if os.path.exists(file_path):
            os.remove(file_path)

        wikidata_museums.get_museums_from_wikidata()

        self.assertTrue(os.path.exists(file_path))


if __name__ == '__main__':
    unittest.main()