'''
https://www.codewars.com/kata/53c93982689f84e321000d62
'''
def getAllPrimeFactors(n):
  if isinstance(n, int) is False or n <= 0:
        return []
  elif n == 1:
      return [1]
  else:
      result = []
      divider = 2
      while n != 1:
          if n % divider == 0:
              result.append(divider)
              n = n/divider
          else:
              divider += 1
      return result

def getUniquePrimeFactorsWithCount(n):
  if isinstance(n, int) is False or n <= 0:
        return [[],[]]
  elif n == 1:
      return [[1],[1]]
  else:
      result = []
      result_count = {}
      divider = 2
      while n != 1:
          if n % divider == 0:
              result.append(divider)
              n = n/divider
          else:
              divider += 1
      for i in result:
          if i not in result_count:
              result_count[i] = 1
          else:
              result_count[i] += 1
      keys  = []
      values = []
      for key, value in result_count.items():
          keys.append(key)
          values.append(value)
      return [keys,values]

def getUniquePrimeFactorsWithProducts(n):
  if isinstance(n, int) is False or n <= 0:
        return []
  elif n == 1:
      return [1]
  else:
      result = []
      result_count = {}
      final_result = []
      divider = 2
      while n != 1:
          if n % divider == 0:
              result.append(divider)
              n = n/divider
          else:
              divider += 1
      for i in result:
          if i not in result_count:
              result_count[i] = 1
          else:
              result_count[i] += 1
      for key, value in result_count.items():
          final_result.append(key**value)
      return final_result
