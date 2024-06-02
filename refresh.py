import datetime
import locale
import os

import day_crawler
from mensa import Weekday

root_url = "https://moellh.com/mensakrabbler"

speisen_recommendation_dataframes = [day_crawler.crawl(weekday) for weekday in Weekday]

html_template = """
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="{styles}">
  <script src="{script}"></script>
  <title>Der Mensa Krabbler</title>
  <link rel="icon" href="{icon}">
</head>
<body>
  <header>
    <div class="brand">
        <span>
          <img src="{icon}">
        </span>
        <h1>Mensa Krabbler</h1>
      </div>    
      <nav>
        <ul class="nav_links">
          <li><a href="https://mensa.honestlyxm.com/9116" target="_blank" rel="noopener noreferrer">Reviews</a></li>
          <li><a>Über Uns</a></li>
        </ul>
      </nav>
      <a><button class="signInButton">Sign In</button></a>
  </header>
  <div id="button-frame">
    <button id="button1" class="weekday-button" onclick="showTable('monday'), activateButton(1)">Montag</button>
    <button id="button2" class="weekday-button" onclick="showTable('tuesday'), activateButton(2)">Dienstag</button>
    <button id="button3" class="weekday-button" onclick="showTable('wednesday'), activateButton(3)">Mittwoch</button>
    <button id="button4" class="weekday-button" onclick="showTable('thursday'), activateButton(4)">Donnerstag</button>
    <button id="button5" class="weekday-button" onclick="showTable('friday'),activateButton(5)">Freitag</button>
  </div>
  <div id="table-container">
    <div id="monday-table" class="hidden">{monday_html}</div>
    <div id="tuesday-table" class="hidden">{tuesday_html}</div>
    <div id="wednesday-table" class="hidden">{wednesday_html}</div>
    <div id="thursday-table" class="hidden">{thursday_html}</div>
    <div id="friday-table" class="hidden">{friday_html}</div>
  </div>
  <p id="output-text">{date_updated}</p>
</body>
</html>
"""

date = datetime.datetime.now().strftime("%Y-%m-%d")

# get the weekday name of the date in german
actual_location = locale.getlocale()
locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")
weekDayGerman = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")
locale.setlocale(locale.LC_TIME, actual_location)

# get the date in format: dd.mm.yyyy
dateForOutput = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d.%m.%Y")

# Ersetze die Platzhalter im HTML-Template mit den entsprechenden Tabelleninhalten
html_content = html_template.format(
    styles="styles/styles.css",
    script="scripts/script.js",
    icon="files/krebs.png",
    monday_html=speisen_recommendation_dataframes[Weekday.MONDAY.value].to_html(
        index=False
    ),
    tuesday_html=speisen_recommendation_dataframes[Weekday.TUESDAY.value].to_html(
        index=False
    ),
    wednesday_html=speisen_recommendation_dataframes[Weekday.WEDNESDAY.value].to_html(
        index=False
    ),
    thursday_html=speisen_recommendation_dataframes[Weekday.THURSDAY.value].to_html(
        index=False
    ),
    friday_html=speisen_recommendation_dataframes[Weekday.FRIDAY.value].to_html(
        index=False
    ),
    date_updated=("Zuletzt geupdatet am: " + weekDayGerman + ", " + dateForOutput),
)

with open("index.html", "w") as f:
    f.write(html_content)
