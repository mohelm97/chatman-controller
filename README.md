# 🟡 Chatman Controller

<p align="center">
  <img src="assets/chatman.png" width="350" alt="Chatman Toy">
</p>

A reverse-engineered controller for the **Chatman toy**, allowing you to bring it back to life! Originally designed as a USB-connected talking assistant for kids, Chatman is no longer supported by its manufacturer — but that doesn't mean it's useless. This project lets you control its **LED matrix**, **eye**, **hand**, and **antenna movements** using Python.

---

## 🎉 Features

-   ✅ Control Chatman's **LED matrix** (3x8) in real time
-   👁️ Move **eyes**, **hands**, and **antenna**
-   🖥️ GUI (`chatman_gui.py`) for easy control
-   🧑‍💻 CLI (`chatman_cli.py`) for scripting or automation
-   🔌 USB HID communication with the Chatman device

---

## 🧠 Why This Exists

The official Chatman software and website are now discontinued, leaving the hardware unsupported. This project reverse-engineers the USB commands sent to the toy, allowing anyone to repurpose it — whether for fun, education, or building a retro-styled virtual assistant.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/chatman-controller.git
cd chatman-controller
```

### 2. Install Dependencies

Install required packages using:

```bash
pip install -r requirements.txt
```

This includes:

-   `hidapi` for USB HID communication

### 3. Connect Your Chatman Toy

Make sure your Chatman device is plugged into a USB port before launching the app.

---

## 🖥️ Running the GUI

<p align="center">
  <img src="assets/chatman_gui.png" width="400" alt="Chatman GUI Screenshot">
</p>

```bash
python chatman_gui.py
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
python chatman_cli.py
```

In this mode, you'll be prompted to choose eye, hand, and antenna movements, as well as LED values for Chatman's face.

### ▶ One-Time Command Mode

Provide movement and LED values directly via command-line arguments:

```bash
python chatman_cli.py --eyes EYES_OPEN --hands HANDS_UP --antenna ANTENNAS_OUT --leds FF 00 AA
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
python chatman_cli.py --no-reset --eyes EYES_OPEN --hands HANDS_UP --antenna ANTENNAS_CENTER --leds 00 FF 00
```

> 💡 You typically only need to reset Chatman once — usually on the **first command after plugging it in**. After that, you should use `--no-reset`.

---

## 🧩 Project Structure

```text
chatman_controller.py     # Main controller class + movement enums
chatman_gui.py            # Graphical interface using Tkinter
chatman_cli.py            # Command-line interface for advanced usage
requirements.txt          # Python dependencies
README.md                 # You are here!
```

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
