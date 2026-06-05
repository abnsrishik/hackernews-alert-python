# Hacker News Top Story Alert

A Python automation that scrapes Hacker News, finds the most upvoted article, and emails it to you — so you never miss what the tech community is talking about.

## How It Works

1. Scrapes the Hacker News front page using BeautifulSoup
2. Extracts all article titles, links, and upvote scores
3. Finds the article with the highest upvotes
4. Sends it to your email with title, link, and upvote count

## Example Email

```
Subject: Show HN: I built a tool that does X

Current Most Upvoted News is https://github.com/user/project
Upvotes: 847
Source: Hacker News
```

## Features

- **Live scraping** — fetches real-time data from Hacker News front page
- **Smart selection** — automatically finds highest upvoted article
- **Email delivery** — sends directly to your inbox via Gmail SMTP
- **Fully secure** — credentials stored in environment variables

## How to Run

```bash
git clone https://github.com/abnsrishik/hackernews-alert-python
cd hackernews-alert-python
pip install requests beautifulsoup4
python main.py
```

## Setup

Set environment variables:

```bash
export MY_EMAIL="your@gmail.com"
export MY_PASS="your_gmail_app_password"
export TO_EMAIL="recipient@gmail.com"
```

> Gmail requires an App Password. Get one at: https://myaccount.google.com/apppasswords

## Automate with GitHub Actions

Get the top story every morning. Save as `.github/workflows/hn_alert.yml`:

```yaml
name: Hacker News Alert
on:
  schedule:
    - cron: '30 2 * * *'  # 2:30 AM UTC = 8:00 AM IST
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - run: pip install requests beautifulsoup4
      - run: python main.py
        env:
          MY_EMAIL: ${{ secrets.MY_EMAIL }}
          MY_PASS: ${{ secrets.MY_PASS }}
          TO_EMAIL: ${{ secrets.TO_EMAIL }}
```

## Requirements

- Python 3.x
- requests (`pip install requests`)
- beautifulsoup4 (`pip install beautifulsoup4`)
- smtplib (built-in)

## What I Learned

- Web scraping with BeautifulSoup — find_all, class selectors, tag navigation
- Extracting href attributes from anchor tags
- List comprehension with string parsing for upvote scores
- Finding max value index across a list
- Gmail SMTP with TLS for sending emails
