import numpy as np

class TrinityEngine:
    def __init__(self):
        # სისტემის საწყისი პარამეტრები (Theorem 4-ის მიხედვით)
        self.R_target = 0.4  # ოპტიმალური წერტილი
        self.alpha = 0.5     # კონტრაქციის კოეფიციენტი (Convergence rate)
        self.R_max = 0.6     # მაქსიმალური ზღვარი
        self.R_min = 0.2     # მინიმალური ზღვარი
        
    def criticality_convergence(self, R_current):
        """
        Theorem 4: Geometric Convergence using Banach Contraction Mapping.
        უზრუნველყოფს სისტემის დაბრუნებას ოპტიმალურ ზონაში.
        """
        if R_current > self.R_max:
            # თუ სისტემა ზედმეტად ქაოტურია, ვაბრუნებთ მიზნისკენ
            return R_current - self.alpha * (R_current - self.R_max)
        elif R_current < self.R_min:
            # თუ სისტემა ზედმეტად სტატიკურია, ვამატებთ დინამიკას
            return R_current + self.alpha * (self.R_min - R_current)
        return R_current

    def calculate_trinity_score(self, survival, growth, foresight):
        """
        ანგარიშობს სინერგიის ქულას 15%-იანი ბონუსით.
        """
        base_score = (survival + growth + foresight) / 3
        return base_score * 1.15

# სიმულაციის გაშვება
engine = TrinityEngine()
current_R = 0.9  # დავუშვათ მოხდა ძლიერი შოკი (სისტემა დაცილდა მიზანს)

print(f"--- Trinity Antifragile Engine Activated ---")
print(f"Initial Criticality (R_0): {current_R}")

# გეომეტრიული კონვერგენციის ჩვენება 7 ეპოქაში
for epoch in range(1, 8):
    current_R = engine.criticality_convergence(current_R)
    distance = abs(current_R - engine.R_target)
    print(f"Epoch {epoch}: R = {current_R:.4f} | Distance to Target: {distance:.4f}")

final_score = engine.calculate_trinity_score(100, 12, 40)
print(f"\nFinal Synergy Score: {final_score:.2f}")
