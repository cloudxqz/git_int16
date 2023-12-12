import json

def parse_report(need_to_parse_file, output):
    with open(need_to_parse_file, 'r') as f:
        report = json.load(f)

    vulnerabilities = []
    for site in report['site']:
        for alert in site['alerts']:
            vulnerability = {
                'name': alert['name'],
                'count': int(alert['count'])
            }
            vulnerabilities.append(vulnerability)

    result = {
        'vulnerabilities': vulnerabilities
    }

    with open(output, 'w') as f:
        json.dump(result, f, indent=4)

parse_report('/root/2023-12-11-ZAP-Report-.json', '/root/123123123.json')
