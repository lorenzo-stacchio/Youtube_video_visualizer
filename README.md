# Youtube video visualizer
<p align="right">
  <img src="https://img.shields.io/badge/Python-FFD43B?logo=python&logoColor=blu"/>
  <img src="https://img.shields.io/badge/Selenium-43B02A?logo=Selenium&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google_chrome-4285F4?logo=Google-chrome&logoColor=white"/>
  <img src="https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white"/>
<img src="https://visitor-badge.laobi.icu/badge?page_id=lorenzo-stacchio.Youtube_video_visualizer" alt="visitors">
</p>

<p align="center">
  <img src="imgs/icon.png" alt="icon" width=300 height=200/>
</p>

Simple Python script based on [Selenium](https://www.selenium.dev/) to increase views on a pre-defined youtube video. Is
up to you the choice of implementing a dynamic change IP address feature or use your default one.

## Drivers

I will provide you a simple version of the Chrome Driver for Windows ([v. **ChromeDriver
99.0.4844.51**](https://chromedriver.storage.googleapis.com/index.html?path=99.0.4844.51/)). You can change it
accordingly to your Google Chrome version, you can find the version for
you [here](https://chromedriver.chromium.org/downloads). You should replace the driver binaries in
the ```drivers/``` folder.

## Install

Create a virtual environment for python (or just use the global one) and install all the dependencies with:

```pip install -r requirements.txt```

## Usage

```
usage: yt_watcher.py [-h] [--youtube_url YOUTUBE_URL] [--views VIEWS] [--sound SOUND] [--language LANGUAGE]

options:
  -h, --help            show this help message and exit
  --youtube_url         Valid url to a youtube video.
  --views               Number of views to provide to the selected youtube video.
  --watch_full          If used, the video will be watched entirely (recommended for short videos).
  --chrome_driver_path  Path to the chrome driver to use.
  --silent_mode         Use the driver in silent mode.
  --sound               Sound on if driver not in silent mode.
  --language            Language used in youtube, please refer to data/config_text_languages.json to check supported language or add by your own will.
  ```

Note that ```youtube_url``` must be a valid youtube video url as
the [script default one](https://www.youtube.com/watch?v=BwWGZJeRVmU).

## TODO list:

- [x] Support italian youtube language
- [x] Params parsing
- [ ] Support Ubuntu distribution (to be tested)
- [x] Support other youtube languages (tested on all countries reported in ```data/config_text_languages.json```)
- [x] Provide the chance to watch a video just for the time needed to count a visualization; 
