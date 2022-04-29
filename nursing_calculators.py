def bmi(height, weight):
  """Returns the BMI of a client with the given values.
  Formula used is: BMI = (weight * 703) / height ^2  """
  return round(((weight * 703) / height**2), 1)
