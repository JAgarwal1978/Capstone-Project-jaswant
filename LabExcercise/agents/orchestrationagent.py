from agents.retrieveragent import RetrieverAgent
from agents.predictoragent import PredictorAgent
from agents.alertingagent import AlertingAgent

class AgentCoordinator:
    def __init__(self, retriever, predictor, alerter):
        self.retriever = retriever
        self.predictor = predictor
        self.alerter = alerter

    def run_cycle(self, device_id):
        telemetry = self.retriever.get_latest_telemetry(device_id)
        if telemetry:
            prediction = self.predictor.predict_failure(telemetry)
            self.alerter.check_alert(prediction)
            return prediction
        return None
