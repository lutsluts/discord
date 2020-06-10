# see on dcity 2nd edition kaartide müügiks
# suhteliselt kasutu asi tegelt aga mõne sekundi äkki hoiad kokku
# script küsib sult iga kaardi kohta, mis hinnaga sa neid müüa tahad
# prindib sulle terve lause mida saad CityHelper discordis kasutada
# idk dont blame me lol

cards = ("farm park wind-turbine hospital hotel job-center stadium casino art-gallery ad-agency school research-center university brewery WEED-farm night-club waves-broadcast-tower laboratory forest solar-plant nuclear-plant military-industrial-complex public-restrooms law-firm social-aid-office")
cardsSplit = cards.split()

for i in range(24):
   print("Mis hinda soovid kaardile: " + cardsSplit[i])
   hind = input()
   print("!sell 999 " + cardsSplit[i] + " " + hind + " " + "sim")
   print(" ")
   print(" ")
   i += 1
