import os
import re

def convert_static_paths(file_path):
    print(f"🔍 Before modification in {file_path}:")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        # نمایش تمامی مسیرهای استاتیک
        static_paths = re.findall(r'(/static/staticfiles[^"]+)', content)
        print("Found static paths:", static_paths)

        # تغییر مسیر استاتیک
        new_content = re.sub(r'(/static/staticfiles[^"]+)', r'{% staticfiles "\1" %}', content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print(f"✅ Processed: {file_path}")
    print(f"🔍 After modification in {file_path}:")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content[:300])  # فقط چند خط اول برای بررسی

def convert_static_in_directory(directory_path):
    for subdir, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(subdir, file)
                convert_static_paths(file_path)

if __name__ == "__main__":
    print("🔄 Starting static path conversion...")
    convert_static_in_directory("templates")  # تغییر مسیر به دایرکتوری templates
    print("🎉 Conversion completed!")
