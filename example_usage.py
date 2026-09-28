from client import BlackboardArchitecture

def main():
    bb = BlackboardArchitecture()
    bb.post("anomaly_score", 0.95)
    bb.register_ks("AlertKS", lambda s: s.get("anomaly_score", 0) > 0.8, lambda b: b.post("alert_sent", True), priority=10)
    fired = bb.step()
    print("Blackboard Pattern Verification:")
    print(f"Triggered KS: {fired}")
    print(f"Current State: {bb.state}")

if __name__ == "__main__":
    main()
