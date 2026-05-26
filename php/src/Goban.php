<?php

declare(strict_types=1);

namespace Goban;

class Goban
{
    /** @var list<list<string>> */
    private array $grid;

    /** @param list<string> $lines */
    public function __construct(array $lines)
    {
        $this->grid = array_map(str_split(...), $lines);
    }

    public function getStatus(int $x, int $y): Status
    {
        if (empty($this->grid)) {
            return Status::OUT;
        }

        if ($x < 0 || $y < 0 || $y >= count($this->grid) || $x >= count($this->grid[0])) {
            return Status::OUT;
        }

        return match ($this->grid[$y][$x]) {
            '#' => Status::BLACK,
            'o' => Status::WHITE,
            '.' => Status::EMPTY,
        };
    }

    public function isTaken(int $x, int $y): bool
    {
        throw new \RuntimeException('Not implemented');
    }
}
