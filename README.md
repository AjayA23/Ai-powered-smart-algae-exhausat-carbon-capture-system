# 🌿 AI-Powered Smart Algae Exhaust Carbon Capture System

An IoT and AI-based carbon capture system that uses **microalgae to absorb CO₂ from exhaust air** while continuously monitoring environmental parameters.

The system uses an **ESP32**, dual **MQ135 sensors**, an algae tank, air pump, relay module, water-level sensor, and temperature sensor. AI/ML is used to estimate carbon capture efficiency and support automated control of the system.

---

## 🚀 Project Overview

The **AI-Powered Smart Algae Exhaust Carbon Capture System** is designed to reduce CO₂ emissions by passing exhaust air through an algae-based absorption system.

The system measures air quality before and after the algae tank:

**Exhaust Air → MQ135 Input → Algae Tank → MQ135 Output → Cleaned Air**

The ESP32 collects sensor data and controls the connected actuators automatically.

---

## 🎯 Objectives

* Monitor exhaust air quality in real time.
* Use microalgae for biological CO₂ absorption.
* Measure air quality before and after the algae tank.
* Automatically control the air pump.
* Monitor algae tank temperature and water level.
* Estimate carbon capture efficiency using Machine Learning.
* Provide a foundation for IoT-based environmental monitoring.

---

## 🧰 Hardware Components

* ESP32 Development Board
* MQ135 Sensor × 2
* Algae Tank
* Microalgae
* Air Pump
* Relay Module
* 12V Power Adapter
* Water-Level Sensor
* DS18B20 Temperature Sensor
* LED / Lighting System
* Connecting Wires
* Tubes / Air Pipes

---

## 🔌 ESP32 Pin Configuration

| Component                  | ESP32 Pin |
| -------------------------- | --------- |
| MQ135 Input                | GPIO 39   |
| MQ135 Output               | GPIO 32   |
| Water-Level Sensor         | GPIO 36   |
| DS18B20 Temperature Sensor | GPIO 4    |
| Air Pump Relay             | GPIO 12   |
| LED Relay                  | GPIO 13   |

### Relay Logic

* **Air Pump Relay:** Active LOW
* **LED Relay:** Active HIGH

---

## ⚙️ Working Principle

1. Exhaust air enters the system.
2. The first MQ135 sensor measures the incoming air quality.
3. The air is passed through the algae tank using an air pump.
4. Microalgae absorb a portion of the available carbon dioxide during the process.
5. The second MQ135 sensor measures the air quality after the algae tank.
6. The ESP32 compares input and output readings.
7. Capture efficiency is calculated from the sensor readings.
8. The air pump is automatically controlled according to the configured threshold.
9. The system monitors water level and temperature to maintain suitable algae conditions.
10. The AI/ML model can be used to estimate carbon capture efficiency from collected sensor data.

---

## 🤖 AI / Machine Learning

A Machine Learning model is used to estimate **Capture Efficiency (%)** based on sensor and environmental parameters.

The project uses a **Random Forest Regressor** for prediction.

Possible input parameters include:

* Input MQ135 reading
* Output MQ135 reading
* Temperature
* Water level
* Other collected system parameters

### ML Target

```text
CaptureEfficiency_percent
```

The trained model can be saved as:

```text
algae_model.keras
```

or as a compatible trained model file depending on the implementation.

---

## 🔄 Automatic Control

### Air Pump

When the input air-quality reading exceeds the configured threshold:

```text
MQ135 Input > 1200
        ↓
Air Pump ON
```

The pump can be automatically controlled through the relay module.

### LED / Algae Lighting

When the configured temperature condition is above the project threshold:

```text
Temperature > 30°C
        ↓
LED Control Activated
```

> These thresholds are configurable and should be calibrated according to the actual hardware, algae species, sensor characteristics, and experimental conditions.

---

## 📊 Capture Efficiency

A basic efficiency calculation can be represented as:

```text
Capture Efficiency (%) =
((Input Reading - Output Reading) / Input Reading) × 100
```

The actual MQ135 output should be properly calibrated before interpreting the readings as CO₂ concentration.

---

## 🏗️ System Architecture

```text
                 EXHAUST AIR
                     │
                     ▼
              ┌─────────────┐
              │ MQ135 INPUT │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │  AIR PUMP   │
              └──────┬──────┘
                     │
                     ▼
        ┌────────────────────────┐
        │       ALGAE TANK       │
        │                        │
        │      MICROALGAE        │
        │                        │
        │  Temperature Sensor    │
        │  Water-Level Sensor    │
        └───────────┬────────────┘
                    │
                    ▼
             ┌─────────────┐
             │ MQ135 OUTPUT│
             └──────┬──────┘
                    │
                    ▼
                 ESP32
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Relay Module        AI / ML Model
          │                   │
     ┌────┴────┐              ▼
     ▼         ▼       Capture Efficiency
 Air Pump     LED
```

---

## 📁 Suggested Project Structure

```text
Ai-powered-smart-algae-exhausat-carbon-capture-system/
│
├── README.md
├── requirements.txt
│
├── firmware/
│   └── esp32_code.ino
│
├── ai/
│   ├── train_model.py
│   ├── predict.py
│   └── algae_model.keras
│
├── data/
│   └── sensor_data.csv
│
├── diagrams/
│   ├── system_architecture.png
│   ├── block_diagram.png
│   └── circuit_diagram.png
│
└── dashboard/
    └── app.py
```

---

## 💻 Software Requirements

* Python 3.10 or newer
* Arduino IDE
* ESP32 Board Package
* VS Code / PyCharm / Jupyter Notebook
* Streamlit (if dashboard is used)

---

## 📦 Python Installation

Clone the repository:

```bash
git clone https://github.com/AjayA23/Ai-powered-smart-algae-exhausat-carbon-capture-system.git
```

Enter the project directory:

```bash
cd Ai-powered-smart-algae-exhausat-carbon-capture-system
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the AI / Dashboard

If the project contains a Streamlit dashboard:

```bash
streamlit run app.py
```

---

## 📈 Expected Output

The system can provide:

* 🌫️ Input air-quality reading
* 🌱 Output air-quality reading
* 💨 Air pump status
* 🌡️ Temperature
* 💧 Water-level status
* 📊 Capture efficiency
* 🤖 AI-predicted efficiency
* 💡 LED status
* ⚙️ Automated actuator control

---

## 🌍 Applications

* Industrial exhaust monitoring
* Environmental monitoring
* Educational projects
* Smart agriculture
* Algae-based carbon capture research
* IoT-based pollution monitoring
* Sustainable energy and environmental systems

---

## 🔮 Future Improvements

* Real CO₂ sensor integration for more accurate CO₂ measurement
* Cloud-based IoT dashboard
* Mobile application
* Real-time data logging
* Automated algae health monitoring
* Solar-powered operation
* Improved ML prediction models
* Multiple algae tanks for higher capture capacity
* Long-term performance analysis

---

## ⚠️ Important Note

The MQ135 is a **general-purpose air-quality sensor** and its analog output should not automatically be treated as a calibrated CO₂ concentration. Accurate CO₂ measurement requires appropriate calibration and, for quantitative CO₂ measurement, a dedicated CO₂ sensor.

This project is intended as an experimental/educational prototype for smart environmental monitoring and algae-based carbon capture.

---

## 👨‍💻 Author

devanand amrute

GitHub:
https://github.com/AjayA23

---

## 📜 License

This project is available for educational and research purposes. Add an appropriate open-source license to the repository if you want others to reuse and modify the code.
