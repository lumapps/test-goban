<?php

declare(strict_types=1);

namespace Goban;

enum Status
{
    case BLACK;
    case WHITE;
    case EMPTY;
    case OUT;
}
