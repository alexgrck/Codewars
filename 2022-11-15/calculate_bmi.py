def calculate_bmi(weight, height):
    """Return different string values depending on BMI value."""
    bmi = weight / (height ** 2)
    return ('Underweight' if bmi <= 18.5 else 'Normal' if bmi <= 25.0 else 
            'Overweight' if bmi <= 30.0 else "Obese")