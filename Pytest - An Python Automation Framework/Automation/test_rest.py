import pytest
import requests
import json
import math
import html

def pytest_html_report_title(report):
   report.title = "My very own title!"

   
@pytest.fixture
def supply_url():
	print("Inside Fixture")
	return "http://dummy.restapiexample.com/api/v1/employee"

def test_firstapitest(supply_url):
	req = requests.get(supply_url)
	assert req.status_code == 406
	print(req.text)
	


	
