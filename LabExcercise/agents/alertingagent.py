from agents.baseagent import StatefulAgent

class AlertingAgent(StatefulAgent):
    def __init__(self, threshold=0.8):
        super().__init__()
        self.threshold = threshold

    def check_alert(self, prediction):
        if prediction["FailureProbability"] >= self.threshold:
            device_id = prediction["DeviceID"]
            print(f"[ALERT] Device {device_id} predicted to fail! Prob={prediction['FailureProbability']}")
            # Optionally: send email / webhook / Teams alert
