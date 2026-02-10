from PIL import Image


BASE_DIR = ""

def convert_image(in_path:str, out_path:str):
    img = Image.open(in_path).convert("L")
    threshold=128
    bw = img.point(lambda x: 255 if x > threshold else 0, '1')
    bw.save(out_path, format='PNG')
    
def convert_all():
    import os
    input_dir = os.path.join(BASE_DIR, "input_imgs")
    output_dir = os.path.join(BASE_DIR, "output_imgs")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            in_path = os.path.join(input_dir, filename)
            out_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_bw.png")
            convert_image(in_path, out_path)
            print(f"Converted {filename} to black and white PNG.")

if __name__ == "__main__":
    convert_all()
    print("All images converted to black and white PNG format.")