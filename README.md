# WSBTickerNews

This was an introductory project into webscraping. Nothing fancy but still usefull for me to understand the basics of webscraping.
This scrapper goes through the articles mentionning your favorite Ticker and return the **title**, the **link** (clickable in most recent terminals) and the **flair**.

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
Results
```
https://www.reddit.com/r/wallstreetbets/search?q=TSLA&restrict_sr=1&sort=new

Posts for TSLA
----
A summary of the GME meme machine
The link: https://www.reddit.com/r/wallstreetbets/comments/kkc0uq/a_summary_of_the_gme_meme_machine/
Discussion
----

----
$TSLA calls $100k
The link: https://www.reddit.com/r/wallstreetbets/comments/kkbxbq/tsla_calls_100k/
Gain
----

----
Just Turned 18 and can do options!!!
The link: https://www.reddit.com/r/wallstreetbets/comments/kk90t6/just_turned_18_and_can_do_options/
Fundamentals
----

----
GME mooning on Monday and Tuesday 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
The link: https://www.reddit.com/r/wallstreetbets/comments/kk75l4/gme_mooning_on_monday_and_tuesday/
Discussion
----

----
First yearly christmas gains/loss Post!
The link: https://www.reddit.com/r/wallstreetbets/comments/kk4y24/first_yearly_christmas_gainsloss_post/
Gain
----

----
Merry Christmas WSB - A quick look at this year's top 50 most mentioned tickers!
The link: https://www.reddit.com/r/wallstreetbets/comments/kk18dy/merry_christmas_wsb_a_quick_look_at_this_years/
Discussion
----
```
