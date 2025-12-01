import gradio as gr
from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
import torch

# Load the ViLT model and processor once at the start
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

# Move model to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


def answer_question(image, question):
    """
    Takes an image + question and returns the model's answer.
    Includes basic safety checks and error handling.
    """
    try:
        # Ensure we are working with a PIL image
        if not isinstance(image, Image.Image):
            image = Image.fromarray(image)

        # Encode image + text for the model
        encoding = processor(image, question, return_tensors="pt").to(device)
        
        # Forward pass
        outputs = model(**encoding)
        logits = outputs.logits
        
        # Select the highest scoring label
        idx = logits.argmax(-1).item()
        answer = model.config.id2label[idx]
        return answer

    except Exception as e:
        return f"Error: {e}"


# Simple Gradio UI
interface = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Image(type="pil", label="Input Image"),
        gr.Textbox(label="Question")
    ],
    outputs=gr.Textbox(label="Answer", lines=15, max_lines=40),
    title="ViLT Visual Question Answering",
    description=(
        "A Visual Question Answering demo built using the ViLT model. "
        "Upload an image and enter a question to receive an answer."
    ),
)
interface.launch()
