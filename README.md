# Xvideos - lightweight video stream reading

Xvideos is a lightweight single class library for background video reading. The ```VideoReader``` class works in 2 threads,
which allows you to efficiently read the video with its parallel processing.

## Install

You can use the Pip package manager to install the package:
```
pip install xvideos
```

Or you can install manually:
```
git clone https://github.com/tam2511/xvideos.git
cd xvideos
python setup.py install
```

## Documentation

This library consists of a single VideoReader class and several helper functions.
Their signature and description can be found in the [documentation](https://xvideos.readthedocs.io/en/latest/#)


## Examples

The ```VideoReader``` class is very easy to use, just pass the source of the video stream to the class constructor 
and then use the ```get()``` method to get frames until the video stream ends

```python
from xvideos import VideoReader

reader = VideoReader(source='./test.mp4')

while True:
    flag, batch = reader.get()
    if not flag:
        break
    ... # do something

```
