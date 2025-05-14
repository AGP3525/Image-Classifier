import streamlit as st
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import torch

st.sidebar.title("Bilgi")
st.sidebar.info(
    "Bu uygulama Hugging Face'ten eğitilmiş ViT modeli ile görüntü sınıflandırması yapar. "
    "Resminizi yükleyin, AI tahmin etsin!"
)
st.sidebar.markdown("---")
st.sidebar.write("Geliştiren: Alican")

st.title("Görüntü Sınıflandırıcı AI")
st.write("Bir resim yükleyin, hangi sınıfa ait olduğunu tahmin edelim.")

model_name = "google/vit-base-patch16-224"
extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

uploaded_file = st.file_uploader("Bir resim yükleyin", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    resized_image = image.resize((300, 300))
    st.image(resized_image, caption="Yüklenen Görüntü", use_container_width=False)

    if st.button("Tahmin Et"):
        inputs = extractor(images=image, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        predicted_label = model.config.id2label[predicted_class_idx]
        st.success(f"Tahmin Edilen Sınıf: **{predicted_label}**")

st.markdown("---")
st.markdown(" Developed by Alican Güldürdek")
