#Linkdean Practice code calander




import calendar

#ef main():

#    c = calendar.TextCalendar(calendar.SUNDAY)
#    st = c.formatmonth(2017,1,0,0)
#    print(st)

  
#if __name__ == "__main__":
#    main()
   
# calendar using HTML    


#def main():
   # print("Team meetings will be on: ")
    #for m in range(1,13):
    #    cal = calendar.monthcalendar(2018,m)
    #    weekone=cal[0]
    #    weektwo=cal[1]

    #    if weekone[calendar.FRIDAY] != 0: 
    #        meetday = weekone[calendar.FRIDAY]
    #    else: 
    #        meetday = weektwo[calendar.FRIDAY]
    #    print(calendar.month_name[m], meetday)


#if __name__ == "__main__":
#    main()


from datetime import date

def main():

    today=date.today()
    days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    print("Tomorrow will be "+days[(today.weekday()+1)%7])




if __name__ == "__main__":
    main()  
