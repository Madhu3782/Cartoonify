# 🎨 Cartoonify – Turn Your Photo into a Cartoon

Cartoonify is a fun and beginner-friendly Python application that transforms your photos into cartoon-style images using OpenCV and basic image processing techniques.

---

## 📷 Demo

| Original Image | Cartoonified Image |
|----------------|--------------------|
| ![original](sample/original.jpg) | ![cartoon](sample/cartoon.jpg) |

---

## ✨ Features

- ✅ Convert any image into cartoon-style artwork
- ✅ Real-time webcam cartoonization (optional)
- ✅ Smooth color quantization and edge detection
- ✅ Save the cartoon image locally
- ✅ Lightweight and easy to use

---

## 🛠️ Technologies Used

- Python 3
- OpenCV
- NumPy
- Matplotlib *(for display, optional)*
- Tkinter or Streamlit *(if GUI is added)*

---

Install the dependencies

bash
Copy
Edit
pip install -r requirements.txt

## 🚀 How to Run


## 📂 Project Structure
cartoonify/
├── cartoonify.py
├── sample/
│   ├── original.jpg
│   └── cartoon.jpg
├── requirements.txt
└── README.md

📚 How It Works
1)Image is read using OpenCV

2)Applied bilateral filter to smoothen the colors

3)Edge detection using adaptive threshold

4)Combine edges with the smooth image

5)Display or save the final cartoonified image
