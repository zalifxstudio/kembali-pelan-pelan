from PIL import Image
from pathlib import Path
assets=Path(r"D:\CODEX\Kembali_Pelan_Pelan\book\assets")
assets.mkdir(parents=True, exist_ok=True)
files=[["cover","D:\\net3bar\\.codex\\generated_images\\01a159b5-57ea-7c12-b503-84989eedb1f9\\exec-8e7e95a1-3ae9-4c08-a16a-9c7932fd6561.png"],["patterns","D:\\net3bar\\.codex\\generated_images\\01a159b5-57ea-7c12-b503-84989eedb1f9\\exec-c89ebbdd-9fe4-4af0-90af-0f898387a5b2.png"],["prayer","D:\\net3bar\\.codex\\generated_images\\01a159b5-57ea-7c12-b503-84989eedb1f9\\exec-cef2beec-9bda-4a1b-ba94-44a69b78739f.png"],["speech","D:\\net3bar\\.codex\\generated_images\\01a159b5-57ea-7c12-b503-84989eedb1f9\\exec-bf2a7447-9e15-4315-93aa-7dfeb2c06d33.png"],["quran","D:\\net3bar\\.codex\\generated_images\\01a159b5-57ea-7c12-b503-84989eedb1f9\\exec-5cf7aab3-d025-438b-8605-59ee209b2a4e.png"],["sleep","D:\\net3bar\\.codex\\generated_images\\01a159b5-57ea-7c12-b503-84989eedb1f9\\exec-3b37f73b-b227-4e2a-8997-5c71bf17609f.png"],["thinking","D:\\net3bar\\.codex\\generated_images\\01a159b5-57ea-7c12-b503-84989eedb1f9\\exec-ac3ac68f-bc3a-46ae-b183-c14bc0836a65.png"],["restart","D:\\net3bar\\.codex\\generated_images\\01a159b5-57ea-7c12-b503-84989eedb1f9\\exec-19ebadfe-76e9-4cd4-94ba-79b129d8244a.png"]]
for name,source in files:
 im=Image.open(source).convert("RGB")
 limit=1500 if name=="cover" else 900
 im.thumbnail((limit,limit))
 target=assets/(name+".webp")
 im.save(target,"WEBP",quality=84,method=6)
 print(name,im.size,target.stat().st_size)
