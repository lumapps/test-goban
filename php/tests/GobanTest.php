<?php

declare(strict_types=1);

namespace Goban\Tests;

use Goban\Goban;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;

class GobanTest extends TestCase
{
    /** @return array<string, array{list<string>, int, int, bool}> */
    public static function provideTestCases(): array
    {
        return [
            'white_is_taken_when_surrounded_by_black' => [
                ['.#.', '#o#', '.#.'], 1, 1, true,
            ],
            'white_is_not_taken_when_it_has_a_liberty' => [
                ['...', '#o#', '.#.'], 1, 1, false,
            ],
            'black_shape_is_taken_when_surrounded-1' => [
                ['oo.', '##o', 'o#o', '.o.'], 0, 1, true,
            ],
            'black_shape_is_taken_when_surrounded-2' => [
                ['oo.', '##o', 'o#o', '.o.'], 1, 1, true,
            ],
            'black_shape_is_taken_when_surrounded-3' => [
                ['oo.', '##o', 'o#o', '.o.'], 1, 2, true,
            ],
            'black_shape_is_not_taken_when_it_has_a_liberty-1' => [
                ['oo.', '##.', 'o#o', '.o.'], 0, 1, false,
            ],
            'black_shape_is_not_taken_when_it_has_a_liberty-2' => [
                ['oo.', '##.', 'o#o', '.o.'], 1, 1, false,
            ],
            'black_shape_is_not_taken_when_it_has_a_liberty-3' => [
                ['oo.', '##.', 'o#o', '.o.'], 1, 2, false,
            ],
            'square_shape_is_taken-1' => [
                ['oo.', '##o', '##o', 'oo.'], 0, 1, true,
            ],
            'square_shape_is_taken-2' => [
                ['oo.', '##o', '##o', 'oo.'], 0, 2, true,
            ],
            'square_shape_is_taken-3' => [
                ['oo.', '##o', '##o', 'oo.'], 1, 1, true,
            ],
            'square_shape_is_taken-4' => [
                ['oo.', '##o', '##o', 'oo.'], 1, 2, true,
            ],
        ];
    }

    /**
     * @param list<string> $input
     */
    #[DataProvider('provideTestCases')]
    public function testIsTaken(array $input, int $x, int $y, bool $expected): void
    {
        $goban = new Goban($input);

        $this->assertSame($expected, $goban->isTaken($x, $y));
    }
}
