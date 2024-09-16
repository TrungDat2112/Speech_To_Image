# Đọc file captions.txt và lưu trữ captions theo tên file ảnh
def load_captions(file_path):
    captions = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',', 1)  # Tách thành 2 phần: tên file và caption
            image_id = parts[0].strip()  # Lấy tên file ảnh
            caption = parts[1].strip()   # Lấy caption
            if image_id not in captions:
                captions[image_id] = []
            captions[image_id].append(caption)  # Thêm caption vào danh sách của ảnh
    return captions

# Đường dẫn tới file captions.txt
caption_file_path = 'captions.txt'

# Tải các mô tả từ file captions.txt
captions = load_captions(caption_file_path)

# Kiểm tra kết quả
print(f"Loaded {len(captions)} images with captions.")
sample_image_id = list(captions.keys())[0]
print(f"Captions for {sample_image_id}: {captions[sample_image_id]}")
import os
# Đường dẫn tới các thư mục train, val, test
train_folder = 'Images/train'
val_folder = 'Images/val'
test_folder = 'Images/test'

# Lấy danh sách file ảnh từ các thư mục
train_images = os.listdir(train_folder)
val_images = os.listdir(val_folder)
test_images = os.listdir(test_folder)

# Liên kết các mô tả với từng tập dữ liệu
train_captions = {img: captions[img] for img in train_images if img in captions}
val_captions = {img: captions[img] for img in val_images if img in captions}
test_captions = {img: captions[img] for img in test_images if img in captions}

print(f"Số lượng captions trong train: {len(train_captions)}")
print(f"Số lượng captions trong val: {len(val_captions)}")
print(f"Số lượng captions trong test: {len(test_captions)}")
print(len(train_captions) + len(val_captions) + len(test_captions))
