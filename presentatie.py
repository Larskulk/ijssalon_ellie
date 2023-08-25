mijn_dict = {'vis': 10, 'vlees': 25, 'overig': 15}

def presenteer(dictionary, totaal):
    for key, value in dictionary.items():
        print(key, ":", value)
    print("========================")
    print(f"totaal:", totaal)



