# Edge Computing IoT Gateway

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![IoT](https://img.shields.io/badge/IoT-Edge_Computing-blue.svg)](https://en.wikipedia.org/wiki/Edge_computing)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade IoT Edge Gateway** simulation. This repository implements a local gateway that aggregates data from multiple sensor devices, performs edge analytics (filtering/aggregation), and forwards critical alerts to a cloud uplink.

## 🚀 Features

- **Device Management**: Registers and tracks status of connected edge devices.
- **Data Aggregation**: Buffers high-frequency sensor readings.
- **Edge Analytics**: Local processing to detect anomalies (e.g., high temperature) without cloud round-trip.
- **Protocol Simulation**: Mocks MQTT-style message passing.
- **Cloud Uplink**: Batches non-critical data for upstream transmission.

## 📁 Project Structure

```
edge-computing-iot-gateway/
├── src/
│   ├── gateway.py        # Gateway Logic
│   ├── device_sim.py     # Sensor Simulation
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/edge-computing-iot-gateway.git

# Install
pip install -r requirements.txt

# Run Gateway (Simulate 5 devices)
python src/main.py --devices 5
```

## 📄 License

MIT License
