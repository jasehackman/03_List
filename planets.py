planet_list = ["Mercury", "Mars"]

#1
planet_list.append("Jupiter")
planet_list.append("Saturn")

# print(planet_list)

#2
planet_list.extend(["Uranus", "Neptune"])
# print(planet_list)

#3
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")


#4
planet_list.append("Pluto")


#5
rocky_planets = planet_list[0:4]
# print(rocky_planets)

#6
del planet_list[8]
# print(planet_list)

#Challenge
#1
space = [("bob", "Earth"), ("greg", "Mars"), ("steve", "Neptune"), ("mike", "Earth"), ("blake", "Earth"), ("bill", "Mars")]

for planet in planet_list:
  space_craft = list()
  for craft in space:
    if planet in craft:
      space_craft.append(craft[0])
  if len(space_craft)==2:
    str = " and "
    print(f"{planet} was visited by {str.join(space_craft)}")
  if len(space_craft):
    str = ", "
    print(f"{planet} was visited by {str.join(space_craft)}")

