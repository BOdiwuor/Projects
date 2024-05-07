zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

#print(zodiac_elements["energy"])

#Add the key "energy" to the zodiac_elements. It should map to a value of "Not a Zodiac element". Run the code. Since "energy" is now a key, its value prints to the terminal!
#.update is also used to add multiple keys

zodiac_elements.update({"energy": "Not a Zodiac element"}) 
  
print(zodiac_elements)

if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])

#How to get a key

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])

print(zodiac_elements["fire"])

#How to safely get a key

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)

print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)

print(stack_id)

#How to delete a key

#How to get all values in a dictionary

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

#Iterate through the values in the num_exercises dictionary and add each value to the total_exercises variable.
for exercise in num_exercises.values():
  total_exercises += exercise

print(total_exercises)

#How to get both keys and values

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

#Use a for loop to iterate through the items of pct_women_in_occupation. 
for occupation, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " "  "percent of" + " "+ occupation +"s.")


tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	
         "The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	
         "Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

tarot.pop(13)

spread.update({"past": "Death"})

tarot.pop(22)

spread.update({"present": "The Fool"})

tarot.pop(10)

spread.update({"future": "Wheel of Fortune"})


for key, value in spread.items():
  print("Your" + " " + key + " " "is the" + " " + str(value) + " " "card.")




