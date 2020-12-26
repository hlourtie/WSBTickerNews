# WSBTickerNews

This was an introductory project into webscraping. Nothing fancy but still usefull for me.

### Requirements

Only requirements are that you have [Selenium](https://selenium-python.readthedocs.io/ "Selenium package") package installed.
```python
pip3 install selenium
```
and that you have [chromium driver](https://chromedriver.chromium.org/downloads "Chromium DownLoad") installed in your 
```
/usr/local/bin/
```
If it is somewhere else just modify the path in the code

### Usage

Launch the program with Python and with a list of tickers for whom you'd want to see the new reddit posts from WSB

example:
```
python3.8 WSBscrapper.py TSLA PTON
```
