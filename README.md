# IGUMV - Interactive Game Using Machine Vision

An exergame tracking module that combines computer vision with Unity game integration for real-time motion tracking and collision detection. This project was developed under the supervision of Prof. Rasti, focusing on HSV thresholding and geometric angle calculation for live feedback of ball collision detections with walls.

## 🎯 Project Overview

This system tracks a colored ball in real-time using computer vision techniques and provides feedback to a Unity-based exergame. The project demonstrates the trade-off between accuracy and efficiency in motion tracking applications and implements user-in-the-loop interactions for enhanced gaming experiences.

## 🌟 Key Features

- **Real-time Ball Tracking**: HSV color space thresholding for robust ball detection
- **Collision Detection**: Geometric angle calculation for wall collision detection
- **Unity Integration**: UDP communication between Python and Unity
- **Interactive Calibration**: Manual HSV threshold adjustment interface
- **Grid-based Zones**: 3x3 grid system for precise collision area detection
- **Audio Feedback**: Sound effects for collision events
- **Automated Input**: Keyboard automation for game interaction

## 🏗️ Project Structure

```
IGUMV/
├── src/
│   ├── computer_vision/          # Core computer vision modules
│   │   ├── main_ball_tracker.py   # Primary ball tracking application
│   │   ├── ball_tracker_v2.py     # Enhanced version with improvements
│   │   ├── hsv_filter.py          # HSV filtering class and utilities
│   │   └── frame_processor.py     # Frame processing utilities
│   └── unity_integration/         # Unity game integration
│       ├── UDPReceive.cs          # Unity UDP receiver script
│       └── README.md              # Unity setup instructions
├── config/                       # Configuration files
│   ├── config.py                 # Main configuration parameters
│   └── hsv_thresholds.txt        # HSV threshold values
├── tests/                        # Test files
│   └── automation_test.py        # Automation testing utilities
├── build/                        # Build artifacts
│   └── build_test.spec           # PyInstaller specification
├── docs/                         # Documentation
├── assets/                       # Asset files (sounds, images)
└── requirements.txt              # Python dependencies
```

## 🔧 Technical Implementation

### Computer Vision Pipeline

1. **Color Space Conversion**: BGR to HSV for better color detection
2. **Thresholding**: Dynamic HSV range filtering for ball isolation
3. **Morphological Operations**: Erosion and dilation for noise reduction
4. **Contour Detection**: Finding ball boundaries using OpenCV
5. **Centroid Calculation**: Precise ball position tracking
6. **Trajectory Analysis**: Angle calculation for collision prediction

### HSV Thresholding

The system uses HSV color space for robust ball detection:
- **Hue (H)**: Defines the color (46-80 for green objects)
- **Saturation (S)**: Color intensity (65-255 for vibrant colors)
- **Value (V)**: Brightness level (50-255 for visible objects)

### Geometric Angle Calculation

Collision detection uses geometric analysis:
- Track ball trajectory using multiple frame centers
- Calculate movement vectors and angles
- Detect wall collisions based on trajectory changes
- Provide real-time feedback to Unity game

## 🚀 Setup Instructions

### Prerequisites

- Python 3.7+
- OpenCV-compatible camera
- Unity 2019.4+ (for game integration)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hehesam/IGUMV.git
   cd IGUMV
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure camera settings** in `config/config.py`

4. **Calibrate HSV thresholds**:
   ```bash
   python src/computer_vision/main_ball_tracker.py
   ```

## 📖 Usage Guide

### Basic Ball Tracking

1. **Start the application**:
   ```bash
   python src/computer_vision/main_ball_tracker.py
   ```

2. **Calibration Phase**:
   - Adjust HSV trackbars for optimal ball detection
   - Click two points to confirm threshold values

3. **Zone Setup Phase**:
   - Click two corners to define tracking area
   - System automatically creates 3x3 collision grid

4. **Tracking Phase**:
   - Ball detection and collision tracking begins
   - Press 't' to terminate the application

### Unity Integration

1. **Setup Unity project**:
   - Import `UDPReceive.cs` into your Unity Assets folder
   - Create an empty GameObject and attach the script
   - Configure UDP port (default: 5052)

2. **Start communication**:
   - Run the Python ball tracker
   - Unity will receive collision data via UDP

## 🎛️ Configuration

### HSV Threshold Adjustment

Modify `config/hsv_thresholds.txt` or use the interactive trackbars:
```
46 65 50 80 255 255
```
Format: `low_H low_S low_V high_H high_S high_V`

### Camera Settings

Edit `config/config.py`:
```python
CAMERA_INDEX = 0        # Camera device index
FRAME_WIDTH = 640       # Capture width
FRAME_HEIGHT = 480      # Capture height
```

## 🔬 Research Insights

This project demonstrates several key concepts in computer vision and human-computer interaction:

### Accuracy vs. Efficiency Trade-offs

- **High Accuracy**: Detailed contour analysis and multi-frame tracking
- **High Efficiency**: Optimized HSV thresholding and minimal processing
- **Balance**: Adaptive algorithms that adjust based on system performance

### Motion Tracking Techniques

- **HSV Color Space**: More robust than RGB for varying lighting conditions
- **Morphological Operations**: Noise reduction without losing object shape
- **Trajectory Analysis**: Predictive collision detection using geometric calculations

### User-in-the-Loop Interactions

- **Interactive Calibration**: Real-time threshold adjustment
- **Visual Feedback**: Live visualization of detection pipeline
- **Adaptive Zones**: User-defined tracking areas for flexible gameplay

## 🛠️ Development

### Building Executable

To create a standalone executable:
```bash
pyinstaller build/build_test.spec
```

### Running Tests

```bash
python tests/automation_test.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is part of an academic internship under the supervision of Prof. Rasti.

## 🙏 Acknowledgments

- **Prof. Rasti** for supervision and guidance
- **OpenCV Community** for computer vision tools
- **Unity Technologies** for game engine integration

## 📧 Contact

For questions or collaboration opportunities, please open an issue in this repository.

---

*This project demonstrates the practical application of computer vision in interactive gaming and represents learning achievements in motion tracking, HSV color space processing, and real-time user interaction systems.*
