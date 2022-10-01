# balanced brackets '{[()]}' using recursive function

def recursive_solution(params):
    arr = params[0]
    c = params[1]
    lau = params[2] # worthless
    # print(lau)
    # print(arr, c)
    if c == 'sarapateu': # worthless
      return [params, c]
    else:
      try:
        if arr[c] == '{':
          if arr[c + 1] == '}':
            arr.pop(c)
            arr.pop(c)
            c = 0
            return recursive_solution([arr, c, lau])
          else:
            c += 1
            return recursive_solution([arr, c, lau])
        if arr[c] == '[':
          if arr[c + 1] == ']':
            arr.pop(c)
            arr.pop(c)
            c = 0
            return recursive_solution([arr, c, lau])
          else:
            c += 1
            return recursive_solution([arr, c, lau])
        if arr[c] == '(':
          if arr[c + 1] == ')':
            arr.pop(c)
            arr.pop(c)
            c = 0
            return recursive_solution([arr, c, lau])
          else:
            c += 1
            return recursive_solution([arr, c, lau])
      except:
        return arr

def mask(arr2):
  arr = []
  for c in range(len(arr2)):
    arr.append(arr2[c])
    params = [arr, 0, len(arr)]
    bolian = recursive_solution(params)
    if bolian == []:
      final_answr = 'sua array esta correta'
    else:
      final_answr = 'sua array esta errada'
  return final_answr

# arr2 = '{[()]}[][{}]({}){}'
# a = mask(arr2)
# print(a)

arr2 = '{[()]}[][{}]({})'
%timeit recursive_solution(arr2)
