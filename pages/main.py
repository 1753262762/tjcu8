import json
import os

# 获取父文件夹的路径
parent_folder = os.path.dirname(os.path.dirname(__file__))  # 上一层目录
save_folder = os.path.join(parent_folder,'pages//json')  # 指向'save' 文件夹
image_folder = os.path.join(parent_folder, 'image')  # 指向 'image' 文件夹

image_index = {'images': []}

# 检查图片文件夹是否存在
if not os.path.exists(image_folder):
    print(f"指定的文件夹 {image_folder} 不存在,请确认路径是否正确.")
else:
    # 使用 os.walk 遍历文件夹及其子目录
    for root, dirs, files in os.walk(image_folder):
        for filename in files:
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # 只包含常见的图片格式
                file_path = os.path.join(root, filename)  # 获取完整路径
                relative_path = os.path.relpath(file_path, parent_folder)  # 转换为相对路径
                image_index['images'].append({
                    'name': filename,
                    'path': "..\\"+relative_path  # 使用相对路径
                })

    # 保存为 JSON 文件
    output_path = os.path.join(save_folder, 'image_index.json')  # 设置输出路径
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(image_index, json_file, ensure_ascii=False, indent=4)

    print("image_index.json 文件已创建!")
