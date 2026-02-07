import time
import random
import threading

class SensorSimulator:
    def __init__(self, device_id: str, gateway, interval: float = 1.0):
        self.device_id = device_id
        self.gateway = gateway
        self.interval = interval
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        while self.running:
            temp = random.uniform(20.0, 90.0) # Occasional high temps
            humidity = random.uniform(30.0, 60.0)
            
            payload = {
                "device_id": self.device_id,
                "timestamp": time.time(),
                "temperature": temp,
                "humidity": humidity
            }
            
            self.gateway.ingest_data(payload)
            time.sleep(self.interval)

    def stop(self):
        self.running = False
