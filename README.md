# Project Title: IoT Vehicle Controller

## Objective
This project implements an Internet of Things (IoT) based system for remotely controlling and monitoring a vehicle. It provides a graphical user interface (GUI) for issuing commands like movement and managing system security, serving as a foundation for smart vehicle functionalities and anti-theft measures.

---

## Tools & Technologies
- Programming Language: Python 3.x
- Frameworks: Tkinter (for GUI)
- Simulator: Custom Python GUI / (Mention if you use Wokwi or Device Simulator Express for hardware simulation if applicable)
- Dependencies: pyserial (if used for Arduino communication), other standard Python libraries. (You'll list these accurately in your `requirements.txt`)

---

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/marthanjoel/IoT-VECHILE-CONTROLLER.git
cd IoT-VECHILE-CONTROLLER
Use code with caution.

2. Create Virtual Environment (Recommended)
bash
python3 -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
Use code with caution.

3. Install Dependencies
bash
pip install -r requirements.txt
Use code with caution.

4. Upload Arduino Sketch
Open the vehicle_controller.ino (or similar) sketch in the Arduino IDE.
Select your Arduino board (Uno/Mega) and corresponding COM port.
Upload the sketch to your Arduino board(s).
5. Run the Project
bash
python3 main.py 
Use code with caution.
5. Screen shots
   <img width="1366" height="768" alt="Screenshot from 2025-09-19 15-17-38" src="https://github.com/user-attachments/assets/31d953ed-55cb-45b2-a6ab-5430f3893df1" />


---
Simulation Details
Sensor Emulated: Distance (currently "N/A" but designed for future integration)
Actuator Emulated: Vehicle movement controls (Forward, Backward, Left, Right, Stop)
Trigger Logic: System arming/disarming, vehicle movement commands sent to Arduino.
Screenshots
Include 2–3 screenshots showing:
Initial interface (showing "Connect Arduinos", "Disconnected" status, "Arm/Disarm System")
(If applicable, a screenshot showing connected status or a specific interaction)
Output behavior (e.g., system armed state, if visual feedback is implemented)

---
Observations
What worked well? (e.g., GUI responsiveness, successful communication with Arduino mockups, modular design)
Any bugs or challenges? (e.g., initial connectivity issues, delays in command execution, handling disconnections gracefully)
How was the simulation validated? (e.g., testing GUI button functionality, verifying serial output commands to a simulated Arduino or a real one without a physical vehicle)


----
Future Improvements
Integrate actual distance sensors and display live readings on the GUI.
Implement advanced security features like GPS tracking and remote engine disabling.
Enhance communication robustness using dedicated IoT protocols (e.g., MQTT).
Add logging capabilities for system events and alerts.
Develop a mobile application interface for remote control.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments
Thanks to the Tkinter and Arduino communities for their excellent resources and tools.
