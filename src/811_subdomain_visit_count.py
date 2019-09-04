
class Solution(object):

	def subdomainVisit(self, cpdomains):

		d = {}
		for item in cpdomains:
			n, domains = item.split()
			n, domains = int(n), domains.split('.')

			for i in range(len(domains)):
				temp = '.'.join(domains[i:])
				d[temp] = d[temp] + n if temp in d else n
		return [str(d[i]) + ' ' + i for i in d]
