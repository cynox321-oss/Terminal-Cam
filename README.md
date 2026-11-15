# 📷 Live ASCII Webcam

A lightweight Python application that converts live webcam footage into **real-time ASCII art** directly inside your terminal.

Using OpenCV and NumPy, it captures webcam frames, converts them into grayscale, resizes them, and maps brightness levels to ASCII characters to create a live text-based video feed.

## ✨ Features

- 🎥 Real-time webcam capture
- 🔤 Converts video frames into ASCII characters
- ⚡ Live terminal rendering
- 🌑 Grayscale brightness mapping
- 📐 Automatically adjusts output width to terminal size
- 🐍 Built with Python, OpenCV and NumPy

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam access and image processing |
| NumPy | Pixel and brightness calculations |
| Sys | Terminal output handling |

## 📦 Installation

**1. Clone the repository**

```bash
git clone https://github.com/cynox321-oss/LIVE-ASCII-WEBCAM.git
```

**2. Open the project directory**

```bash
cd LIVE-ASCII-WEBCAM
```

**3. Install dependencies**

```bash
pip install opencv-python numpy
```

## 🚀 Usage

Run the Python script:

```bash
python main.py
```

Make sure your webcam is connected and accessible.

The application will start capturing live video and display it as ASCII art in your terminal.

Press `Ctrl + C` to stop the program.

## ⚙️ How It Works

1. Captures frames from the webcam using OpenCV.
2. Converts each frame into grayscale.
3. Resizes the frame to fit the terminal width.
4. Maps pixel brightness values to ASCII characters.
5. Prints the generated ASCII frame directly in the terminal.
6. Repeats continuously to create a live video effect.

## 📁 Project Structure

```text
LIVE-ASCII-WEBCAM/
│
├── main.py
└── README.md
```

## 👨‍💻 Author

**Karan Kousik**

- GitHub: [@cynox321-oss](https://github.com/cynox321-oss)
- Repository: [LIVE-ASCII-WEBCAM](https://github.com/cynox321-oss/LIVE-ASCII-WEBCAM)

---

⭐ If you find this project interesting, consider giving the repository a star!

*Built with Python, pixels, and a little bit of terminal magic.*
