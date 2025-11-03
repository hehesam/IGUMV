# Changelog

All notable changes to the IGUMV project will be documented in this file.

## [2.0.0] - 2024-11-03 - Repository Reorganization

### Added
- **New organized directory structure**:
  - `src/computer_vision/` - Core computer vision modules
  - `src/unity_integration/` - Unity game integration components
  - `config/` - Configuration files and parameters
  - `docs/` - Comprehensive documentation
  - `tests/` - Test files and utilities
  - `assets/` - Asset files (sounds, images)
  - `build/` - Build artifacts and specifications

- **Comprehensive documentation**:
  - Updated README.md with detailed project description
  - ARCHITECTURE.md - System architecture overview
  - API.md - Complete API documentation
  - TROUBLESHOOTING.md - Common issues and solutions
  - Unity integration guide

- **Configuration management**:
  - `config/config.py` - Centralized configuration parameters
  - `config/hsv_thresholds.txt` - HSV threshold values
  - `requirements.txt` - Python dependencies

### Changed
- **File organization with descriptive names**:
  - `ball_detection.py` → `src/computer_vision/main_ball_tracker.py`
  - `ball_detection_class.py` → `src/computer_vision/hsv_filter.py`
  - `ball_detection_2.py` → `src/computer_vision/ball_tracker_v2.py`
  - `multiple_frames.py` → `src/computer_vision/frame_processor.py`
  - `build_test.py` → `tests/automation_test.py`
  - `threshold.txt` → `config/hsv_thresholds.txt`

- **Unity integration improvements**:
  - Enhanced `UDPReceive.cs` documentation
  - Detailed setup instructions
  - Integration examples and best practices

- **README.md completely rewritten**:
  - Added project overview and features
  - Technical implementation details
  - Setup and usage instructions
  - Research insights and learning outcomes

### Technical Improvements
- **Better code organization**: Logical separation of concerns
- **Enhanced documentation**: API references and architecture guides
- **Improved maintainability**: Clear file structure and naming conventions
- **Better user experience**: Comprehensive setup and troubleshooting guides

### Research Context
This reorganization reflects the project's evolution from a simple ball tracking experiment to a comprehensive exergame system demonstrating:
- HSV thresholding for robust object detection
- Geometric angle calculation for collision detection
- Real-time computer vision processing
- Unity game integration via UDP communication
- Trade-offs between accuracy and efficiency in motion tracking

### Migration Notes
- **Old file locations**: All original files remain in `image_processing/` and `unity_game/` directories
- **New structure**: Use files in `src/` directory for development
- **Configuration**: Update any hardcoded paths to use new structure
- **Dependencies**: Install requirements using `pip install -r requirements.txt`

## [1.0.0] - Original Implementation

### Features
- Basic ball detection using HSV color space
- Interactive HSV threshold calibration
- Grid-based collision detection
- UDP communication with Unity
- Audio feedback for collisions
- Keyboard automation for game control

### Components
- `ball_detection.py` - Main tracking application
- `ball_detection_class.py` - HSV filtering class
- `ball_detection_2.py` - Enhanced tracking version
- `UDPReceive.cs` - Unity UDP receiver
- Basic documentation and setup notes