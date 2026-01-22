import sys
import os
sys.path.append(os.getcwd())
from helpdesk_agent.agent import root_agent

print("Attributes of root_agent:")
for attr in dir(root_agent):
    if not attr.startswith("_"):
        print(attr)