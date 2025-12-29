from cs50 import SQL
from csv import DictReader

db = SQL("sqlite:///data.db")

with open("static/colors.csv", "r") as csv:
    reader = DictReader(csv)
    for row in reader:
        db.execute("INSERT INTO colors (red, green, blue, name, officialnamed) VALUES(?, ?, ?, ?, 1)", row["red"], row["green"], row["blue"], row["color_name"])
