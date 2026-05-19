package main

import (
	"strings"
)

// Status enum
type Status int

const (
	WHITE Status = iota
	BLACK
	EMPTY
	OUT
)

// Goban grid
type Goban struct {
	grid [][]string
}

// NewGoban returns a new goban
func NewGoban(input []string) Goban {
	goban := Goban{grid: make([][]string, 0, len(input))}

	for _, line := range input {
		goban.grid = append(goban.grid, strings.Split(line, ""))
	}

	return goban
}

// GetStatus Get the status of a given position
//
// Args:
//
//	x: the x coordinate
//	y: the y coordinate
//
// Returns:
//
//	Status
func (goban Goban) GetStatus(x int, y int) Status {
	if len(goban.grid) == 0 {
		return OUT
	}

	if x < 0 || y < 0 || y >= len(goban.grid) || x >= len(goban.grid[0]) {
		return OUT
	}

	switch goban.grid[y][x] {
	case "#":
		return BLACK
	case "o":
		return WHITE
	case ".":
		return EMPTY
	}

	panic("GetStatus")
}

func (goban Goban) IsTaken(x int, y int) bool {
	panic("Not implemented")
}
