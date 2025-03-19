  import random
  
  def get_random_math_problem():
      operands = [10, 20, 30, 40, 50]
      operator = ['+', '-', '*', '/']
      problem = ""
      
      for i in range(3):
          problem += str(operands[random.randint(0, len(operands) - 1)])
          problem += operator[random.randint(0, len(operator) - 1)]
      
      problem = problem[:-1] + '=' + str(eval(problem))
      
      return problem