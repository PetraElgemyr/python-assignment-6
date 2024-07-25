"""
Uppgift
Skapa ett program som läser in uppgifter om personer för att sedan skriva ut medelåldern för kvinnor och män.
"""


def main():

    isEnteringData = True
    numberOfMen = 0
    numberOfWomen = 0
    ageSumOfMen = 0
    ageSumOfWomen = 0

    while isEnteringData is True:
        category = getGenderStringFromUser()
        if category == "M":
            numberOfMen += 1
            age = getAgeFromUser()
            ageSumOfMen = ageSumOfMen + age
        elif category == "K":
            numberOfWomen += 1
            age = getAgeFromUser()
            ageSumOfWomen = ageSumOfWomen + age

        continueToEnterData = input(
            "Vill du fortsätta mata in data? Skriv stop för att avsluta eller tryck enter för att fortsätta: "
        ).upper()
        if continueToEnterData == "STOP":
            isEnteringData = False
        else:
            isEnteringData = True

    print(
        f"Medelåldern för män är: {int(ageSumOfMen/numberOfMen)} \nMedelåldern för kvinnor är: {int(ageSumOfWomen/numberOfWomen)}"
    )


def getGenderStringFromUser():
    isValidString = False
    while isValidString is False:
        category = ""
        category = input(
            "Vilket grupp tillhör personen? Skriv M för man eller K för kvinna och klicka på enter: "
        )
        category = category.upper().strip()
        isValidString = validateGenderString(category)
        if isValidString is True:
            return category


def validateGenderString(genderString):
    if genderString == "M" or genderString == "K":
        return True
    elif genderString == "":
        print(
            "Du måste ange en grupp, vänligen försök igen. Skriv M för man eller K för kvinna och klicka på enter:"
        )
        return False
    else:
        print(
            f"Det finns ingen grupp {genderString}, vänligen försök igen. Skriv M för man eller K för kvinna och klicka på enter:"
        )
        return False


def getAgeFromUser():
    isValidAge = False
    while isValidAge is False:
        age = input(
            "Hur många år är personen? Skriv åldern i heltal och klicka på enter: "
        )
        validAge = convertAgeStringToInt(age)
        if validAge is not None:
            isValidAge = True
            return validAge


def convertAgeStringToInt(age):
    try:
        return int(age)
    except ValueError:
        print("Felaktig ålder angiven. Försök igen. Obs! Skriv bara in heltal")
        return None


main()
