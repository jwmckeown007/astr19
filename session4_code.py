class Platypus:
	def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
		self.arm_length = float(arm_length)
		self.leg_length = float(leg_length)
		self.num_eyes = int(num_eyes)
		self.has_tail = bool(has_tail)
		self.is_furry = bool(is_furry)

	def characteristics(self):
		print("Platypus Physical Characteristics:")
		print(f"Arm Length: {self.arm_length} inches")
		print(f"Leg Length: {self.leg_length} inches")
		print(f"Number of Eyes: {self.num_eyes}")
		print(f"Has a Tail? {'Yes' if self.has_tail else 'No'}")
		print(f"Is Furry? {'Yes' if self.is_furry else 'No'}")

if __name__ == "__main__":
	Perry = Platypus(4.0, 4.2, 2, True, True)
	Perry.characteristics()
