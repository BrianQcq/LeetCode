
class Solution(object):

	def getHint(self, secret, guess):
		bull, cow = 0, 0
		s, g = {}, {}

		for i in range(len(secret)):
			if secret[i] == guess[i]:
				bull += 1
			else:
				s[secret[i]] = s.get(secret[i], 0) + 1
				g[guess[i]] = g.get(guess[i], 0) + 1

		for key in s:
			if key in g:
				cow += min(s[key], g[key])
		return '{0}A{1}B'.format(bull, cow)