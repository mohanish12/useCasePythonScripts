def lrgWrdDict(dict):
    keyLrgst = max(dict)
    dictLrgst = keyLrgst
    valueLargstInit = ""
    for key in dict:
        if isinstance(dict[key], list):
            valueLrgst = max(dict[key], key=len)
        else:
            valueLrgst = dict[key]

        if (len(valueLargstInit) < len(valueLrgst)):
            valueLargstInit = valueLrgst

    if (len(valueLargstInit) > len(keyLrgst)):
        dictLrgst = valueLargstInit

    print("The longest string in the dictionary is:" + " " + dictLrgst)


dict = {"Game": ["Mohanish Mahajan is a man on earth", "Armaan", "Aman"],
        "Age": "hum honge kamyab ek din pura hai vishwas",
        "Great Mohanish Mahajan is the man on earth that wants to see the movie": 'Indian'}

lrgWrdDict(dict)
