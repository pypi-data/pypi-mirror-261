import sys
sys.path.append("../mqi-api")
from v1.api import MQI 

m = MQI("ws://mqicontroller.local", "8080")
m.connect()

m.set_current("1", "0")
