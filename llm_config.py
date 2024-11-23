# llm_config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

LLM_TYPE = "openai"  # Options: 'ollama', 'openai', 'anthropic' (careful API calls will cost a lot if your actually using ChatGPT)

# LLM settings for llama_cpp DOESN'T WORK 
MODEL_PATH = "/home/james/llama.cpp/models/gemma-2-9b-it-Q6_K.gguf" # Replace with your llama.cpp models filepath

LLM_CONFIG_LLAMA_CPP = {
    "llm_type": "llama_cpp",
    "model_path": MODEL_PATH,
    "n_ctx": 20000,  # context size
    "n_gpu_layers": 0,  # number of layers to offload to GPU (-1 for all, 0 for none)
    "n_threads": 8,  # number of threads to use
    "temperature": 0.7,  # temperature for sampling
    "top_p": 0.9,  # top p for sampling
    "top_k": 40,  # top k for sampling
    "repeat_penalty": 1.1,  # repeat penalty
    "max_tokens": 1024,  # max tokens to generate
    "stop": ["User:", "\n\n"]  # stop sequences
}

# LLM settings for Ollama
LLM_CONFIG_OLLAMA = {
    "llm_type": "ollama",
    "base_url": "http://localhost:11434",  # default Ollama server URL
    "model_name": "custom-phi3-32k-Q4_K_M",  # Replace with your Ollama model name
    "temperature": 0.7,
    "top_p": 0.9,
    "n_ctx": 55000,
    "context_length": 55000,
    "stop": ["User:", "\n\n"]
}

# LLM settings for OpenAI be careful API calls will cost a lot if your actually using ChatGPT
LLM_CONFIG_OPENAI = {
    "llm_type": "openai",
    "api_key": os.getenv("OPENAI_API_KEY"),  # Get API key from environment variable
    "base_url": os.getenv("OPENAI_API_BASE", "https://dashscope.aliyuncs.com/compatible-mode/v1"),  # Get base URL from environment variable
    "model_name": "qwen-max",  # Using Qwen-Max model
    "messages": [],  # Placeholder for conversation history
    "temperature": 0.7,
    "top_p": 0.9,
    "max_tokens": 32000,
    "stop": ["User:", "\n\n"],
    "presence_penalty": 0,
    "frequency_penalty": 0
}

# LLM settings for Anthropic
LLM_CONFIG_ANTHROPIC = {
    "llm_type": "anthropic",
    "api_key": os.getenv("ANTHROPIC_API_KEY", ""),  # Get API key from environment variable
    "model_name": "claude-3-sonnet-20240229",  # Updated to latest Claude model
    "temperature": 0.7,
    "top_p": 0.9,
    "max_tokens": 4096,
    "stop": ["User:", "\n\n"]
}

def get_llm_config():
    if LLM_TYPE == "llama_cpp":
        return LLM_CONFIG_LLAMA_CPP
    elif LLM_TYPE == "ollama":
        return LLM_CONFIG_OLLAMA
    elif LLM_TYPE == "openai":
        config = LLM_CONFIG_OPENAI.copy()
        # Ensure API key is set
        if not config["api_key"]:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        return config
    elif LLM_TYPE == "anthropic":
        config = LLM_CONFIG_ANTHROPIC.copy()
        # Ensure API key is set
        if not config["api_key"]:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
        return config
    else:
        raise ValueError(f"Invalid LLM_TYPE: {LLM_TYPE}")
