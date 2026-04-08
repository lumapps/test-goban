export enum Status {
  WHITE = 1,
  BLACK = 2,
  EMPTY = 3,
  OUT = 4,
}

export class Goban {
  private board: string[];

  constructor(board: string[]) {
    this.board = board;
  }

  public print() {
    console.log(this.board.join("\n"));
  }

  public getStatus(x: number, y: number): Status {
    if (
      x < 0 ||
      y < 0 ||
      y >= this.board.length ||
      x >= this.board[y].length
    ) {
      return Status.OUT;
    } else if (this.board[y][x] === ".") {
      return Status.EMPTY;
    } else if (this.board[y][x] === "o") {
      return Status.WHITE;
    } else if (this.board[y][x] === "#") {
      return Status.BLACK;
    }
    throw new Error(`Unknown goban value at position (${x}, ${y})`);
  }

  public isTaken(x: number, y: number): boolean {
    throw new Error("Not implemented");
  }
}
