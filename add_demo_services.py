import os
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio_app.models import Service

def add_demo_services():
    print("Starting Demo Services injection...")
    
    services_data = [
        {
            "title": "Autonomous AI Agents",
            "description": "Custom autonomous agents capable of complex reasoning, tool use, and multi-step task execution. Built with LangChain and AutoGPT architectures.",
            "technologies": "LangChain, CrewAI, Python, OpenAI, Anthropic",
            "starting_price": 1499.00,
            "delivery_time": "3-5 Weeks",
            "basic_description": "Single-purpose task agent with API integration.",
            "standard_description": "Multi-agent swarm for complex workflow automation.",
            "premium_description": "Enterprise-grade autonomous system with human-in-the-loop controls."
        },
        {
            "title": "Enterprise RAG Pipelines",
            "description": "High-performance Retrieval Augmented Generation systems. Connect your private documents to LLMs with advanced semantic search.",
            "technologies": "ChromaDB, Pinecone, LlamaIndex, FAISS, Python",
            "starting_price": 1999.00,
            "delivery_time": "4-6 Weeks",
            "basic_description": "Standard PDF/Text document retrieval system.",
            "standard_description": "Advanced hybrid search (Semantic + Keyword) with re-ranking.",
            "premium_description": "Full-scale knowledge graph integration with real-time data sync."
        },
        {
            "title": "Custom LLM Fine-tuning",
            "description": "Tailor open-source models (Llama 3, Mistral) to your specific domain, tone, and private dataset for maximum performance and privacy.",
            "technologies": "PyTorch, Hugging Face, QLoRA, CUDA, Weights & Biases",
            "starting_price": 2999.00,
            "delivery_time": "6-8 Weeks",
            "basic_description": "LoRA fine-tuning for specific tone and style.",
            "standard_description": "Full parameter tuning on domain-specific datasets.",
            "premium_description": "Custom pre-training and specialized alignment (RLHF/DPO)."
        },
        {
            "title": "Multi-modal AI Chatbots",
            "description": "Next-gen conversational interfaces that understand text, images, and voice. Deployable across WhatsApp, Web, and Mobile.",
            "technologies": "FastAPI, React, Whisper, GPT-4V, Twilio",
            "starting_price": 999.00,
            "delivery_time": "2-4 Weeks",
            "basic_description": "Text-based smart chatbot with FAQ integration.",
            "standard_description": "Voice and Image capable assistant with CRM sync.",
            "premium_description": "Omnichannel AI workforce with full task execution capabilities."
        },
        {
            "title": "AI-Powered Computer Vision",
            "description": "Advanced visual intelligence for object detection, face recognition, and automated quality control in industrial or retail environments.",
            "technologies": "OpenCV, YOLOv8, TensorFlow, NVIDIA Jetson, Mediapipe",
            "starting_price": 2499.00,
            "delivery_time": "5-7 Weeks",
            "basic_description": "Real-time object detection and counting system.",
            "standard_description": "Advanced behavioral analysis and tracking.",
            "premium_description": "Custom edge-device deployment with distributed camera networks."
        }
    ]

    for data in services_data:
        service, created = Service.objects.update_or_create(
            title=data['title'],
            defaults=data
        )
        if created:
            print(f"Created: {service.title}")
        else:
            print(f"Updated: {service.title}")

    print("\nAll demo services injected successfully!")

if __name__ == "__main__":
    add_demo_services()
