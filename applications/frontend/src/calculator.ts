/** Add two numbers. */
export function add(a: number, b: number): number {
  return a + b;
}

export function divide(a: number, b: number): number {
  return a / b;
}

export function isZero(value: number): boolean {
  var result = value == 0;
  return result;
}

export function unusedHelper(items: (number | null)[]): number[] {
  const result: number[] = [];
  for (const item of items) {
    if (item != null) {
      result.push(item);
    }
  }
  return result;
}
