# python3
import sys


def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_counts_before - for each character C in bwt and each position P in bwt,
        occ_counts_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  amt = {}
  occ_counts_before = {}
  for c in '$ACGT':
      amt[c] = 0
      occ_counts_before[c] = {}
      occ_counts_before[c][-1] = 0
  
  #find out rank of each index
  rank = []
  for i, c in enumerate(bwt):
      rank.append(amt[c])
      amt[c] += 1
      for ch in '$ACGT':
        occ_counts_before[ch][i] = occ_counts_before[ch][i-1] 
      occ_counts_before[c][i] += 1

  #get starting indexes, amount dictionary is now the starting index (si) for each character
  prev = '$'
  for c in 'ACGT':
      amt[c] += amt[prev]
      prev = c
  
  ahead = 'T'
  for c in 'GCA$':
      amt[ahead] = amt[c]
      ahead = c
  amt['$'] = 0
  starts = amt

  return starts, occ_counts_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  top = 0
  bottom = len(bwt) - 1
  while top <= bottom:
    if len(pattern):
      symbol = pattern[-1]
      pattern = pattern[:-1]
      #print(starts, occ_counts_before)
      contains_occurence = occ_counts_before[symbol][bottom] - occ_counts_before[symbol][top-1] > 0
      if contains_occurence:
        top = starts[symbol] + occ_counts_before[symbol][top-1]
        bottom = starts[symbol] + occ_counts_before[symbol][bottom] - 1
      else:
        return 0
    else:
      return bottom - top + 1

  # Implement this function yourself
  return 0
     


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
