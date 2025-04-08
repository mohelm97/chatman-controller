# 🟡 Chatman Controller

<p align="center">
  <img src="https://raw.githubusercontent.com/mohelm97/chatman-controller/master/assets/chatman.png" width="350" alt="Chatman Toy">
</p>

A reverse-engineered controller for the **Chatman toy**, allowing you to bring it back to life! Originally designed as a USB-connected talking assistant for kids, Chatman is no longer supported by its manufacturer — but that doesn't mean it's useless. This project lets you control its **LED matrix**, **eye**, **hand**, and **antenna movements** using Python.

---

## 🎉 Features

-   ✅ Control Chatman's **LED matrix** (3x8) in real time
-   👁️ Move **eyes**, **hands**, and **antenna**
-   🖥️ GUI (`chatman_gui`) for easy control
-   🧑‍💻 CLI (`chatman_cli`) for scripting or automation
-   🔌 USB HID communication with the Chatman device

---

## 🧠 Why This Exists

The official Chatman software and website are now discontinued, leaving the hardware unsupported. This project reverse-engineers the USB commands sent to the toy, allowing anyone to repurpose it — whether for fun, education, or building a retro-styled virtual assistant.

---

## 🚀 Getting Started

### 1. Install Chatman Controller via pip

The `chatman-controller` package is now available on PyPI. To install it, simply run:

```bash
pip install chatman-controller
```

This will install all the necessary dependencies for communication with the Chatman device, including `hidapi` for USB HID communication.

### 2. Connect Your Chatman Toy

Make sure your Chatman device is plugged into a USB port before launching the app.

---

## 🖥️ Running the GUI

<p align="center">
  <img src="https://raw.githubusercontent.com/mohelm97/chatman-controller/master/assets/chatman_gui.png" width="400" alt="Chatman GUI Screenshot">
</p>

```bash
chatman_gui
```

This will launch a control panel where you can:

-   Toggle the LED matrix (3x8 grid)
-   Choose eye, hand, and antenna movement
-   See the resulting hex code for your LED configuration

If the device fails to connect, an error will be shown.

---

## 🔧 Running the CLI

You can control Chatman directly from the terminal using the CLI tool `chatman_cli.py`.

### ▶ Interactive Mode

Run without arguments or use `--interactive` to enter an interactive session:

```bash
chatman_cli
```

In this mode, you'll be prompted to choose eye, hand, and antenna movements, as well as LED values for Chatman's face.

### ▶ One-Time Command Mode

Provide movement and LED values directly via command-line arguments:

```bash
chatman_cli --eyes EYES_OPEN --hands HANDS_UP --antenna ANTENNAS_OUT --leds FF 00 AA
```

-   **--eyes**: Choose from:
    -   `EYES_CLOSED`, `EYES_ONE_THIRD_OPEN`, `EYES_TWO_THIRDS_OPEN`, `EYES_OPEN`, `NO_MOVEMENT`
-   **--hands**: Choose from:

    -   `HANDS_DOWN`, `HANDS_ONE_THIRD_UP`, `HANDS_TWO_THIRDS_UP`, `HANDS_UP`, `NO_MOVEMENT`

-   **--antenna**: Choose from:

    -   `ANTENNAS_IN`, `ANTENNAS_CENTER`, `ANTENNAS_OUT`, `NO_MOVEMENT`

-   **--leds**: Provide 3 hexadecimal values for the face LEDs:
    -   e.g., `--leds FF 00 AA`

### ▶ No Reset Option

If you don’t want to reset Chatman on startup, use the `--no-reset` flag:

```bash
chatman_cli --no-reset --eyes EYES_OPEN --hands HANDS_UP --antenna ANTENNAS_CENTER --leds 00 FF 00
```

> 💡 You typically only need to reset Chatman once — usually on the **first command after plugging it in**. After that, you should use `--no-reset`.

---

## 🧑‍💻 Using the Chatman Controller in Python

If you'd prefer to control the Chatman toy directly from your Python code, you can use the `ChatmanController` class, which provides an easy-to-use API for controlling the toy's movements and LED matrix.

### Example Usage:

```python
from chatman_controller import ChatmanController, EyeMovement, HandMovement, AntennaMovement

# Initialize the ChatmanController
controller = ChatmanController()

# Move the eyes, hands, and antenna, and set the LED matrix
controller.move(
    EyeMovement.EYES_CLOSED,         # Eye movement
    HandMovement.HANDS_UP,           # Hand movement
    AntennaMovement.ANTENNAS_IN,     # Antenna movement
    [0x3C, 0x7E, 0x00]               # LED matrix (3x8)
)
```

### Parameters:

-   **EyeMovement**: Controls the eye position.

    -   Options: `EYES_CLOSED`, `EYES_ONE_THIRD_OPEN`, `EYES_TWO_THIRDS_OPEN`, `EYES_OPEN`, `NO_MOVEMENT`

-   **HandMovement**: Controls the hand position.

    -   Options: `HANDS_DOWN`, `HANDS_ONE_THIRD_UP`, `HANDS_TWO_THIRDS_UP`, `HANDS_UP`, `NO_MOVEMENT`

-   **AntennaMovement**: Controls the antenna position.

    -   Options: `ANTENNAS_IN`, `ANTENNAS_CENTER`, `ANTENNAS_OUT`, `NO_MOVEMENT`

-   **LED Matrix**: A list of 3 hexadecimal values representing the LED matrix (3x8 grid). Each value should be in the range `0x00` to `0xFF`.

---

## 🛠️ Extend This Project

Here are a few fun ideas:

-   🎙️ Add voice control
-   🤖 Use a local LLM or OpenAI API to turn it into a chat-based assistant
-   🎵 Make it dance to music by analyzing sound

---

## 🙌 Credits

Created by **Mohammed N. Almadhoun**

Email: mohelm97@gmail.com

Feel free to fork, improve, or reach out if you’ve built something cool with it!
