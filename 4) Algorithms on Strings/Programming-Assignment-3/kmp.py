# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  prefix = []
  pl = len(pattern)
  s = pattern + '$' + text
  prefix.append(0)
  border = 0
  for i, c in enumerate(s):
    if i == 0: 
      continue
    while (border > 0) and (c != s[border]):
      border = prefix[border - 1]
    if c == s[border]:
      border += 1
    else:
      border = 0
    prefix.append(border)
    if border == pl:
      result.append(i - (2*pl))

  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

