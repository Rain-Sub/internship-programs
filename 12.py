import calendar

print(calendar.TextCalendar(firstweekday=6).formatyear(2015))
class TextCalendar:
    def __init__(self, firstweekday=0):
        self.firstweekday = firstweekday
    def formatyear(self, theyear, w=2, l=1, c=6):
        """return a years calendar in a multi-line string
        the arguments have the following meaning:
        theyear -the year to generate the calendar far
        w-width of date columns
        l-number of lines for eachweek
        c-number of spaces between month columns
        """
        s=""
        for i in range(1,13,3):
            s+=self.formatmonth(theyear,i,w,l).rstrip()
            s+=" "*c
            if i+1<=12:
                s+=self.formatmonth(theyear,i+1,w,l).rstrip()
            s+=" "*c
            if i+2<=12:
                s+=self.formatmonth(theyear,i+2,w,l).rstrip()
            s+="\n"

            return s