test_data = '''RbBQKBNR
pppppppp
wbwbwbwb
bwbwbwbw
wbwbwbwb
bwbwbwbw
pppppppp
RNBQKBNR'''

# test_data = '''wNBQKBNR
# pppppppp
# wbwbwbwb
# bwbwbwbw
# wbwbwbwb
# bwbwbwbw
# pppppppp
# RNBQKBNR'''

# test_data = '''RNwQKBNR
# pppppppp
# wbwbwbwb
# bwbwbwbw
# wbwbwbwb
# bwbwbwbw
# pppppppp
# RNBQKBNR'''

figures = [
    {"name": "King", "symbol": "K", "qty": 2},
    {"name": "Queen", "symbol": "Q", "qty": 2},
    {"name": "Rook", "symbol": "R", "qty": 4},
    {"name": "Bishop", "symbol": "B", "qty": 4},
    {"name": "Knight", "symbol": "N", "qty": 4},
    {"name": "Pawn", "symbol": "p", "qty": 16},
]

def main():
    board = [list(i) for i in test_data.split("\n")]

    current_items = count_figures(board)
    print(current_items)
    database = get_data_structure(figures)
    missed_figure = compare_figures(current_items, database)


    print(missed_figure)

def count_figures(user):
    current_figures = {}
    for i in user:
        for k in i:
            if k == "w" or k == "b":
                continue
            else:
                current_figures[k] = current_figures.get(k,0)+1
    return dict(sorted(current_figures.items(), key = lambda x: x[0]))

def get_data_structure(data):
    data_figures = {}
    for i in data:
        data_figures[i['symbol']] = i["qty"]
    return dict(sorted(data_figures.items(), key = lambda x: x[0]))

def compare_figures(current, database):
    for i in database:
        for m in current:
            if i == m and database[i] != current[i]:
                for item in figures:
                    if item["symbol"] == m:
                        return item["name"]

main()
