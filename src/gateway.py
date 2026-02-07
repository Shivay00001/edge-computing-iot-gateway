import time
import json
import logging
from collections import deque

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [GATEWAY] - %(message)s')

class EdgeGateway:
    def __init__(self):
        self.devices = {}
        self.data_buffer = deque(maxlen=100)
        self.cloud_uplink_queue = []

    def register_device(self, device_id: str, device_type: str):
        self.devices[device_id] = {"type": device_type, "status": "ONLINE", "last_seen": time.time()}
        logging.info(f"Registered device: {device_id} ({device_type})")

    def ingest_data(self, payload: dict):
        """Receives data from devices."""
        device_id = payload.get("device_id")
        if device_id not in self.devices:
            logging.warning(f"Ignored data from unknown device: {device_id}")
            return

        self.devices[device_id]["last_seen"] = time.time()
        self.process_edge_rules(payload)

    def process_edge_rules(self, data: dict):
        """Local analytics engine."""
        temp = data.get("temperature")
        
        # Rule 1: Critical Alert (Immediate Action)
        if temp and temp > 80.0:
            logging.error(f"🚨 CRITICAL ALERT: Device {data['device_id']} temp {temp}°C! Triggering local shutoff.")
            # In real world: send command back to device for shutoff
        
        # Rule 2: Batching normal data
        self.cloud_uplink_queue.append(data)
        if len(self.cloud_uplink_queue) >= 10:
            self.upload_to_cloud()

    def upload_to_cloud(self):
        """Simulates sending batch to cloud."""
        if not self.cloud_uplink_queue:
            return
            
        logging.info(f"☁️ Uploading batch of {len(self.cloud_uplink_queue)} records to Cloud...")
        # Mock network delay
        time.sleep(0.5) 
        self.cloud_uplink_queue.clear()
        logging.info("✅ Upload complete.")

    def health_check(self):
        """Monitors device health."""
        now = time.time()
        for dev_id, info in self.devices.items():
            if now - info["last_seen"] > 10:
                info["status"] = "OFFLINE"
                logging.warning(f"Device {dev_id} is OFFLINE (Timeout)")
