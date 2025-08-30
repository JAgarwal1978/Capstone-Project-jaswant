from agents.baseagent import StatefulAgent

class PredictorAgent(StatefulAgent):
    def __init__(self):
        super().__init__()

    def predict_failure(self, telemetry):
        """Simple rule-based predictor"""
        prob = 0.0
        if telemetry["Temperature"] > 90 or telemetry["CPU_Usage"] > 90:
            prob = 0.85
        elif telemetry["Temperature"] > 80 or telemetry["CPU_Usage"] > 80:
            prob = 0.5
        else:
            prob = 0.1

        failure_class = "Yes" if prob > 0.5 else "No"
        result = {**telemetry, "FailureProbability": prob, "FailureClass": failure_class}
        self.remember(telemetry["DeviceID"], result)
        return result
