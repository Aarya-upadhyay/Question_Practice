class Solution:
    def floodFill(self, image, sr, sc, color):

        n = len(image)
        m = len(image[0])

        c = image[sr][sc]

        visi = [[0] * m for _ in range(n)]

        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]

        def valid(i, j, n, m):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            return True

        def dfs(image, sr, sc, n, m, color, c, visi):

            image[sr][sc] = color
            visi[sr][sc] = 1

            for k in range(4):

                ro = sr + x[k]
                co = sc + y[k]

                if (valid(ro, co, n, m)
                    and visi[ro][co] == 0
                    and image[ro][co] == c):

                    dfs(image, ro, co, n, m, color, c, visi)

        dfs(image, sr, sc, n, m, color, c, visi)

        return image
