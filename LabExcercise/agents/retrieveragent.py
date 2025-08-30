from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from agents.baseagent import StatefulAgent

class RetrieverAgent(StatefulAgent):
    def __init__(self, service_endpoint, index_name, api_key):
        super().__init__()
        self.client = SearchClient(
            endpoint=service_endpoint,
            index_name=index_name,
            credential=AzureKeyCredential(api_key)
        )

    def get_latest_telemetry(self, device_id):
        results = self.client.search(
            search_text=f'DeviceID:{device_id}',
            top=1
        )
        for r in results:
            telemetry = {
                "DeviceID": r.get("DeviceID"),
                "Temperature": r.get("Temperature"),
                "Pressure": r.get("Pressure"),
                "CPU_Usage": r.get("CPU_Usage"),
                "Timestamp": r.get("Timestamp")
            }
            self.remember(device_id, telemetry)
            return telemetry
        return None
