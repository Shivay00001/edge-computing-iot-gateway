import time
import argparse
from src.gateway import EdgeGateway
from src.device_sim import SensorSimulator

def main():
    parser = argparse.ArgumentParser(description="IoT Edge Gateway Simulator")
    parser.add_argument("--devices", type=int, default=3, help="Number of simulated devices")
    parser.add_argument("--duration", type=int, default=20, help="Simulation duration in seconds")
    
    args = parser.parse_args()
    
    print("--- Edge Computing IoT Gateway Demo ---")
    
    gateway = EdgeGateway()
    msg_sims = []
    
    # Initialize Devices
    for i in range(args.devices):
        dev_id = f"sensor_{i+1:03d}"
        gateway.register_device(dev_id, "HVAC_SENSOR")
        sim = SensorSimulator(dev_id, gateway, interval=random.uniform(0.5, 2.0))
        msg_sims.append(sim)
        sim.start()
        
    print(f"Started {args.devices} devices. Running for {args.duration}s...")
    
    try:
        end_time = time.time() + args.duration
        while time.time() < end_time:
            gateway.health_check()
            time.sleep(2)
            
        print("\nStopping Simulation...")
        for sim in msg_sims:
            sim.stop()
        
        # Final flush
        gateway.upload_to_cloud()
        
    except KeyboardInterrupt:
        print("\nAborted.")

if __name__ == "__main__":
    import random # Lazy import fix
    main()
