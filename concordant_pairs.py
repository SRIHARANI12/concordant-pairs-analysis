def analyze_concordant_pairs(times, risks):
    n = len(times)
    concordant = 0
    discordant = 0
    risk_ties = 0
    permissible = 0
    ties = 0

    for i in range(n):
        for j in range(i + 1, n):
            if times[i] != times[j]:
                permissible += 1
                if (times[i] < times[j] and risks[i] < risks[j]) or (times[i] > times[j] and risks[i] > risks[j]):
                    concordant += 1
                elif (times[i] < times[j] and risks[i] > risks[j]) or (times[i] > times[j] and risks[i] < risks[j]):
                    discordant += 1
                elif risks[i] == risks[j]:
                    risk_ties += 1
            else:
                ties += 1

    return concordant, discordant, risk_ties, permissible, ties


# ✅ Example Data
times = [1, 2, 3, 4]
risks = [4, 3, 2, 1]

# 🔍 Analyze
concordant, discordant, risk_ties, permissible, ties = analyze_concordant_pairs(times, risks)

# 📊 Output
print("Concordant Pairs:", concordant)
print("Discordant Pairs:", discordant)
print("Risk Ties:", risk_ties)
print("Permissible Pairs:", permissible)
print("Ties:", ties)
