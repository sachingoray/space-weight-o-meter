                        
                        ### WEIGHT CONVERTER BASED ON THE PLANET YOU  ARE ON!!
#                                              ^_^

                       ### AND SPECIFICALLY IT'S FORM OUR SOLAR SYSTEM

## SO FIRST ASKING THE USER FOR THE INPUT
print("********************************************************************************************************")
print("     ")
print ("                    Welcome to the Intergalactic Weight-o-Meter!")
print("              Where kilograms meet chaos and fun facts rule the galaxy!")
print("   ")
print("********************************************************************************************************")

## DECLEARING THE PLANTES AND THERI GRAVITY;
planet_gravity = {
 "sun":240,
 "mercury": 3.7,
 "venus": 8.87,
 "earth": 9.81,
 "mars": 3.71,
 "jupiter": 24.79,
 "saturn": 10.44,
 "uranus": 8.69,
 "neptune": 11.15
}

###Funny facts // messages from each planet
fun_facts ={
"sun" : " congratulations, you’re officially a human skyscraper! Just don’t try to sit down… or you’ll melt. 🔥😆",
"mercury":"I'm  is so light, even your problems would weigh less here! 😆",
"venus" : "On me, your weight is almost Earth-like… but the heat might melt your scales! 🔥",
"earth" : " The only planet where you can get pizza delivered 🍕.",
"mars" : "Not overweight! Just on the wrong planet 😉 I  make everyone look lighter.",
"jupiter" : "Careful! In here  you’re hitting PRs without lifting anything 💪.",
"saturn" : "My  rings are pretty, but they won’t help your waistline 😂.",
"uranus" : "Weighing in on Ur-anus  sounds funny already 🙃.",
"neptune" : "Well in here, you’re heavier, but hey, at least no one can see you through the storms 🌊.",
}

## NOW APPLYING THE CONDITON 
# condition for  program

## SO FIRST ASKING THE USER FOR THE INPUT
print("")
weight = float(input("Please enter your current weight in KG?? ::"))

while True:
	planet = input("Please enter the planet you want to be on? NOTE; its should be only our solar system planets ::")
	print("  ")
	print("!! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !")
	print("")


	if planet in planet_gravity:
		weight_in_netwon = weight * planet_gravity[planet]
		weight_kg_equivalent = weight_in_netwon / planet_gravity["earth"]
		print(f"on {planet.title()} ::  Your weight would be {weight_kg_equivalent:.2f}kg" )
		print(f"Message from {planet}:: {fun_facts[planet]}")
		break
	else:
		print("Invalid input:: Try planests from our solar system or sun")
		print("    ")
		print("********************************************************************************************************")
