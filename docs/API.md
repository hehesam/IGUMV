# IGUMV API Documentation

## Computer Vision API

### BallTracker Class

#### Methods

##### `__init__(camera_index=0)`
Initializes the ball tracking system.

**Parameters:**
- `camera_index` (int): Camera device index (default: 0)

**Example:**
```python
tracker = BallTracker(camera_index=0)
```

##### `calibrate_hsv_thresholds()`
Opens interactive HSV calibration interface.

**Returns:**
- `tuple`: (low_H, low_S, low_V, high_H, high_S, high_V)

##### `detect_ball(frame)`
Detects ball in the given frame.

**Parameters:**
- `frame` (numpy.ndarray): Input frame

**Returns:**
- `dict`: Detection result
  ```python
  {
      'detected': bool,
      'center': tuple(x, y),
      'radius': float,
      'contour': numpy.ndarray
  }
  ```

##### `calculate_collision_angle(centers_history)`
Calculates collision angle from trajectory.

**Parameters:**
- `centers_history` (list): List of (x, y) center positions

**Returns:**
- `float`: Collision angle in degrees

### HSVFilter Class

#### Methods

##### `__init__()`
Initializes HSV filtering interface.

##### `create_trackbars(window_name)`
Creates HSV adjustment trackbars.

**Parameters:**
- `window_name` (str): OpenCV window name

##### `apply_filter(frame)`
Applies HSV filtering to frame.

**Parameters:**
- `frame` (numpy.ndarray): Input frame

**Returns:**
- `numpy.ndarray`: Filtered binary mask

## Unity Integration API

### UDPReceive Component

#### Properties

##### `port` (int)
UDP listening port (default: 5052)

##### `startReceiving` (bool)
Controls UDP reception state

##### `printToConsole` (bool)
Enable console logging of received data

##### `data` (string)
Last received data string

#### Methods

##### `Start()`
Initializes UDP receiver thread.

##### `ReceiveData()`
Background thread method for receiving UDP data.

## Communication Protocol

### Python to Unity Data Format

#### Collision Event
```json
{
    "type": "collision",
    "zone": 1-9,
    "angle": 45.5,
    "timestamp": 1634567890.123
}
```

#### Ball Position Update
```json
{
    "type": "position",
    "x": 320,
    "y": 240,
    "timestamp": 1634567890.123
}
```

#### Game State
```json
{
    "type": "game_state",
    "state": "playing",
    "score": 150
}
```

## Configuration API

### Configuration Parameters

#### Camera Settings
```python
CAMERA_INDEX = 0           # Camera device index
FRAME_WIDTH = 640          # Capture width
FRAME_HEIGHT = 480         # Capture height
```

#### Detection Parameters
```python
MIN_BALL_RADIUS = 1        # Minimum detectable radius
MAX_BALL_RADIUS = 500      # Maximum detectable radius
BLUR_KERNEL_SIZE = 11      # Gaussian blur kernel
```

#### HSV Thresholds
```python
HSV_LOWER = (46, 65, 50)   # Lower HSV bounds
HSV_UPPER = (80, 255, 255) # Upper HSV bounds
```

#### Grid Configuration
```python
GRID_ROWS = 3              # Collision grid rows
GRID_COLS = 3              # Collision grid columns
```

#### Network Settings
```python
UDP_PORT = 5052            # UDP communication port
UDP_HOST = "localhost"     # Target host address
```

## Utility Functions

### Image Processing

#### `stackImages(scale, imgArray)`
Stacks multiple images for display.

**Parameters:**
- `scale` (float): Scaling factor
- `imgArray` (list): Array of images to stack

**Returns:**
- `numpy.ndarray`: Stacked image

#### `gradient(pt1, pt2)`
Calculates gradient between two points.

**Parameters:**
- `pt1` (tuple): First point (x, y)
- `pt2` (tuple): Second point (x, y)

**Returns:**
- `float`: Gradient value

### Geometric Calculations

#### `getAngle(centers, frame, index, height, hit_state)`
Calculates collision angle from center points.

**Parameters:**
- `centers` (list): Ball center positions
- `frame` (numpy.ndarray): Current frame
- `index` (int): Frame index
- `height` (int): Frame height
- `hit_state` (bool): Current hit state

**Returns:**
- `bool`: Updated hit state

### Audio and Input

#### `keyWord(index)`
Triggers keyboard input based on zone index.

**Parameters:**
- `index` (int): Zone index (0-8)

#### `play_collision_sound()`
Plays collision sound effect.

## Error Codes

### Camera Errors
- `CAM_001`: Camera not found
- `CAM_002`: Camera initialization failed
- `CAM_003`: Frame capture timeout

### Detection Errors
- `DET_001`: No contours found
- `DET_002`: Ball size out of range
- `DET_003`: Multiple balls detected

### Network Errors
- `NET_001`: UDP socket creation failed
- `NET_002`: Connection timeout
- `NET_003`: Data transmission error

## Event System

### Event Types

#### Ball Detection Events
```python
{
    'type': 'ball_detected',
    'position': (x, y),
    'radius': float,
    'confidence': float
}
```

#### Collision Events
```python
{
    'type': 'collision',
    'zone': int,
    'angle': float,
    'velocity': float
}
```

#### System Events
```python
{
    'type': 'system_ready',
    'camera_initialized': bool,
    'calibration_complete': bool
}
```

## Performance Metrics

### Tracking Performance
- **FPS**: Frames processed per second
- **Latency**: Detection to output delay
- **Accuracy**: Detection success rate

### Memory Usage
- **Peak Memory**: Maximum memory consumption
- **Average Memory**: Typical memory usage
- **Memory Leaks**: Long-term memory growth

## Threading Model

### Main Thread
- GUI updates
- User interaction handling
- Frame display

### Processing Thread
- Image processing
- Ball detection
- Angle calculation

### Communication Thread
- UDP data transmission
- Audio playback
- Keyboard automation

## Examples

### Basic Usage
```python
from src.computer_vision.main_ball_tracker import BallTracker

# Initialize tracker
tracker = BallTracker()

# Calibrate thresholds
thresholds = tracker.calibrate_hsv_thresholds()

# Start tracking
tracker.start_tracking()
```

### Custom Configuration
```python
from config.config import *

# Override default settings
CAMERA_INDEX = 1
HSV_LOWER = (30, 50, 50)
HSV_UPPER = (90, 255, 255)

# Initialize with custom config
tracker = BallTracker(camera_index=CAMERA_INDEX)
```

### Unity Integration
```csharp
public class GameController : MonoBehaviour
{
    public UDPReceive udpReceive;
    
    void Update()
    {
        string data = udpReceive.data;
        if (!string.IsNullOrEmpty(data))
        {
            ProcessCollisionData(data);
        }
    }
}
```