import unittest

import hseling_api_cross_lingual_morph_analysis


class HSELing_API_Cross_lingual_morph_analysisTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hseling_api_cross_lingual_morph_analysis.app.test_client()

    def test_index(self):
        rv = self.app.get('/healthz')
        self.assertIn('Application Cross-lingual morphological analysis', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
