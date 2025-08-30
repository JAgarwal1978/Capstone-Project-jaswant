from agents.retrieveragent import RetrieverAgent
from agents.predictoragent import PredictorAgent
from agents.alertingagent import AlertingAgent
from agents.orchestrationagent import AgentCoordinator
 
# Config
SERVICE_ENDPOINT = "https://jaswantlabaisearch.search.windows.net"
INDEX_NAME = "devicedataindex"
# "devicejsonindex"
API_KEY = "W34JgogieglUphsxRljl7diUXMZIR61zLbkjdee4tEAzSeAVV8SO"

# Create agents
retriever = RetrieverAgent(SERVICE_ENDPOINT, INDEX_NAME, API_KEY)
predictor = PredictorAgent()
alerter = AlertingAgent(threshold=0.8)

# Coordinator
coordinator = AgentCoordinator(retriever, predictor, alerter)

# Run prediction for a device
result = coordinator.run_cycle("Pump-23")
print(result)

# Check stateful history
print(retriever.recall("Pump-23"))
print(predictor.recall("Pump-23"))
