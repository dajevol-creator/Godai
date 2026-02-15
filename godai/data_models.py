# Data Structures for Civilizational Indicators

class CivilizationalIndicators:
    def __init__(self, population, gdp, life_expectancy, education_index, happiness_index):
        self.population = population  # Total population
        self.gdp = gdp  # Gross Domestic Product
        self.life_expectancy = life_expectancy  # Average life expectancy
        self.education_index = education_index  # Education index
        self.happiness_index = happiness_index  # Happiness index

    def __repr__(self):
        return (f"CivilizationalIndicators(population={self.population}, gdp={self.gdp}, "
               f"life_expectancy={self.life_expectancy}, education_index={self.education_index}, "
               f"happiness_index={self.happiness_index})")

# Example of instantiation:
# civ_indicator = CivilizationalIndicators(population=1000000, gdp=50000, life_expectancy=75, education_index=0.8, happiness_index=0.7)