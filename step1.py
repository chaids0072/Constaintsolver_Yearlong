
from urllib.request import urlopen
import urllib.request
import json

def get_plan(domain_file,problem_file):
	data = {'domain': open(domain_file, 'r').read(),
	        'problem': open(problem_file, 'r').read()}

	url = 'http://solver.planning.domains/solve'
	req = urllib.request.Request(url)
	req.add_header('Content-Type', 'application/json')
	json_data = json.dumps(data)
	json_data_as_bytes = json_data.encode('utf-8')
	req.add_header('Content-Length', len(json_data_as_bytes))
	response = urllib.request.urlopen(req, json_data_as_bytes)
	result_json = json.load(response)
	return result_json
