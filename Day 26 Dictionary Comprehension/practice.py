numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:



#Write your code 👆 above:
result = [n for n in numbers if n%2==0]
print(result)


###########################################
#Dictionary Comprehension

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day:(temp*9/5+32) for (day,temp) in weather_c.items()}


print(weather_f)


