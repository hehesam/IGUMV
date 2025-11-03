# IGUMV Troubleshooting Guide

## Common Issues and Solutions

### Camera Issues

#### Camera Not Detected
**Problem**: `cv2.VideoCapture()` returns false or no camera feed

**Solutions:**
1. Check camera connection and drivers
2. Try different camera indices (0, 1, 2, etc.)
3. Close other applications using the camera
4. Update camera drivers
5. Test with different USB ports

```python
# Test camera availability
import cv2
for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera {i} is available")
        cap.release()
```

#### Poor Frame Rate
**Problem**: Slow or choppy video processing

**Solutions:**
1. Reduce frame resolution in `config/config.py`
2. Optimize lighting conditions
3. Close unnecessary applications
4. Check CPU usage and memory

```python
# Set lower resolution for better performance
FRAME_WIDTH = 320
FRAME_HEIGHT = 240
```

### Ball Detection Issues

#### Ball Not Detected
**Problem**: Green ball not being recognized

**Solutions:**
1. **Recalibrate HSV thresholds**:
   - Run calibration phase
   - Adjust trackbars for better color isolation
   - Save new threshold values

2. **Check lighting conditions**:
   - Ensure adequate lighting
   - Avoid shadows on the ball
   - Use consistent lighting

3. **Verify ball color**:
   - Use a vibrant green ball
   - Avoid reflective surfaces
   - Ensure ball is in contrast with background

#### Multiple Ball Detection
**Problem**: System detects multiple objects as balls

**Solutions:**
1. **Refine HSV ranges**:
   - Narrow the hue range
   - Increase minimum saturation
   - Adjust value thresholds

2. **Filter by size**:
   - Set appropriate MIN_BALL_RADIUS and MAX_BALL_RADIUS
   - Remove small noise objects

3. **Improve background**:
   - Use non-green background
   - Remove green objects from view

### Collision Detection Issues

#### False Collision Detection
**Problem**: System detects collisions when ball doesn't hit walls

**Solutions:**
1. **Adjust angle sensitivity**:
   ```python
   # In collision detection function
   angle_threshold = 30  # Increase for less sensitivity
   ```

2. **Increase minimum trajectory length**:
   ```python
   if len(all_centers) >= 5:  # Require more points
       hit_state = getAngle(all_centers, frame, i, height, hit_state)
   ```

3. **Calibrate grid zones accurately**:
   - Ensure grid covers exact playing area
   - Verify corner points are correct

#### Missing Collision Detection
**Problem**: Real collisions not detected

**Solutions:**
1. **Decrease angle threshold**
2. **Check ball trajectory smoothness**
3. **Verify grid zone positioning**
4. **Ensure adequate frame rate**

### Unity Integration Issues

#### No Data Received in Unity
**Problem**: Unity doesn't receive UDP data from Python

**Solutions:**
1. **Check port configuration**:
   - Verify both systems use port 5052
   - Ensure no port conflicts

2. **Firewall settings**:
   - Allow Python and Unity through Windows Firewall
   - Check antivirus software blocking

3. **Network connectivity**:
   ```bash
   # Test UDP connection
   telnet localhost 5052
   ```

4. **Verify script attachment**:
   - Ensure UDPReceive script is attached to GameObject
   - Check script is enabled and startReceiving is true

#### Data Corruption or Parsing Errors
**Problem**: Received data is incomplete or malformed

**Solutions:**
1. **Add data validation**:
   ```csharp
   if (!string.IsNullOrEmpty(data) && data.Contains(":"))
   {
       ProcessData(data);
   }
   ```

2. **Implement error handling**:
   ```csharp
   try
   {
       ProcessCollisionData(data);
   }
   catch (System.Exception e)
   {
       Debug.LogError("Data processing error: " + e.Message);
   }
   ```

### Performance Issues

#### High CPU Usage
**Problem**: System consuming too much CPU

**Solutions:**
1. **Optimize frame processing**:
   - Reduce frame resolution
   - Process every nth frame
   - Use ROI (Region of Interest)

2. **Reduce morphological operations**:
   ```python
   # Reduce iterations
   mask2 = cv2.erode(mask1, None, iterations=2)  # Was 4
   mask3 = cv2.dilate(mask2, None, iterations=3)  # Was 6
   ```

#### Memory Leaks
**Problem**: Memory usage increases over time

**Solutions:**
1. **Clear frame buffers**:
   ```python
   # Clear variables in main loop
   frame = None
   hsv = None
   mask = None
   ```

2. **Limit trajectory history**:
   ```python
   # Keep only recent centers
   if len(all_centers) > 10:
       all_centers = all_centers[-5:]
   ```

### Audio Issues

#### No Sound Effects
**Problem**: Collision sounds not playing

**Solutions:**
1. **Check audio file location**:
   - Ensure `hit1.wav` exists in correct directory
   - Use absolute path if necessary

2. **Audio system initialization**:
   ```python
   try:
       mixer.init()
       sound = mixer.Sound("assets/hit1.wav")
   except pygame.error as e:
       print(f"Audio error: {e}")
   ```

3. **System audio settings**:
   - Check system volume
   - Verify audio drivers

### Installation Issues

#### Missing Dependencies
**Problem**: Import errors for required packages

**Solutions:**
1. **Install missing packages**:
   ```bash
   pip install opencv-python imutils pygame pyautogui numpy
   ```

2. **Use virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Check Python version**:
   - Ensure Python 3.7+ is installed
   - Verify pip is up to date

#### OpenCV Installation Issues
**Problem**: OpenCV not working properly

**Solutions:**
1. **Reinstall OpenCV**:
   ```bash
   pip uninstall opencv-python
   pip install opencv-python
   ```

2. **Try different OpenCV version**:
   ```bash
   pip install opencv-python==4.5.5.64
   ```

## Debugging Tools

### Enable Debug Mode
Add debug flags to see detailed information:

```python
DEBUG_MODE = True

if DEBUG_MODE:
    print(f"Ball center: {center}")
    print(f"HSV thresholds: {greenLower} - {greenUpper}")
    print(f"Contour count: {len(cnts)}")
```

### Frame Analysis
Save frames for analysis:

```python
# Save problematic frames
cv2.imwrite(f"debug/frame_{timestamp}.png", frame)
cv2.imwrite(f"debug/mask_{timestamp}.png", mask)
```

### Performance Monitoring
Track system performance:

```python
import time

start_time = time.time()
# ... processing code ...
processing_time = time.time() - start_time
fps = 1.0 / processing_time
print(f"FPS: {fps:.2f}")
```

## Getting Help

If you continue to experience issues:

1. **Check system requirements**:
   - Windows 10/11
   - Python 3.7+
   - OpenCV 4.5+
   - USB camera or webcam

2. **Review configuration**:
   - Verify all config files
   - Check file paths
   - Validate parameter ranges

3. **Test components individually**:
   - Test camera capture alone
   - Test HSV filtering separately
   - Test Unity UDP receiver independently

4. **Create issue report** with:
   - System specifications
   - Error messages
   - Steps to reproduce
   - Screenshots or video

## Contact

For additional support, please create an issue in the GitHub repository with detailed information about your problem.