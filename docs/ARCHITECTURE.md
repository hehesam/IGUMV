# IGUMV Architecture Documentation

## System Architecture Overview

The IGUMV (Interactive Game Using Machine Vision) system follows a modular architecture that separates computer vision processing from game integration, enabling flexible development and maintenance.

## Component Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    IGUMV System                             │
├─────────────────────────────────────────────────────────────┤
│  Computer Vision Layer                                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐│
│  │  HSV Filtering  │  │ Ball Tracking   │  │ Collision Det.  ││
│  │                 │  │                 │  │                 ││
│  │ • Threshold     │  │ • Contour Det.  │  │ • Angle Calc.   ││
│  │ • Morphology    │  │ • Centroid      │  │ • Grid Zones    ││
│  │ • Color Space   │  │ • Trajectory    │  │ • Event Trigger ││
│  └─────────────────┘  └─────────────────┘  └─────────────────┘│
├─────────────────────────────────────────────────────────────┤
│  Communication Layer                                        │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐│
│  │  UDP Protocol   │  │ Audio Feedback  │  │ Input Control   ││
│  │                 │  │                 │  │                 ││
│  │ • Socket Comm.  │  │ • Sound Effects │  │ • Key Automation││
│  │ • Data Serializ.│  │ • Event Audio   │  │ • Game Control  ││
│  └─────────────────┘  └─────────────────┘  └─────────────────┘│
├─────────────────────────────────────────────────────────────┤
│  Unity Game Layer                                           │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐│
│  │ UDP Receiver    │  │ Game Logic      │  │ Visual Feedback ││
│  │                 │  │                 │  │                 ││
│  │ • Data Reception│  │ • Score System  │  │ • UI Updates    ││
│  │ • Event Parsing │  │ • Game State    │  │ • Animations    ││
│  └─────────────────┘  └─────────────────┘  └─────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## Data Flow Architecture

### 1. Input Processing
```
Camera Feed → HSV Conversion → Threshold Application → Morphological Operations
```

### 2. Object Detection
```
Processed Frame → Contour Detection → Ball Identification → Centroid Calculation
```

### 3. Motion Analysis
```
Ball Positions → Trajectory Calculation → Angle Analysis → Collision Detection
```

### 4. Output Generation
```
Collision Events → UDP Transmission → Unity Reception → Game Response
```

## Module Dependencies

### Core Dependencies
- **OpenCV**: Computer vision operations
- **NumPy**: Numerical computations
- **imutils**: Image processing utilities

### Communication Dependencies
- **Socket**: UDP networking
- **Threading**: Asynchronous communication

### Interface Dependencies
- **pygame**: Audio feedback
- **pyautogui**: Input automation

## Design Patterns

### 1. Observer Pattern
- Ball detection events trigger multiple responses (audio, UDP, automation)
- Collision detection notifies multiple subsystems

### 2. Strategy Pattern
- Different tracking algorithms (v1, v2) implement common interface
- HSV filtering strategies can be swapped

### 3. Factory Pattern
- Configuration objects created based on setup parameters
- Different camera configurations instantiated as needed

## Performance Considerations

### Optimization Strategies

1. **Frame Rate Management**
   - Adaptive FPS based on processing load
   - Skip frame processing when necessary

2. **Memory Efficiency**
   - Reuse image buffers
   - Minimal object allocation in main loop

3. **Processing Pipeline**
   - Early exit conditions for failed detection
   - Region of Interest (ROI) processing

### Scalability

- **Horizontal**: Multiple camera support
- **Vertical**: Enhanced algorithm complexity
- **Modular**: Easy integration of new features

## Configuration Management

### Static Configuration
- `config/config.py`: System parameters
- `config/hsv_thresholds.txt`: Detection thresholds

### Dynamic Configuration
- Interactive trackbar adjustments
- Runtime parameter updates

## Error Handling Strategy

### Camera Failures
- Graceful degradation
- Error logging and recovery

### Network Issues
- UDP timeout handling
- Connection retry logic

### Detection Failures
- Robust fallback mechanisms
- State preservation

## Security Considerations

### Network Security
- Local UDP communication only
- No external network exposure

### Input Validation
- Camera parameter bounds checking
- HSV value range validation

## Testing Architecture

### Unit Tests
- Individual component testing
- Mock camera input for testing

### Integration Tests
- End-to-end system validation
- Performance benchmarking

### Stress Tests
- High-frequency detection scenarios
- Memory leak detection

## Extension Points

### New Detection Algorithms
- Implement `BallDetector` interface
- Register in detection factory

### Additional Game Engines
- Implement communication protocol
- Create engine-specific adapters

### Enhanced Feedback Systems
- Visual feedback overlays
- Haptic feedback integration

## Documentation Structure

```
docs/
├── ARCHITECTURE.md     # This file
├── API.md             # API documentation
├── SETUP.md           # Detailed setup guide
├── TROUBLESHOOTING.md # Common issues and solutions
└── EXAMPLES.md        # Usage examples and tutorials
```

This architecture ensures maintainability, extensibility, and clear separation of concerns while providing robust real-time performance for the exergame application.