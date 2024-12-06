import os

def rename_duplicate_files(directory):
    files = os.listdir(directory)
    file_dict = {}

    for file in files:
        name, ext = os.path.splitext(file)
        if ext.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tif']:  # Görüntü dosyası uzantıları
            if name not in file_dict:
                file_dict[name] = [file]
            else:
                file_dict[name].append(file)

    for name, file_list in file_dict.items():
        if len(file_list) > 1:
            for i, file in enumerate(file_list):
                new_name = f"{name}_{i+1}{os.path.splitext(file)[1]}"
                os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                print(f"{file} -> {new_name}")


directory_path = "/your/folder/path"
rename_duplicate_files(directory_path)
#uzantıları farklı aynı isme sahip dosyaların ismini değiştirmek