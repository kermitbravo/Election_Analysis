counties = ["Arapahoe", "Denver", "Jefferson"]

# total_votes = 500
# my_votes = int(input("Type an amount "))
# percentage_votes = int(my_votes / total_votes * 100)
# print(f"The percentage of votes is {percentage_votes}%")
# 20

# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print("Your grade is an A.")
# else:
#     if score >= 80:
#         print("Your grade is a B.")
#     else:
#         if score >= 70:
#             print("Your grade is a C.")
#         else:
#             if score >= 60:
#                 print("Your grade is a D.")
#             else:
#                 print("Your grade is an F.")

# # What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print("Your grade is an A.")
# elif score >= 80:
#     print("Your grade is a B.")
# elif score >= 70:
#     print("Your grade is a C.")
# elif score >= 60:
#     print("Your grade is a D.")
# else:
#     print("Your grade is an F.")

# counties = ["Arapahoe", "Denver", "Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# for county in counties:
#     print(county)

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)

# for num in range(15):
#     print(num)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_tuple:
#       print(county)

# for i in range(len(counties)):
#     print(counties[i])

# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for key, value in counties_dict.items():
#     print(key, value)

# for county, voters in counties_dict.items():
#     print(county, voters)

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters")

# voting_data = [
#     {"county": "Arapahoe", "registered_voters": 422829},
#     {"county": "Denver", "registered_voters": 463353},
#     {"county": "Jefferson", "registered_voters": 432438},
# ]

# for county in range(len(voting_data)):

#     print(voting_data[county]["county"])


# for county_dict in voting_data:

#     print(county_dict["registered_voters"])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes."
# )

# print(message_to_candidate)

# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes."
# )

# print(message_to_candidate)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters")


# voting_data = [
#     {"county": "Arapahoe", "registered_voters": 422829},
#     {"county": "Denver", "registered_voters": 463353},
#     {"county": "Jefferson", "registered_voters": 432438},
# ]

# for county_dict in voting_data:
#     print(
#         f'{county_dict["county"]} county has {county_dict["registered_voters"]:,} registered voters'
#     )

# for county_dict in voting_data:

#     print(county_dict["registered_voters"])