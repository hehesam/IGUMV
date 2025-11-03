# Unity Integration Guide

This directory contains the Unity integration components for the IGUMV exergame system.

## Setup Instructions

### 1. Unity Project Setup

1. **Create or open your Unity project** (Unity 2019.4 or later recommended)

2. **Import the UDP script**:
   - Copy `UDPReceive.cs` to your Unity project's `Assets/Scripts/` folder
   - If the Scripts folder doesn't exist, create it

### 2. GameObject Configuration

1. **Create an empty GameObject**:
   - Right-click in the Hierarchy
   - Select "Create Empty"
   - Rename it to "UDPReceiver"

2. **Attach the script**:
   - Select the UDPReceiver GameObject
   - In the Inspector, click "Add Component"
   - Search for "UDPReceive" and add it

### 3. Script Configuration

Configure the UDPReceive component parameters:

- **Port**: `5052` (default, should match Python configuration)
- **Start Receiving**: `true` (enable UDP reception)
- **Print To Console**: `true` (for debugging, disable in production)

### 4. Integration with Game Logic

Create a game controller script to handle received data:

```csharp
using UnityEngine;

public class ExergameController : MonoBehaviour
{
    public UDPReceive udpReceive;
    
    void Start()
    {
        // Initialize game state
    }
    
    void Update()
    {
        // Check for new collision data
        string data = udpReceive.data;
        if (!string.IsNullOrEmpty(data))
        {
            ProcessCollisionData(data);
        }
    }
    
    void ProcessCollisionData(string data)
    {
        // Parse and handle collision events
        // Example: trigger effects, update score, etc.
        Debug.Log("Collision detected: " + data);
    }
}
```

## Data Format

The Python ball tracker sends data in the following formats:

### Collision Event
```
collision:zone:angle
```
Example: `collision:5:45.2`

### Ball Position
```
position:x:y
```
Example: `position:320:240`

## Troubleshooting

### Common Issues

1. **No data received**:
   - Check that port 5052 is not blocked by firewall
   - Verify both Python and Unity are using the same port
   - Ensure Python ball tracker is running

2. **Connection errors**:
   - Try restarting both applications
   - Check Windows firewall settings
   - Verify localhost connectivity

3. **Performance issues**:
   - Reduce UDP data frequency in Python
   - Optimize data parsing in Unity
   - Consider using background threading

### Debug Mode

Enable console output to monitor incoming data:
- Set "Print To Console" to `true` in the UDPReceive component
- Check the Unity Console window for incoming messages

## Advanced Usage

### Custom Data Parsing

Extend the UDPReceive script for custom data formats:

```csharp
public class CustomUDPReceive : UDPReceive
{
    public UnityEvent<CollisionData> OnCollisionReceived;
    
    protected override void ProcessReceivedData(string data)
    {
        // Parse custom data format
        CollisionData collision = ParseCollisionData(data);
        OnCollisionReceived.Invoke(collision);
    }
}
```

### Multi-threaded Processing

For high-frequency data, consider using Unity's Job System:

```csharp
using Unity.Collections;
using Unity.Jobs;

public struct DataProcessingJob : IJob
{
    public NativeArray<float> inputData;
    public NativeArray<float> results;
    
    public void Execute()
    {
        // Process collision data in background
    }
}
```

## Performance Optimization

1. **Reduce Update Frequency**: Process UDP data every few frames instead of every frame
2. **Use Object Pooling**: Reuse GameObjects for visual effects
3. **Optimize String Operations**: Cache parsed data to avoid repeated string processing

## Network Security

- The UDP receiver only accepts local connections
- No external network access is required
- Consider adding data validation for production use 