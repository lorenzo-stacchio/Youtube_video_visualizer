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
```
usage: yt_watcher.py [-h] [--youtube_url YOUTUBE_URL] [--views VIEWS] [--sound SOUND] [--language LANGUAGE]

options:
  -h, --help            show this help message and exit
  --youtube_url         Valid url to a youtube video.
  --views               Number of views to provide to the selected youtube video.
  --silent_mode         Use the driver in silent mode.
  --sound               Sound on if driver not in silent mode.
  --language            Language used in youtube, please refer to data/config_text_languages.json to check supported language or add by your own will.
  ```
  

Note that ```youtube_url``` must be a valid youtube video url as the [script default one](https://www.youtube.com/watch?v=BwWGZJeRVmU).

## TODO list:
- [x] Support italian youtube language
- [x] Params parsing
- [ ] Linux support and testing 
- [ ] Support english (and others) youtube languages