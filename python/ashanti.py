import datetime


def findDay(date):
    """
    input date string in format dd/mm/yyyy
    output day string

    Examples:
    input 06/08/1997
    output Wednesday
    """
    day, month, year = (int(i) for i in date.split("/"))
    birth_date = datetime.date(year, month, day)
    return birth_date.strftime("%A")


ashanti_names = {
    "Sunday": ["Akosua", "Kwasi"],
    "Monday": ["Adwoa", "Kadjo"],
    "Tuesday": ["Abeena", "Kwabena"],
    "Wednesday": ["Akwa", "Kwaku"],
    "Thursday": ["Yaa", "Yaw"],
    "Friday": ["Afia", "Kofi"],
    "Saturday": ["Amma", "Kwame"],
}

# group_members = {
#     "Adama": {"birth_date": "06/08/1998", "gender": "female"},
#     "Bello": {"birth_date": "06/07/2000", "gender": "male"},
#     "Lina": {"birth_date": "20/11/2021", "gender": "female"},
#     "Latif": {"birth_date": "22/10/2021", "gender": "male"},
# }


def get_name(day, gender):
    if gender.lower() == "female":
        return ashanti_names[day][0]
    elif gender.lower() == "male":
        return ashanti_names[day][1]


print(
    "If you join the Ashanti tribe you get a new name. Follow the prompts below to get a new name...\n"
)

# for key, value in group_members.items():
#     birth_day = findDay(value["birth_date"])
#     name = get_name(birth_day, value["gender"])
#     print("{0}'s Ashanti name is {1}".format(key, name))

birth = input("Enter your birthday in this format: dd/mm/yyyy: ")
birth_day = findDay(birth)
name = input("Enter your name: ")
gender = input("Enter your gender: ")
gettingName = get_name(birth_day, gender)
print("{0}'s Ashanti name is {1}".format(name, gettingName))
