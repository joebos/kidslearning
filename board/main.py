from board import Board

def main():
    b = Board()
    b.set_start(3, 1)
    b.move_right()
    b.set_end(3, 2)
    b.print()

main()