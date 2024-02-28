from task1 import count_figures, get_data_structure, compare_figures, figures

test_data1 = '''RbBQKBNR
pppppppp
wbwbwbwb
bwbwbwbw
wbwbwbwb
bwbwbwbw
pppppppp
RNBQKBNR'''

test_data2 = '''wNBQKBNR
pppppppp
wbwbwbwb
bwbwbwbw
wbwbwbwb
bwbwbwbw
pppppppp
RNBQKBNR'''

test_data3 = '''RNwQKBNR
pppppppp
wbwbwbwb
bwbwbwbw
wbwbwbwb
bwbwbwbw
pppppppp
RNBQKBNR'''

test_data4 = '''RNBbKBNR
pppppppp
wbwbwbwb
bwbwbwbw
wbwbwbwb
bwbwbwbw
pppppppp
RNBQKBNR'''

def data_manipulation(txt):
    return [list(i) for i in txt.split("\n")]

board1 = data_manipulation(test_data1)
board2 = data_manipulation(test_data2)
board3 = data_manipulation(test_data3)
board4 = data_manipulation(test_data4)

def test_count_figures():
    assert count_figures(board1) == {'B': 4, 'K': 2, 'N': 3, 'Q': 2, 'R': 4, 'p': 16}
    assert count_figures(board2) == {'B': 4, 'K': 2, 'N': 4, 'Q': 2, 'R': 3, 'p': 16}
    assert count_figures(board3) == {'B': 3, 'K': 2, 'N': 4, 'Q': 2, 'R': 4, 'p': 16}
    assert count_figures(board4) == {'B': 4, 'K': 2, 'N': 4, 'Q': 1, 'R': 4, 'p': 16}

def test_get_data_structure():
    assert get_data_structure(figures) == {'B': 4, 'K': 2, 'N': 4, 'Q': 2, 'R': 4, 'p': 16}


def test_compare_figures():
    data1 = count_figures(board1)
    data2 = count_figures(board2)
    data3 = count_figures(board3)
    data4 = count_figures(board4)

    data = get_data_structure(figures)

    assert compare_figures(data1, data) == "Knight"
    assert compare_figures(data2, data) == "Rook"
    assert compare_figures(data3, data) == "Bishop"
    assert compare_figures(data4, data) == "Queen"
