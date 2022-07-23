"""
What century is it?
20th"
21st"
22nd"
23rd"
12th"
20th"
# """

def what_century(year):
   year = str(int(year) // 100 + 1 if int(year) % 100 != 0 else int(year) // 100)
   if year[-1] == "1": suffix = "st"
   elif year[-1] =="2": suffix = "nd"
   elif year[-1] == "3": suffix = "rd"
   else:suffix = "th"
   if int(year) in range(11, 14): suffix = "th"
   return year+suffix


