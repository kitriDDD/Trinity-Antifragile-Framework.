import numpy as np

def calculate_trinity_score(survival, growth, foresight):
    # Trinity Synergy: 15% Bonus for integrating all pillars
    base_score = (survival + growth + foresight) / 3
    return base_score * 1.15 

print("Trinity Antifragile Engine Loaded.")
print(f"Final Synergy Score: {calculate_trinity_score(100, 12, 40):.2f}%")
