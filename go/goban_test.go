package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

type TestPosition struct {
	X int
	Y int
}

type TestCase struct {
	name           string
	input          []string
	position       TestPosition
	expectedResult bool
}

func TestGoban(t *testing.T) {
	testCases := []TestCase{
		{
			name: "test_white_is_taken_when_surrounded_by_black",
			input: []string{
				".#.",
				"#o#",
				".#.",
			},
			position:       TestPosition{1, 1},
			expectedResult: true,
		},
		{
			name: "test_white_is_not_taken_when_it_has_a_liberty",
			input: []string{
				"...",
				"#o#",
				".#.",
			},
			position:       TestPosition{1, 1},
			expectedResult: false,
		},
		{
			name: "test_black_shape_is_taken_when_surrounded-1",
			input: []string{
				"oo.",
				"##o",
				"o#o",
				".o.",
			},
			position:       TestPosition{0, 1},
			expectedResult: true,
		},
		{
			name: "test_black_shape_is_taken_when_surrounded-2",
			input: []string{
				"oo.",
				"##o",
				"o#o",
				".o.",
			},
			position:       TestPosition{1, 1},
			expectedResult: true,
		},
		{
			name: "test_black_shape_is_taken_when_surrounded-3",
			input: []string{
				"oo.",
				"##o",
				"o#o",
				".o.",
			},
			position:       TestPosition{1, 2},
			expectedResult: true,
		},
		{
			name: "test_black_shape_is_not_taken_when_it_has_a_liberty-1",
			input: []string{
				"oo.",
				"##.",
				"o#o",
				".o.",
			},
			position:       TestPosition{0, 1},
			expectedResult: false,
		},
		{
			name: "test_black_shape_is_not_taken_when_it_has_a_liberty-2",
			input: []string{
				"oo.",
				"##.",
				"o#o",
				".o.",
			},
			position:       TestPosition{1, 1},
			expectedResult: false,
		},
		{
			name: "test_black_shape_is_not_taken_when_it_has_a_liberty-3",
			input: []string{
				"oo.",
				"##.",
				"o#o",
				".o.",
			},
			position:       TestPosition{1, 2},
			expectedResult: false,
		},
		{
			name: "test_square_shape_is_taken-1",
			input: []string{
				"oo.",
				"##o",
				"##o",
				"oo.",
			},
			position:       TestPosition{0, 1},
			expectedResult: true,
		},
		{
			name: "test_square_shape_is_taken-2",
			input: []string{
				"oo.",
				"##o",
				"##o",
				"oo.",
			},
			position:       TestPosition{0, 2},
			expectedResult: true,
		},
		{
			name: "test_square_shape_is_taken-3",
			input: []string{
				"oo.",
				"##o",
				"##o",
				"oo.",
			},
			position:       TestPosition{1, 1},
			expectedResult: true,
		},
		{
			name: "test_square_shape_is_taken-4",
			input: []string{
				"oo.",
				"##o",
				"##o",
				"oo.",
			},
			position:       TestPosition{1, 2},
			expectedResult: true,
		},
	}

	for _, testCase := range testCases {
		t.Run(testCase.name, func(t *testing.T) {
			goban := NewGoban(testCase.input)

			require.Equal(t, testCase.expectedResult, goban.IsTaken(testCase.position.X, testCase.position.Y))
		})
	}
}
