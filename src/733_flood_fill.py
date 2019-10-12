
class Solution(object):
	def floodFill(self, image, sr, sc, newColor):

		def dfs(img, r, c, oc, nc):
			if r >= len(img) or r < 0 or c >= len(img[0]) or c < 0 or img[r][c] != oc:
				return
			img[r][c] = nc
			dfs(img, r-1, c, oc, nc)
			dfs(img, r+1, c, oc, nc)
			dfs(img, r, c-1, oc, nc)
			dfs(img, r, c+1, oc, nc)

		pixel = image[sr][sc]
		if pixel == newColor:
			return image
		image[sr][sc] = newColor
		dfs(image, sr-1, sc, pixel, newColor)
		dfs(image, sr+1, sc, pixel, newColor)
		dfs(image, sr, sc-1, pixel, newColor)
		dfs(image, sr, sc+1, pixel, newColor)

	def floodFill_2(self, image, sr, sc, newColor):
		r, c = len(image), len(image[0])
		color = image[sr][sc]

		def dfs(i, j):
			if i < 0 or i >= r or j < 0 or j >= c:
				return
			if image[i][j] == newColor or image[i][j] != color:
				return
			image[i][j] = newColor
			dfs(i-1, j)
			dfs(i+1, j)
			dfs(i, j-1)
			dfs(i, j+1)

		dfs(sr, sc)
		return image