# Image-Classifier
Image Classification Using PyCharm


Proje Klasör Yapısı

image-classifier-app/
├── app.py
├── requirements.txt
└── README.md

# Görüntü Sınıflandırıcı AI

Bu proje, Hugging Face üzerinde eğitilmiş ViT (Vision Transformer) modelini kullanarak bir görüntünün hangi sınıfa ait olduğunu tahmin eden basit bir Streamlit web uygulamasıdır.

Özellikler

- Kullanıcıdan resim yüklemesi alır.
- Yüklenen resmi ViT modeline verir.
- Modelin tahmin ettiği sınıfı kullanıcıya gösterir.
- Hugging Face’ten `google/vit-base-patch16-224` modeli kullanılmıştır.

Kullanılan Teknolojiler

- [Streamlit](https://streamlit.io/)
- [Transformers by Hugging Face](https://huggingface.co/transformers/)
- [Torch](https://pytorch.org/)
- [Pillow (PIL)](https://pillow.readthedocs.io/)

Uygulamayı Çalıştırma

1. Depoyu klonlayın:

bash
git clone https://github.com/kullanici-adiniz/image-classifier-app.git
cd image-classifier-app

Gerekli Kütüphaneler
pip install -r requirements.txt

Uygulamayı Başlatma
streamlit run main.py




