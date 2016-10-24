#![Simplistic I/O Services](https://s3-eu-west-1.amazonaws.com/thomasjsn/public/github/sios/sios.png)

The goal is to make it easier to write Python scripts to read, process and act on sensor data.

# Requirements
* Linux environment (like a RaspBerry Pi)
* Python3

# Examples
## Read sensor data from Arduino

```python
import sios

arduino = sios.Serial('/dev/ttyACM0', 9600)
temperature = sios.Measurement()

while True:
    response = arduino.send('get')

    if not response:
        continue

    gas.add(response)   # add recevied sensor value to measurement
    print(gas.get(3))   # print mean for last three points
    print(gas.mean)     # print mean for all points (300 by default)
    print(gas.stdev)    # print standard deviation for all points
    print(gas.length)   # print the number of points
    if gas.rising:      # if current measurement is outside the normal distribution (3 sigma)
        print('Rising!!')

    time.sleep(1)
```
