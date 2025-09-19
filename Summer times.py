months=["January","February","March","April","May","June",
"July","Augudst","September","October","November","December"]

seasons=["Winter","Spring",
"Summer","Autumn"]

current_month=int(input("What month is it (1-12)?"))
if current_month <= 2 or current_month == 12:
    season = 0
elif current_month <= 5:
    season = 1
elif current_month <= 8:
    season = 2
else:
    season = 3
print("It is ",seasons[season])