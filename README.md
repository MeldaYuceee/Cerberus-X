# Cerberus-X  
### Triple-Layer Anomaly Detection for UAV Survivability

Cerberus-X is a minimal, defense-inspired anomaly detection prototype designed to explore **multi-layer awareness** in UAV systems.

Instead of trusting a single signal, Cerberus-X watches **network behavior, RF conditions, and telemetry data together** to detect subtle but correlated anomalies that may indicate system compromise.

This project is part of a weekly learning path focused on **UAV safety, survivability, and defense-grade engineering mindset**.

---

## Core Idea

Real-world UAV failures rarely appear cleanly in a single metric.

- Network traffic may look *slightly* unusual  
- RF noise may rise *just a bit*  
- Telemetry may drift without fully breaking  

Individually, these signals may not trigger alarms.  
**Together, they form a pattern.**

Cerberus-X fuses weak indicators across multiple layers to maintain awareness when no single signal looks critical on its own.

---

## Architecture

Cerberus-X operates on three independent layers:

### 1. Network Layer
Monitors basic traffic behavior such as:
- Sudden packet spikes
- Throughput drops
- Short burst patterns resembling scans or instability

### 2. RF Layer
Observes radio conditions including:
- Noise floor increases
- Signal-to-noise ratio (SNR) drops
- Brief spectral irregularities

### 3. Telemetry Layer
Checks whether the UAV state still makes physical sense:
- Velocity mismatches
- Position jitter
- Rising Bit Error Rate (BER)

Each layer contributes a small anomaly score.

---

## Anomaly Scoring Logic

- Each layer produces a **weak signal**
- Scores are combined into a single anomaly value
- Correlated anomalies raise the system state faster than isolated ones

### System States

- **SAFE**  
  Normal fluctuations, expected behavior

- **SUSPICIOUS**  
  One or more weak anomalies detected

- **CRITICAL**  
  Multiple layers showing correlated abnormal behavior

The goal is not precision detection, but **early awareness through redundancy**.

---

## What This Project Is (and Is Not)

**Cerberus-X is:**
- A learning-focused prototype
- A demonstration of multi-layer thinking
- A foundation for future, more advanced systems

**Cerberus-X is not:**
- A production intrusion detection system
- A real-time embedded implementation
- A complete security solution

Simplicity is intentional — clarity over complexity.

---

## Motivation

This project was inspired by a key realization:

> One sensor can fail quietly.  
> Multiple layers failing together are much harder to miss.

Cerberus-X reflects how defense and avionics systems think about survivability — not just reacting to failures, but **maintaining awareness as conditions slowly degrade**.

---

## Related Work

Cerberus-X is part of a broader weekly exploration of UAV safety and defense concepts, including:

- **RAVEN-Link** — adaptive anti-jamming telemetry  
- **HADES** — basic GPS spoofing detection  
- **SilentHawk** — low-RCS radar visibility simulation  

Each project focuses on a different failure or awareness layer.

---

## Future Directions

Planned extensions include:
- Temporal anomaly correlation
- Mission-level risk scoring integration
- Telemetry replay and fault injection
- Lightweight embedded-oriented implementations

---

## Author

**Melda Yüce**  
Computer Engineering Student  
Focus: UAV systems, survivability, and defense-oriented software

---

## Disclaimer

This project is for **educational and research purposes only**.  
It does not represent real-world defense systems or operational security tools.
