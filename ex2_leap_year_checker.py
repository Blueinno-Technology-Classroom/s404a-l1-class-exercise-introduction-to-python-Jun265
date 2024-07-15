Year = int(input ("Tell me what year"))
if Year% 400==0:
    print("This year is a leep year")
elif Year% 4==0 and Year% 100!=0:
    print("This year is a leep year")
else:   
    print("this year is not a leep year")