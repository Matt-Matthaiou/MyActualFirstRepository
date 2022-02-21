enemyName = "orc warrior"
hp = 30
attackDamage = 10.5
ranged = False

print("An", enemyName.capitalize(), "appeared!")

remainingHP = hp - attackDamage

print("The", enemyName.capitalize(), "deals", attackDamage, "points of damage to you with his hammer.")
print("your remaining health is now:", remainingHP)
