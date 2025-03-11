import datetime

class Cal:
    
    def __init__(self):
        self.an = datetime.datetime.now().year
        self.mois = datetime.datetime.now().month
        self.semaine = "mon"
        
    def year(self, an=None):#défini l'année (valeur initiale si année pas donnée)
        if an:
            self.an = an
    
    def month(self, mois=None):#défini le mois (met l'actuel si rien est donné)
        if mois:
            dico_mois={"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, 
                      "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
            
            self.mois = dico_mois.get(mois)
    
    def week_start(self, start="mon"):#défini le jour de début de semaine(par défaut=lundi)
        
        self.semaine = start.lower() #.lower uniformise tout en minuscules pr éviter prblm avec majuscules

    def print(self): #print le calendrier
        first_day = datetime.date(self.an, self.mois, 1) #(année,mois,jour)
        # Get the number of days in the month
        next_month = self.mois % 12 + 1 # %12 permet de revenir à janvier si on est en décembre (12%12+1=1)
        last_day = (datetime.date(self.an, next_month, 1) - datetime.timedelta(days=1)).day #on soustrait 1j au premier jour du mois suivant pour revenir au dernier jour du mois présent
        
        # titre de la semaine
        if self.semaine == "sun":
            week_header = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
        else:
            week_header = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

        # titre du mois et année
        print(f"\n    {first_day.strftime('%B')} {self.an}")
        print(" ".join(week_header))
        
        # Find the weekday of the first day of the month
        start_day = first_day.weekday()  # Monday = 0, Sunday = 6
        
        # Adjust based on the `week_start` setting
        if self.semaine == "sun":
            start_day = (start_day + 1) % 7  # Make Sunday the first day of the week
        
        # Create a list of days for the calendar
        days = ["   "] * start_day  # Fill the first week with empty spaces
        
        for day in range(1, last_day + 1):
            days.append(f"{day:2} ")  # Add day to the calendar, formatted to 2 spaces
        
        # Split the days into weeks
        weeks = [days[i:i+7] for i in range(0, len(days), 7)]
        
        # Print each week
        for week in weeks:
            print("".join(week))

c = Cal()
c.year(2025)
c.month("aug")
c.print()