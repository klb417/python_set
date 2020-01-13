showroom = set()

showroom.update(["Thunderbird", "Mustang", "Civic", "Escape"])

print(len(showroom))

showroom.add("Mustang")

print(showroom)

showroom.update(["Sedona", "Escort"])

print(showroom)

showroom.discard("Mustang")

print(showroom)
