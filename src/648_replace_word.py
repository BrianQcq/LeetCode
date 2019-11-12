
class Solution(object):

	# naive approach
	def replaceWords(self, dict, sentence):
		temp = sentence.split()
		for word in dict:
			for i in range(len(sentence)):
				if temp[i].startswith(word):
					temp[i] = word
		return ' '.join(temp)