class Solution:
    def compress(self, chars: List[str]) -> int:
        compress = chars[0]
        cnt = 1
        left = 0
        right = 1
        while right < len(chars):
          if chars[left] == chars[right]:
            cnt += 1
            right += 1
          else:
            if cnt > 1:
              compress += str(cnt)
            compress += chars[right]
            cnt = 0
            left = right
        if cnt > 1:
          compress += str(cnt)
        chars.clear()
        for item in compress:
            chars.append(item)
        return len(compress)