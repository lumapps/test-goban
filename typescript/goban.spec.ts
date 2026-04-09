import { describe, it } from "node:test";
import assert from "node:assert/strict";

import { Goban } from "./goban.ts";

describe("Goban", () => {
  it("test_white_is_taken_when_surrounded_by_black", () => {
    const goban = new Goban([".#.", "#o#", ".#."]);
    assert.ok(goban.isTaken(1, 1));
  });

  it("test_white_is_not_taken_when_it_has_a_liberty", () => {
    const goban = new Goban(["...", "#o#", ".#."]);
    assert.equal(goban.isTaken(1, 1), false);
  });

  it("test_black_shape_is_taken_when_surrounded", () => {
    const goban = new Goban(["oo.", "##o", "o#o", ".o."]);
    assert.ok(goban.isTaken(0, 1));
    assert.ok(goban.isTaken(1, 1));
    assert.ok(goban.isTaken(1, 2));
  });

  it("test_black_shape_is_not_taken_when_it_has_a_liberty", () => {
    const goban = new Goban(["oo.", "##.", "o#o", ".o."]);

    assert.equal(goban.isTaken(0, 1), false);
    assert.equal(goban.isTaken(1, 1), false);
    assert.equal(goban.isTaken(1, 2), false);
  });

  it("test_square_shape_is_taken", () => {
    const goban = new Goban(["oo.", "##o", "##o", "oo."]);
    assert.ok(goban.isTaken(0, 1));
    assert.ok(goban.isTaken(0, 2));
    assert.ok(goban.isTaken(1, 1));
    assert.ok(goban.isTaken(1, 2));
  });
});
