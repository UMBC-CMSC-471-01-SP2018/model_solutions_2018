# python3 solver.py p1.pddl p1.pddl.out

import requests, sys

if len(sys.argv) not in [2,3]:
    print('usage: python <problem file> [<output file>]')
    exit(0)

domain = open('hw5_domain.pddl', 'r').read()
problem = open(sys.argv[1], 'r').read()

url = 'http://solver.planning.domains/solve'
#headers = {'Content-Type':'application/json'}
#params = {'domain': domain, 'problem': problem}

response = requests.get(url, params={'domain':domain, 'problem':problem})

print('text:', response.text)

if response.json():
    print('json:', response.json())
    out = open(sys.argv[2], 'w') if len(sys.argv) == 3 else sys.stdout
    out.write('\n'.join([act['name'] for act in response.json['result']['plan']]))
