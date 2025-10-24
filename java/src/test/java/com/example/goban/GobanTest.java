package com.example.goban;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class GobanTest {

    @Test
    void whiteIsTakenWhenSurroundedByBlack() {
        Goban goban = new Goban(Arrays.asList(
                ".#.",
                "#o#",
                ".#."
        ));
        assertTrue(goban.isTaken(1, 1));
    }

    @Test
    void whiteIsNotTakenWhenItHasALiberty() {
        Goban goban = new Goban(Arrays.asList(
                "...",
                "#o#",
                ".#."
        ));
        assertFalse(goban.isTaken(1, 1));
    }

    @Test
    void blackShapeIsTakenWhenSurrounded() {
        Goban goban = new Goban(Arrays.asList(
                "oo.",
                "##o",
                "o#o",
                ".o."
        ));
        assertTrue(goban.isTaken(0, 1));
        assertTrue(goban.isTaken(1, 1));
        assertTrue(goban.isTaken(1, 2));
    }

    @Test
    void blackShapeIsNotTakenWhenItHasALiberty() {
        Goban goban = new Goban(Arrays.asList(
                "oo.",
                "##.",
                "o#o",
                ".o."
        ));
        assertFalse(goban.isTaken(0, 1));
        assertFalse(goban.isTaken(1, 1));
        assertFalse(goban.isTaken(1, 2));
    }

    @Test
    void squareShapeIsTaken() {
        Goban goban = new Goban(Arrays.asList(
                "oo.",
                "##o",
                "##o",
                "oo."
        ));
        assertTrue(goban.isTaken(0, 1));
        assertTrue(goban.isTaken(0, 2));
        assertTrue(goban.isTaken(1, 1));
        assertTrue(goban.isTaken(1, 2));
    }
}
