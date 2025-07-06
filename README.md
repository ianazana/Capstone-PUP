# 🌿 IoT-Based Environmental Monitoring and Actuation System for Greenhouse Automation

This project implements an **IoT-based monitoring and actuation system** deployed in the greenhouse of **Pio Del Pilar Elementary School**, designed to automate environmental control using sensors and actuators connected to a Raspberry Pi.

---

## 📍 Project Location
📌 **Pio Del Pilar Elementary School – Greenhouse**

---

## 🧠 Overview

The system gathers real-time data from environmental sensors (temperature, humidity, light, and soil moisture) and activates corresponding actuators when specific thresholds are met. All logic is handled by a **Raspberry Pi**, and the system is controllable and viewable remotely through the **Blynk IoT app**.

---

## 🛠 Hardware Components

| Component                  | Quantity | Function                                           |
|----------------------------|----------|----------------------------------------------------|
| Raspberry Pi              | 1        | Central controller                                 |
| 8-Channel Relay Module     | 1        | Controls actuators (fans, lights, solenoids)       |
| DHT11 Temperature/Humidity Sensor | 1 | Reads air temp and humidity                        |
| Light Sensor (GY-30)       | 1        | Detects ambient light                              |
| Soil Moisture Sensors      | 5        | Measures moisture in different soil points         |
| Exhaust Fans               | 2        | Circulate air when temp/humidity is too high       |
| Solenoid Valves (modified)| 2+       | Irrigation via tubes/pipes                         |
| RGB Lights                 | 1+       | Supplemental lighting based on ambient levels      |

---

## 🔄 How It Works

### 📡 Sensors
- **DHT11** reads temperature and humidity.
- **GY-30 Light Sensor** captures light intensity.
- **5 Soil Moisture Sensors** monitor soil dryness across zones.

### ⚙️ Actuators
- **Relay 1-8**: Control exhaust fans, RGB lights, solenoid valves.
- Based on sensor input:
  - Fans activate when the temperature is too high.
  - Valves open when soil is too dry.
  - Lights turn on when it's too dark.

### 📲 IoT Integration via Blynk
- Real-time data is streamed to the Blynk mobile app.
- Actuators can be manually toggled or auto-triggered.
- Provides remote access and visualization.

---

## 📂 Code Summary

The main code integrates:
- `Adafruit_DHT` and `smbus2` for reading sensors
- `RPi.GPIO` for GPIO pin control
- `blynklib` for remote monitoring via Blynk

> See sample in [`raspi_code.py`](#) (Replace with real path once uploaded)

Key functions:
```python
def read_dht22():  # Read temp & humidity
def read_gy30():   # Read light level
def read_soil_moisture(pin):  # Read soil sensors
