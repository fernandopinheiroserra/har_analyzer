import json
import haralyzer

def analyze_har(har_file_path):
    try:
        with open(har_file_path, 'r') as har_file:
            har_data = json.load(har_file)
        har_parser = haralyzer.HarParser(har_data)

        entries = har_parser.har_data['entries']

        analysis = {
            'entries': []
        }
        for entry in entries:
            analysis_entry = {
                'startedDateTime': entry['startedDateTime'],
                'time': entry['time'],
                'request': {
                    'method': entry['request']['method'],
                    'url': entry['request']['url'],
                    'httpVersion': entry['request']['httpVersion']
                },
                'response': {
                    'status': entry['response']['status'],
                    'statusText': entry['response']['statusText'],
                    'httpVersion': entry['response']['httpVersion']
                }
            }
            analysis['entries'].append(analysis_entry)

        return analysis
    except Exception as e:
        return {'error': str(e)}
