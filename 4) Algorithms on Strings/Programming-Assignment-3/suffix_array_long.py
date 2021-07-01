# python3
import sys

def sort_characters(s, len_s):
  #len_s = len(s)
  letter_map = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
  order = [None] * len_s
  count = [0] * 5
  for i in range(len_s):
    idx = letter_map[s[i]]
    count[idx] = count[idx] + 1
  for i in range(1,5): #Alphabet is $ACGT
    count[i] = count[i] + count[i-1]
  for i in reversed(range(len_s)):
    c = s[i]
    idx = letter_map[c]
    count[idx] = count[idx] - 1
    order[count[idx]] = i
  return order

def compute_char_classes(s, len_s, order):
  #len_s = len(s)
  cl = [None] * len_s
  cl[order[0]] = 0
  for i in range(1,len_s):
    if s[order[i]] != s[order[i-1]]:
      cl[order[i]] = cl[order[i-1]] + 1
    else:
      cl[order[i]] = cl[order[i-1]]
  return cl
  
def sort_doubled(s, len_s, l,order,cl):
  #len_s = len(s)
  count = [0] * len_s
  new_order = [None] * len_s
  for i in range(len_s):
    count[cl[i]] = count[cl[i]] + 1
  for i in range(1,len_s):
    count[i] = count[i] + count[i-1]
  for i in reversed(range(len_s)):
    #start = (order[i] - l + len_s) % len_s 
    start = (order[i] - l) % len_s
    c = cl[start]
    count[c] = count[c] - 1
    new_order[count[c]] = start
  return new_order

def update_classes(new_order, n, cl, l):
  #n = len(new_order)
  new_cl = [None] * n
  new_cl[new_order[0]] = 0
  for i in range(1,n):
    cur, prev = new_order[i], new_order[i-1]
    mid, midprev = (cur + l)%n, (prev+l)%n
    if cl[cur] != cl[prev] or cl[mid] != cl[midprev]:
      new_cl[cur] = new_cl[prev] + 1
    else:
      new_cl[cur] = new_cl[prev]
  return new_cl

def build_suffix_array(s):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  len_s = len(s)
  order = sort_characters(s, len_s)
  cl = compute_char_classes(s, len_s, order)
  l = 1
  while l < len_s:
    order = sort_doubled(s, len_s, l, order, cl)
    cl = update_classes(order, len_s, cl, l)
    l *= 2
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
