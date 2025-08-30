from datetime import datetime


class StatefulAgent:
    def __init__(self):
        self.memory = {}  # retains machine history keyed by DeviceID

    def remember(self, device_id, data):
        """Store history per device"""
        if device_id not in self.memory:
            self.memory[device_id] = []
        self.memory[device_id].append({"timestamp": datetime.utcnow(), **data})

    def recall(self, device_id):
        """Retrieve history for device"""
        return self.memory.get(device_id, [])
