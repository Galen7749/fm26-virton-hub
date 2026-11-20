import urllib.request
import re

url = "https://at.alicdn.com/t/c/font_5254896_8h4mrawts3.js"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode("utf-8")
        print(f"成功获取，文件大小: {len(content)} 字节")
        icon_ids = re.findall(r'id=["\'](icon-[^"\']+)["\']', content)
        print(f"包含的图标总数: {len(icon_ids)}")
        print("所有图标列表:")
        for idx, icon in enumerate(icon_ids, 1):
            print(f"  {idx}. #{icon}")
except Exception as e:
    print("获取失败:", e)
