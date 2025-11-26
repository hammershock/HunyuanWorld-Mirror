from huggingface_hub import hf_hub_download

# 指定保存目录
local_dir = "/temp/hanmo/models/HunyuanWorld-Mirror"

# 下载 skyseg.onnx
file_path = hf_hub_download(
    repo_id="JianyuanWang/skyseg",
    filename="skyseg.onnx",
    local_dir=local_dir,
    local_dir_use_symlinks=False
)

print("Downloaded to:", file_path)
