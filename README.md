# 🧠📸 Vision–Language Models (VLMs) for Visual Question Answering

Modern AI systems are increasingly **multimodal**, capable of processing and generating information from diverse sources such as **images and text**.  
This project focuses on **Vision–Language Models (VLMs)** designed to combine visual and textual understanding for:

- **Visual Question Answering (VQA)**
- **Descriptive image generation and captioning**

## 🚀 Overview

This repository demonstrates practical multimodal AI development by implementing two advanced VLMs:

### 🔹 ViLT – Vision-and-Language Transformer
- Lightweight and optimized for CPU-friendly deployment  
- Fast inference  
- Ideal for **single-word or short-answer VQA**

### 🔹 SmolVLM – Small Vision-Language Model
- Generates multi-sentence, descriptive responses  
- Great for **detailed image understanding and explanation**

## 🎯 Project Goals

This project aims to provide:

- ✔️ **End-to-end multimodal pipelines** for image + text reasoning  
- ✔️ **Efficient CPU-based inference** without requiring GPUs  
- ✔️ **Clean, professional, interactive AI demos** showcasing real-world VQA and multimodal capabilities  

## 📁 Repository Structure

```
nextgen-multimodal-generative-vlm-evaluation-suite/
│── vilt_vqa/
│   └── vilt_app.py
│── smolvlm_vqa/
│   └── smolvlm_app.py
│── assets/
│   └── sample_images/
│── README.md
│── requirements.txt
```
## 🧠 Features

- **Two Multimodal Pipelines:**  
  ViLT (classification-style VQA) and SmolVLM (generative, descriptive answers)

- **Interactive Gradio Interfaces:**  
  Upload an image and get a professional, descriptive answer

- **CPU-Friendly Implementation:**  
  Optimized for environments without GPU

## 🔧 Technical Highlights

### 🔹 Vision–Language Processing
- **ViLT:** Uses attention-based fusion between image patches and text tokens  
- **SmolVLM:** Combines a Vision Transformer encoder with an LLM decoder for generative outputs

### 🔹 Prompt Engineering
- Designed to produce descriptive, multi-sentence answers  
- Formatting ensures structured and readable responses

### 🔹 Inference Optimizations
- Image resizing and normalization  
- Controlled token generation (48–60 tokens) to balance latency and richness

### 🔹 Why These Models?
- **ViLT →** Efficient, lightweight transformer ideal for fact-based VQA  
- **SmolVLM →** Produces rich, detailed multi-sentence explanations

## 🚀 Usage Instructions
- Run ViLT App
```
cd vilt_vqa
python vilt_app.py
```

- Run SmolVLM App
```
cd smolvlm_vqa
python smolvlm_app.py
```
#### A Gradio interface will open in your browser automatically.
