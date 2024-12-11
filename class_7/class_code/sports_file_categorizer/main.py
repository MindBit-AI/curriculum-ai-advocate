from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import List

class SportsFileCategorizer:
    CATEGORIES = [
        "PLAYER_STATS",          # Individual player performance statistics
        "GAME_RESULTS",          # Match/game outcomes and team performance
        "SCOUTING_REPORTS",      # Player evaluation and recruitment data
        "TICKET_SALES",          # Ticketing and attendance data
        "FAN_ENGAGEMENT",        # Fan interaction and social media metrics
        "TEAM_ROSTERS",          # Team composition and player details
        "VENUE_OPERATIONS",      # Stadium/arena operations and logistics
        "MERCHANDISE_SALES",     # Retail and merchandise transaction data
        "SPONSORSHIP_DEALS",     # Sponsorship and partnership information
        "PERFORMANCE_ANALYTICS"   # Advanced metrics and analysis data
    ]

    def __init__(self):
        self.llm = ChatOpenAI(
            # model="gpt-4o-mini",
            model="ft:gpt-4o-mini-2024-07-18:mindbit:sports-file-categorization:Ac34PhnQ",
            temperature=0
        )
        
        template = """Given these CSV column headers: {headers}

Available categories are: {categories}

Analyze the headers and determine which category this file belongs to. Consider:
- PLAYER_STATS: Individual statistics like points, assists, goals, batting averages, etc.
- GAME_RESULTS: Match scores, team statistics, venue details, weather conditions
- SCOUTING_REPORTS: Player evaluations, potential ratings, physical measurements
- TICKET_SALES: Ticket transactions, seat locations, pricing tiers, event details
- FAN_ENGAGEMENT: Social media metrics, app usage, fan club membership
- TEAM_ROSTERS: Player biographical info, contracts, positions, jersey numbers
- VENUE_OPERATIONS: Facility management, staffing, equipment inventory
- MERCHANDISE_SALES: Product sales, inventory levels, customer purchases
- SPONSORSHIP_DEALS: Partner details, contract values, activation metrics
- PERFORMANCE_ANALYTICS: Advanced metrics, predictive models, player tracking

Respond with only the category name, nothing else."""

        self.prompt = ChatPromptTemplate.from_template(template)
        self.output_parser = StrOutputParser()
        self.chain = self.prompt | self.llm | self.output_parser

    def categorize_headers(self, headers: str) -> str:
        """Categorize CSV headers into predefined sports analytics categories."""
        
        category = self.chain.invoke({
            "headers": headers,
            "categories": ", ".join(self.CATEGORIES)
        })
        
        category = category.strip()
        if category not in self.CATEGORIES:
            raise ValueError(f"Invalid category returned: {category}")
        
        return category

# Example usage
if __name__ == "__main__":
    
    # Ambiguous examples that could be either PLAYER_STATS or PERFORMANCE_ANALYTICS
    ambiguous_headers = [
        "player_name, xG_per_90, shot_quality_rating, expected_assists, pressure_regains, progressive_passes", # PERFORMANCE_ANALYTICS
        "player_id, points_per_possession, true_shooting_percentage, defensive_box_plus_minus, vorp, win_shares", # PERFORMANCE_ANALYTICS
        "athlete_name, sprint_speed, acceleration_g_force, heart_rate_variability, power_output, fatigue_index", # PERFORMANCE_ANALYTICS
        "player_name, distance_covered_km, high_intensity_runs, metabolic_power, pass_completion_under_pressure", # PERFORMANCE_ANALYTICS
        "player_id, traditional_stats, advanced_metrics, raw_stats, calculated_indices, performance_scores" # PLAYER_STATS
    ]
    
    categorizer = SportsFileCategorizer()
    
    print("\nTesting ambiguous headers between PLAYER_STATS and PERFORMANCE_ANALYTICS:")
    for headers in ambiguous_headers:
        category = categorizer.categorize_headers(headers)
        print(f"\nHeaders: {headers}")
        print(f"Categorized as: {category}") 