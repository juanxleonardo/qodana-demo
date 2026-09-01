import { add, divide } from "../src/calculator";

test("add", () => {
  expect(add(2, 3)).toBe(5);
});

test("divide", () => {
  expect(divide(10, 2)).toBe(5);
});
