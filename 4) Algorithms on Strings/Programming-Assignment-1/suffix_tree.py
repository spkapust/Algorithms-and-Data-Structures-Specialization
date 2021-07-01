# python3
import sys
#from collections import deque

# def bfs(tree, text):
#   result = []
#   q = deque()
#   q.append(0)
#   while(len(q)):
#     currentnode = q.popleft()
#     for item in tree[currentnode].items():
#       key, newnode = item
#       s, l = key
#       result.append(text[s:s+l])
#       q.append(newnode)
#   return result

#DFS but it just adds the edges as it comes across them
def dfs(tree, text):
  result = []
  stack = []
  stack.append(0)
  while(len(stack)):
    n = stack.pop()
    for item in tree[n].items():
      edge, next_n = item
      result.append(text[edge[0]:edge[0]+edge[1]])
      stack.append(next_n)
  return result

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  tree = {}
  tree[0] = {}
  num_nodes = 1
  lt = len(text)
  
  r = range(lt)
  #Goes much slower if reversed on grader but will still pass
  reverse = False
  if reverse:
      r = reversed(r)

  for i in r:
    new_edge = (i, lt - i)
    found_match = True
    split = False
    sp = i
    currentnode = 0
    while(found_match):
      found_match = False
      edges = tree[currentnode].keys()
      for e in edges:
        s = e[0]
        l = min(e[1],lt - sp)
        
        #greatest_common_prefix
        match_length = 0
        while(match_length < l and text[s+match_length] == text[sp+match_length]):
            match_length += 1
          

        if match_length > 0:
          sp += match_length
          if match_length < l:
            #split
            #
            #   w               w                    w  = currentnode
            # a |             a'|                    a  = old_edge = e
            #   x    ---->      x                    a' = adjusted_edge
            #  /|\             / \                   x  = 
            # j k l           y   z
            #                /|\
            #               j k l

            split = True
            w = currentnode
            old_edge = e
            adjusted_edge = (e[0], match_length)
            x = tree[w][e]
            x_to_y = (e[0] + match_length, e[1] - match_length)
            x_to_z = (sp, lt-sp)
            y = num_nodes
            num_nodes += 1
            z = num_nodes
            num_nodes += 1
            found_match = False
          else:
            currentnode = tree[currentnode][e]
            new_edge = (sp, lt - sp)
            found_match = True
          break

    if split:
      del tree[w][old_edge]
      tree[w][adjusted_edge] = x
      tree[y] = tree[x].copy()
      tree[x].clear()
      tree[x][x_to_y] = y
      tree[x][x_to_z] = z
      tree[z] = {}
    else:
      tree[currentnode][new_edge] = num_nodes
      tree[num_nodes] = {}
      num_nodes += 1
      
  result = dfs(tree, text)
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))