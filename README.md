# Youtube video visualizer

<p align="center">
  <img src="imgs/icon.png" alt="icon" width=300 height=200/>
</p>

Simple Python script based on selenium to augment views on a pre-defined youtube video. Is up to you the choice of implementing the dynamic change of your IP address or use the same at each iteration.


## Drivers

I will provide you a simple version of the Chrome Driver for windows (v. **ChromeDriver 99.0.4844.51**).

## Install

Create a virtual environment for python (or just use the global one) and install all the dependecies with:

```pip install -r requirements.txt```

## Usage

Until a more formal version of the script, you can change the variables in ```yt_watcher.py``` to change the video url to and the number of times you want this scripts sees it.
By default, the browser will be in silent mode, you can change it always from the same scripts. 


The url must be a valid youtube video as: ```https://www.youtube.com/watch?v=BwWGZJeRVmU```.

