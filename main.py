person = {
"name" : "sherifa",
"age" : 18,
"hobbies" : ["swimming", "reading"]
}




print(person['name'])
print(person['age'])
person["age"] = 23
person["country"] = "kuwait"
print(person)
print(f"number of objects in dictionary: {len((person))}")
person["hobbies"].append("codeing")
def check_hobbies(person) :
    if len(person["hobbies"]) >= 3 :
        return print("wow you are amazing")
    else :
        return print("keep exploring your hobbies")
    
check_hobbies(person)