import unittest
from main import fetch_news_data, parse_html_response, extract_script_tag_data, get_required_data 
from bs4 import BeautifulSoup

class TestClass(unittest.TestCase):

    def test_fetch_news_data(self):
        res = fetch_news_data()
        assert res.status_code == 200

    def test_parse_html_response(self):
        res = fetch_news_data()
        soup = parse_html_response(res)
        assert isinstance(soup, BeautifulSoup)

    def test_extract_script_tag_data(self):
        res = fetch_news_data()
        soup = parse_html_response(res)
        data = extract_script_tag_data(soup)
        self.assertIsNotNone(data)

    def test_get_required_data(self):
        res = fetch_news_data()
        soup = parse_html_response(res)
        data = extract_script_tag_data(soup)
        final_data = get_required_data(data)

        assert len(final_data) > 0


