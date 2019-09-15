
class Solution(object):

	def numUniqueEmail(self, emails):

		res = []
		for email in emails:
			local, domain = email.split('@')
			local = local.replace('.', '')
			local = local.split('+')[0]
			print(local, domain)
			if local +'@' + domain not in res:
				res.append(local+'@'+domain)
		return len(res)

A=Solution()
res=A.numUniqueEmail(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"])
print(res)