# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    #Per directions, use direct addressing
    phonebook = ['not found'] * (10**7 + 1)  
    result = []
    
    for cur_query in queries:
        if cur_query.type == 'add':
            phonebook[cur_query.number] = cur_query.name
        
        elif cur_query.type == 'del':
            phonebook[cur_query.number] = 'not found'

        else:
            response = phonebook[cur_query.number]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

