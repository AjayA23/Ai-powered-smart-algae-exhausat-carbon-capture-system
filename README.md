# 🌿 AI-Powered Smart Algae Exhaust Carbon Capture System

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-red?logo=streamlit)](https://ai-powered-smart-algae-exhausat-carbon-capture-system-syer5tuc.streamlit.app/)

[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/AjayA23/Ai-powered-smart-algae-exhausat-carbon-capture-system)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)

[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)

---

## 📌 Project Overview

The **AI-Powered Smart Algae Exhaust Carbon Capture System** is an IoT and AI-based environmental monitoring system designed to demonstrate algae-based carbon capture from exhaust air.

The system uses **microalgae to absorb carbon dioxide from air** while continuously monitoring environmental parameters.

The project combines:

* 🌱 Microalgae-based carbon capture
* 🤖 Artificial Intelligence / Machine Learning
* 📡 IoT monitoring
* 🌫️ MQ135 air-quality sensors
* 💨 Automatic air-pump control
* 🌡️ Temperature monitoring
* 💧 Water-level monitoring
* 💡 Automatic LED control
* 📊 Carbon capture efficiency estimation

---

## 🚀 Live Demo

### 🌐 Try the Application

**[👉 Open Live Demo](https://ai-powered-smart-algae-exhausat-carbon-capture-system-syer5tuc.streamlit.app/)**

The Streamlit dashboard provides an interface for monitoring sensor values and viewing the system's carbon-capture-related parameters.

---

## 🎯 Objectives

The main objectives of this project are:

* Monitor air quality before and after the algae tank.
* Demonstrate algae-based carbon capture.
* Automatically control the air pump.
* Monitor algae tank temperature.
* Monitor water level.
* Estimate carbon capture efficiency.
* Apply Machine Learning for efficiency prediction.
* Develop an IoT-based environmental monitoring system.
* Provide a smart platform for environmental monitoring and analysis.

---

## 🏗️ System Architecture

```text
                         EXHAUST AIR
                              │
                              ▼
                     ┌────────────────┐
                     │  MQ135 INPUT   │
                     └───────┬────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │    AIR PUMP    │
                     └───────┬────────┘
                             │
                             ▼
              ┌─────────────────────────────┐
              │          ALGAE TANK         │
              │                             │
              │         MICROALGAE          │
              │                             │
              │   🌡 Temperature Sensor    │
              │   💧 Water-Level Sensor     │
              └──────────────┬──────────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │  MQ135 OUTPUT  │
                     └───────┬────────┘
                             │
                             ▼
                          ┌───────┐
                          │ ESP32 │
                          └───┬───┘
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
          ┌──────────────┐          ┌──────────────┐
          │ Relay Module │          │  AI / ML     │
          └──────┬───────┘          │    Model     │
                 │                  └──────┬───────┘
            ┌────┴────┐                     │
            ▼         ▼                     ▼
       Air Pump      LED             Capture Efficiency
```

---

## ⚙️ Working Principle

### 1. Exhaust Air Input

Exhaust air enters the system through the input section.

### 2. Input Air Monitoring

The first **MQ135 sensor** measures the incoming air-quality level.

### 3. Air Pump

The air pump pushes the air through the algae tank.

### 4. Algae-Based Carbon Capture

The air passes through the algae tank where microalgae can utilize carbon dioxide as part of their biological growth process.

### 5. Output Monitoring

After passing through the algae tank, the second MQ135 sensor measures the output air.

### 6. ESP32 Processing

The ESP32 collects sensor values and controls the connected devices.

### 7. Efficiency Calculation

The input and output readings are compared to estimate capture efficiency.

### 8. AI Prediction

The Machine Learning model can use sensor and environmental data to estimate carbon capture efficiency.

---

## 🧰 Hardware Components

| Component                  |    Quantity |
| -------------------------- | ----------: |
| ESP32 Development Board    |           1 |
| MQ135 Sensor               |           2 |
| Algae Tank                 |           1 |
| Microalgae                 | As required |
| Air Pump                   |           1 |
| Relay Module               |           1 |
| DS18B20 Temperature Sensor |           1 |
| Water-Level Sensor         |           1 |
| LED / Lighting System      |           1 |
| 12V Power Adapter          |           1 |
| Connecting Wires           | As required |
| Air Tubes                  | As required |

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

### Relay Configuration

* **Air Pump Relay:** Active LOW
* **LED Relay:** Active HIGH

---

## 🤖 Artificial Intelligence / Machine Learning

The project uses Machine Learning to estimate **carbon capture efficiency** from sensor and environmental parameters.

### Machine Learning Algorithm

```text
Random Forest Regressor
```

### Possible Input Parameters

* MQ135 Input Reading
* MQ135 Output Reading
* Temperature
* Water Level
* Other collected sensor parameters

### Prediction Target

```text
CaptureEfficiency_percent
```

The trained model can be stored in the project as:

```text
algae_model.keras
```

or another compatible model format depending on the implementation.

---

## 🔄 Automatic Control

### 💨 Air Pump Control

When the input air-quality reading exceeds the configured threshold:

```text
MQ135 Input > 1200
        │
        ▼
   Air Pump ON
```

The ESP32 activates the relay connected to the air pump.

### 💡 LED Control

When the configured temperature condition exceeds the project threshold:

```text
Temperature > 30°C
        │
        ▼
 LED Control Activated
```

These thresholds can be modified according to the experimental setup.

---

## 📊 Capture Efficiency

A basic efficiency calculation can be represented as:

```text
Capture Efficiency (%) =
((Input Reading - Output Reading) / Input Reading) × 100
```

### Example

```text
Input Reading  = 1000
Output Reading = 700

Efficiency =
((1000 - 700) / 1000) × 100

Efficiency = 30%
```

> **Note:** MQ135 is a general-purpose air-quality sensor. Its raw analog output should not automatically be interpreted as an exact CO₂ concentration without proper calibration.

---

## 📈 System Monitoring

The system can monitor and display:

* 🌫️ Input MQ135 reading
* 🌱 Output MQ135 reading
* 📊 Capture efficiency
* 🤖 AI-predicted efficiency
* 🌡️ Temperature
* 💧 Water-level status
* 💨 Air-pump status
* 💡 LED status
* ⚙️ Automated control status

---

## 📁 Project Structure

```text
Ai-powered-smart-algae-exhausat-carbon-capture-system/
│
├── README.md
├── requirements.txt
├── app.py
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

* Python 3.10+
* Arduino IDE
* ESP32 Board Package
* Visual Studio Code
* Streamlit
* TensorFlow
* NumPy
* Pandas
* Scikit-learn
* Joblib
* Matplotlib
* Seaborn
* Plotly

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AjayA23/Ai-powered-smart-algae-exhausat-carbon-capture-system.git
```

### 2. Open the Project Folder

```bash
cd Ai-powered-smart-algae-exhausat-carbon-capture-system
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

Run the following command:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📄 requirements.txt

```text
tensorflow
numpy
pandas
scikit-learn
joblib
matplotlib
seaborn
plotly
streamlit
```

---

## 🌍 Applications

The system can be explored for:

* 🏭 Industrial exhaust monitoring
* 🌱 Environmental monitoring
* 🌿 Algae-based carbon capture research
* 📡 IoT-based pollution monitoring
* 🧪 Academic and educational projects
* 🌎 Sustainable technology research
* 📊 Smart environmental data analysis

---

## 🔮 Future Scope

Future improvements can include:

* Dedicated calibrated CO₂ sensor
* Cloud-based IoT monitoring
* Mobile application
* Real-time database
* Automated algae health monitoring
* Solar-powered operation
* Improved Machine Learning models
* Multiple algae tanks
* Long-term carbon capture analysis
* Remote monitoring and alerts
* Automatic data logging
* Advanced sensor calibration

---

## ⚠️ Important Note

The **MQ135** is a general-purpose air-quality sensor. Raw MQ135 readings should not be directly considered as precise CO₂ concentration values without proper calibration.

This project is an **experimental and educational prototype** demonstrating the integration of:

**IoT + Artificial Intelligence + Machine Learning + Sensors + Algae-Based Carbon Capture**

Actual carbon capture performance depends on factors such as algae species, lighting, temperature, gas flow rate, tank design, sensor calibration, and operating conditions.

---

## 👨‍💻 Author

### Devanand Amrute

GitHub:
https://github.com/AjayA23

---

## 🔗 Project Links

### 🌐 Live Demo

https://ai-powered-smart-algae-exhausat-carbon-capture-system-syer5tuc.streamlit.app/

### 💻 GitHub Repository

https://github.com/AjayA23/Ai-powered-smart-algae-exhausat-carbon-capture-system

---

## 📜 License

This project is intended for educational and research purposes.

An open-source license such as the **MIT License** can be added if you want to allow others to use, modify, and distribute the project.

---

## ⭐ Support

If you find this project useful, you can **star the GitHub repository** and share the project with others interested in AI, IoT, environmental monitoring, and sustainable technology.
