# from random import Random
# from math import ldexp

# class FullRandom(Random):

#     def random(self):
#         mantissa = 0x10_0000_0000_0000 | self.getrandbits(52)
#         exponent = -53
#         x = 0
#         while not x:
#             x = self.getrandbits(32)
#             exponent += x.bit_length() - 32
#         return ldexp(mantissa, exponent)