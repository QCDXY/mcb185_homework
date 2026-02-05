import random

def deathSaveTrial():
    failures = 0
    successes = 0

    while True:
        roll = random.randint(1, 20)

        if roll == 1:
            failures += 2
        elif roll < 10:
            failures += 1
        elif roll < 20:
            successes += 1
        else:
            return "revive"

        if failures >= 3:
            return "die"
        if successes >= 3:
            return "stable"


def simulate(trials):
    die = 0
    revive = 0
    stable = 0 

    for i in range(trials):
        outcome = deathSaveTrial()
        if outcome == "die":
            die += 1
        elif outcome == "stable":
            stable += 1
        elif outcome == "revive":
            revive += 1 
        i += 1

    die_prob = die / trials
    revive_prob = revive / trials
    stable_prob = stable / trials

    return f"Probobility of die:{die_prob}\nProbobility of Revive:{revive_prob}\nProbobility of Stable:{stable_prob}"


print(simulate(1000000))


