import monitor
import os
import sys

import dotenv
import newrelic.agent

root_path = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(root_path + '/app/')
dotenv.load_dotenv(os.path.join(root_path, '.env'))

monitor.start(interval=1.0)
# monitor.track(os.path.join(os.path.dirname(__file__), 'site.cf'))

# Set up NewRelic Agent
config_path = root_path + '/config/'
newrelic_ini = '%s/newrelic.ini' % config_path
if os.environ['ENV'] in ['production', 'staging']:
    newrelic.agent.initialize(newrelic_ini, os.environ['ENV'])

from serve import * # noqa
