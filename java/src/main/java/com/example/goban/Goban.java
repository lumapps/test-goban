package com.example.goban;

import java.util.List;

public class Goban {
    private final List<String> goban;

    public Goban(List<String> goban) {
        this.goban = goban;
    }

    public Status getStatus(int x, int y) {
        if (goban == null || goban.isEmpty() || x < 0 || y < 0 || y >= goban.size() || x >= goban.get(0).length()) {
            return Status.OUT;
        }
        char stone = goban.get(y).charAt(x);
        switch (stone) {
            case '.':
                return Status.EMPTY;
            case 'o':
                return Status.WHITE;
            case '#':
                return Status.BLACK;
            default:
                throw new IllegalArgumentException("Unknown goban value " + stone);
        }
    }

    public boolean isTaken(int x, int y) {
        throw new UnsupportedOperationException("Not implemented yet");
    }
}
