class Solution:
    def maximumWhiteTiles(self, tiles, carpetLen):
        tiles.sort(key=lambda x: x[0])
        ans = cover = left = 0
        for tl, tr in tiles:
            cover += tr - tl + 1
            while tiles[left][1] < tr - carpetLen + 1:
                cover -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            uncover = max(tr - carpetLen + 1 - tiles[left][0], 0)  # 减去毯子左断电未覆盖的瓷砖段部分
            ans = max(ans, cover - uncover)
        return ans

if __name__ == '__main__':
    tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]]
    carpetLen = 10
    print(Solution().maximumWhiteTiles(tiles, carpetLen))   