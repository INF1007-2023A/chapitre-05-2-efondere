#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	result = name + "\n"
	total_tax_free = 0
	for item in data:
		total_tax_free += item[INDEX_QUANTITY] * item[INDEX_PRICE]

	taxes = total_tax_free * 0.15
	total = total_tax_free + taxes

	result += f"SOUS TOTAL {total_tax_free:10.2f} $\n"
	result += f"TAXES      {taxes:10.2f} $\n"
	result += f"TOTAL      {total:10.2f} $"

	return result


def format_number(number, num_decimal_digits):
	result = ""
	is_negative = number < 0
	integer_part = int(abs(number))
	decimal_part = abs(number) - float(integer_part)
	decimal_part_str = str(decimal_part)

	integer_part_str = str(integer_part)
	for c in range(1, len(integer_part_str) + 1):
		if c != 1 and c % 3 == 1:
			result = " " + result
		result = integer_part_str[-c] + result

	if num_decimal_digits > 0:
		result += "."
		for c in range(0, num_decimal_digits):
			if c != 0 and c % 3 == 0:
				result += " "
			result += decimal_part_str[c + 2]

	if is_negative:
		result = "-" + result

	return result

def get_triangle(num_rows):
	num_cols = num_rows * 2 - 1
	result = "+" * (num_cols + 2) + "\n"
	for row in range(1, num_rows + 1):
		num_letters = row * 2 - 1
		num_spaces = (num_cols - num_letters) // 2
		result += "+" + " " * num_spaces + "A" * num_letters
		result += " " * num_spaces + "+" + "\n"
	result += "+" * (num_cols + 2)
	return result


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
