"""Smoke test for edge-computing-iot-gateway: sensor simulator emits payloads."""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.device_sim import SensorSimulator


class FakeGateway:
    def __init__(self):
        self.received = []

    def ingest_data(self, payload):
        self.received.append(payload)


def main():
    gw = FakeGateway()
    sim = SensorSimulator("dev-1", gw, interval=0.05)
    sim.start()
    time.sleep(0.3)
    sim.stop()

    assert len(gw.received) >= 2, f"expected payloads, got {len(gw.received)}"
    p = gw.received[0]
    assert p["device_id"] == "dev-1"
    assert 20.0 <= p["temperature"] <= 90.0
    assert 30.0 <= p["humidity"] <= 60.0
    assert "timestamp" in p

    print(f"smoke OK: SensorSimulator emitted {len(gw.received)} payloads")


if __name__ == "__main__":
    main()
