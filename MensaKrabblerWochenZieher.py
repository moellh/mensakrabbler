import datetime
import locale
import os

import MensaKrabbler

speisen_recommendation_dataframes = [
    MensaKrabbler.run(weekday) for weekday in MensaKrabbler.Weekday.weekdays
]

# Exportiere die DataFrames als separate HTML-Dateien
speisen_recommendation_dataframes[0].to_html(
    "Website/monday_table.html", index=False
)
speisen_recommendation_dataframes[1].to_html(
    "Website/tuesday_table.html", index=False
)
speisen_recommendation_dataframes[2].to_html(
    "Website/wednesday_table.html", index=False
)
speisen_recommendation_dataframes[3].to_html(
    "Website/thursday_table.html", index=False
)
speisen_recommendation_dataframes[4].to_html(
    "Website/friday_table.html", index=False
)

# Lies den Inhalt der HTML-Dateien ein
with open("Website/monday_table.html", "r") as f:
    monday_html = f.read()
with open("Website/tuesday_table.html", "r") as f:
    tuesday_html = f.read()
with open("Website/wednesday_table.html", "r") as f:
    wednesday_html = f.read()
with open("Website/thursday_table.html", "r") as f:
    thursday_html = f.read()
with open("Website/friday_table.html", "r") as f:
    friday_html = f.read()

# Erzeuge den HTML-Code für die kombinierte Seite mit Button-Auswahl
html_template = ""
with open("./template.html", "r") as file:
    html_template = file.read()

date = datetime.datetime.now().strftime("%Y-%m-%d")

# get the weekday name of the date in german
actual_location = locale.getlocale()
locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")
weekDayGerman = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")
locale.setlocale(locale.LC_TIME, actual_location)

# get the date in format: dd.mm.yyyy
dateForOutput = datetime.datetime.strptime(date, "%Y-%m-%d").strftime(
    "%d.%m.%Y"
)

# Ersetze die Platzhalter im HTML-Template mit den entsprechenden Tabelleninhalten
html_content = html_template.format(
    monday_html=monday_html,
    tuesday_html=tuesday_html,
    wednesday_html=wednesday_html,
    thursday_html=thursday_html,
    friday_html=friday_html,
    date_updated=("Letztes Update am " + weekDayGerman + ", " + dateForOutput),
)

# Speichere den kombinierten HTML-Code in einer Datei
with open("index.html", "w") as f:
    f.write(html_content)

# Commit to git history
os.system("git add index.html")
os.system(
    'git commit -m "Update index.html{}"'.format(
        datetime.datetime.now().strftime(" %Y-%m-%d %H:%M:%S")
    )
)

os.system("cp ./index.html /var/www/html/mensakrabbler/index.html")
