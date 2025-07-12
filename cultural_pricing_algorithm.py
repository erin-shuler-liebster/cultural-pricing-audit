
from typing import Dict
import numpy as np

class CulturalPricingTranslator:
    def __init__(self, cultural_profiles: Dict[str, Dict[str, float]]):
        self.country_profiles = cultural_profiles
        self.thresholds = {
            'low': 0.33,
            'medium': 0.67,
            'high': 1.0
        }

    def categorize_score(self, score: float) -> str:
        if score <= self.thresholds['low']:
            return 'low'
        elif score <= self.thresholds['medium']:
            return 'medium'
        else:
            return 'high'

    def cultural_logic_trace(self, dimension: str, value: float) -> str:
        category = self.categorize_score(value)
        logic = {
            'power_distance': {
                'low': "Flat pricing; peer justification",
                'medium': "Balanced pricing tiers",
                'high': "Hierarchical tiers; expert justification"
            },
            'individualism': {
                'low': "Collective framing; standard offers",
                'medium': "Moderate personalization",
                'high': "Highly personalized; autonomy"
            },
            'uncertainty_avoidance': {
                'low': "Minimal info display",
                'medium': "Transparent, but flexible",
                'high': "Highly transparent with guarantees"
            },
            'masculinity': {
                'low': "Care/empathy driven",
                'medium': "Balanced emotion and results",
                'high': "Competitive, performance-driven"
            },
            'long_term_orientation': {
                'low': "Immediate gratification",
                'medium': "Blend short- and long-term value",
                'high': "Deferred rewards, future benefits"
            },
            'indulgence': {
                'low': "Rational tone",
                'medium': "Balanced emotional messaging",
                'high': "Impulse/personal joy messaging"
            }
        }
        return logic[dimension][category]

    def translate(self, country: str) -> Dict[str, str]:
        profile = self.country_profiles[country]
        return {dim: self.cultural_logic_trace(dim, value) for dim, value in profile.items()}

    def explain_trace(self, country: str) -> Dict[str, str]:
        profile = self.country_profiles[country]
        trace = {}
        for dim, value in profile.items():
            category = self.categorize_score(value)
            explanation = self.cultural_logic_trace(dim, value)
            trace[dim] = f"{dim.title()} ({category}): {explanation}"
        return trace

    def assess_alignment(self, website_tags: Dict[str, str], country: str) -> Dict[str, str]:
        profile = self.country_profiles[country]
        feedback = {}
        for dim, value in profile.items():
            expected = self.cultural_logic_trace(dim, value).lower()
            actual = website_tags.get(dim, '').lower()
            if expected in actual:
                feedback[dim] = "✅ Matched expected cultural signal."
            else:
                feedback[dim] = f"⚠️ Expected: {expected} | Found: {actual or 'None'}"
        return feedback

    def recommend_improvements(self, website_tags: Dict[str, str], country: str) -> Dict[str, str]:
        profile = self.country_profiles[country]
        improvements = {}
        for dim, value in profile.items():
            expected = self.cultural_logic_trace(dim, value).lower()
            actual = website_tags.get(dim, '').lower()
            if expected not in actual:
                improvements[dim] = f"🔧 Improve by emphasizing: {expected}"
        return improvements
