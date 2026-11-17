# 📷 Terminal Cam — Live ASCII Webcam

A lightweight Python application that transforms your live webcam feed into real-time ASCII art directly inside your terminal.

Built using **Python, OpenCV, and NumPy**, Terminal Cam captures webcam frames, converts them into grayscale, and maps pixel brightness to ASCII characters to create a live text-based video experience.

## ✨ Features

- 🎥 **Real-Time Webcam Capture** — Captures live footage from your webcam.
- 🔤 **ASCII Art Conversion** — Converts video frames into ASCII characters.
- ⚡ **Live Terminal Rendering** — Displays the converted footage directly in your terminal.
- 🌑 **Grayscale Processing** — Uses pixel brightness to generate ASCII output.
- 📐 **Automatic Terminal Width Adjustment** — Adjusts output width to fit the terminal.
- 🐍 **Lightweight Python Application** — Built with Python, OpenCV, and NumPy.

## 📸 Screenshots

### Screenshot 1
![Terminal Cam Screenshot 1](Screenshot%202026-11-17%20213736.png)

### Screenshot 2
![Terminal Cam Screenshot 2](Screenshot%202026-11-17%20213651.png)

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam access and image processing |
| NumPy | Pixel manipulation and brightness calculations |
| Sys | Terminal output handling |

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/cynox321-oss/Terminal-Cam.git
```

### 2. Navigate to the project directory

```bash
cd Terminal-Cam
```

### 3. Install dependencies

```bash
pip install opencv-python numpy
```

## 🚀 Usage

Run the application:

```bash
python ASCII.py
```

Make sure your webcam is connected and accessible.

The application will start capturing live video and display the footage as ASCII art directly in your terminal.

To stop the application, press:

```text
Ctrl + C
```

## ⚙️ How It Works

1. Captures live webcam frames using OpenCV.
2. Converts each frame into grayscale.
3. Resizes the frame to fit the terminal width.
4. Maps pixel brightness values to ASCII characters.
5. Prints the generated ASCII frame in the terminal.
6. Repeats the process to create a live video effect.

## 📁 Project Structure

```text
Terminal-Cam/
│
├── ASCII.py
├── README.md
├── Screenshot 2026-11-17 213651.png
└── Screenshot 2026-11-17 213736.png
```

## 👨‍💻 Author

**Karan Kousik**

- GitHub: [@cynox321-oss](https://github.com/cynox321-oss)
- Repository: [Terminal-Cam](https://github.com/cynox321-oss/Terminal-Cam)

---

⭐ If you find this project interesting, consider giving the repository a star!

**Built with Python, pixels, and a little bit of terminal magic.**
