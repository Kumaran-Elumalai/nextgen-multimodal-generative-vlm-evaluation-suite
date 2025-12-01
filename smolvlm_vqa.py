import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
import gradio as gr

# Model selection 
model_name = "HuggingFaceTB/SmolVLM-500M-Instruct"

processor = AutoProcessor.from_pretrained(model_name)
model = AutoModelForVision2Seq.from_pretrained(model_name)

device = "cpu" 
model.to(device)


def answer_question(image, question):
    """
    Generates a short description or answer for the given image + question
    using SmolVLM. Output is cleanly extracted from the model response.
    """
    try:
        # Resize image because the model expects ~224x224 resolution
        image = image.resize((224, 224))

        # Instruction prompt
        prompt = "USER: <image>\nDescribe the image in 1–2 complete sentences.\nASSISTANT:"

        inputs = processor(images=[image], text=[prompt], return_tensors="pt").to(device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=48,
            do_sample=True,
            top_p=0.9,
            temperature=0.7,
        )

        raw_output = processor.decode(outputs[0], skip_special_tokens=True).strip()

        
        # Keep only the text after "ASSISTANT:"
        if "ASSISTANT:" in raw_output:
            answer = raw_output.split("ASSISTANT:")[1].strip()
        else:
            answer = raw_output

        # Truncate incomplete endings
        if "." in answer:
            answer = ".".join(answer.split(".")[:-1]) + "."

        return answer.strip()

    except Exception as e:
        return f"Error: {e}"

# Gradio UI
interface = gr.Interface(
    fn=answer_question,
    inputs=[gr.Image(type="pil", label="Input Image"),
            gr.Textbox(label="Question")],
    outputs=gr.Textbox(label="Answer", lines=15, max_lines=40),
    title="SmolVLM Vision-Language Model Demo",
    description=(
        "A lightweight Vision-Language Model for image-based question answering. "
        "Upload an image and enter a question to generate a response."
    ),
)
interface.launch()