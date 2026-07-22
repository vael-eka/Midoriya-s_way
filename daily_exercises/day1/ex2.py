"""
Write a function called analyze_hero that takes three things:

    hero_name (a string)

    quirk_power (an integer)

    stamina (an integer)

The Requirements:

    Calculate a total_combat_score by adding quirk_power and stamina.

    Use Python's f-strings to format a clean text card.

    Add a simple if/else condition:

        If total_combat_score is greater than or equal to 150, set status to "Pro Hero".

        Otherwise, set status to "Student Trainee".
"""


def analyze_hero(hero_name, quirk_power, stamina):
    total_combat_score = quirk_power + stamina

    if total_combat_score >= 150:
        status = "Hero"
    else:
        status = "Trainee"

    return {
        "Hero": hero_name,
        "Score": total_combat_score,
        "Rank": status
    }


result1 = analyze_hero("Deku", 95, 60)
print(result1)
