# HSV Threshold Configuration
# These values define the HSV color range for ball detection
# Format: low_H low_S low_V high_H high_S high_V

# Default green ball detection values
# Hue: 46-80 (green range)
# Saturation: 65-255 (medium to high saturation)
# Value: 50-255 (medium to high brightness)

# Camera settings
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Detection parameters
MIN_BALL_RADIUS = 1
MAX_BALL_RADIUS = 500
BLUR_KERNEL_SIZE = 11

# Grid settings (for wall collision detection)
GRID_ROWS = 3
GRID_COLS = 3

# UDP communication settings
UDP_PORT = 5052
UDP_HOST = "localhost"

# Audio settings
SOUND_FILE = "hit1.wav"