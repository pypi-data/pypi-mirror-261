# %%

import os
from typing import Any, Callable, Dict, List, Optional, Union

# from langchain_experimental.llms.ollama_functions import OllamaFunctions
# from langchain_community.chat_models import ChatOllama
# from langchain_mistralai import ChatMistralAI
# from openai import OpenAI
# from langchain_together import Together

from langchain_openai import ChatOpenAI, OpenAI
from langchain_fireworks import ChatFireworks
from pydantic import BaseModel


class LLM(BaseModel):
    """Represents a Language Learning Model (LLM) configuration and its interaction logic.

    Attributes:
        provider: A string indicating the LLM provider.
        llm: An instance of the LLM, which can be `ChatOpenAI`, `OpenAI`, or other compatible types.
        messages: A list of messages to be used for chat completions.
    """

    provider: str = "ChatOpenAI"
    llm: Optional[Union[ChatOpenAI, OpenAI]] = None
    messages: List[Dict[str, str]] = [
        {
            "role": "system",
            "content": "You are a helpful and friendly assistant.",
        }
    ]

    def __init__(self, **data: Any):
        super().__init__(**data)
        # Prevent passing 'provider' twice by excluding it from **data when calling create_llm
        llm_kwargs = {k: v for k, v in data.items() if k != "provider"}
        self.llm = LLMFactory.create_llm(self.provider, **llm_kwargs)

    class Config:
        arbitrary_types_allowed = True

    def chat_completion(self, user_content: str) -> Optional[str]:
        """Generates a chat completion using the configured LLM provider.

        Args:
            user_content: The user's message to which the LLM should respond.

        Returns:
            The LLM's response as a string, or None if the provider is not configured for chat completions.
        """
        if self.provider in (
            "OpenAI",
            "TogetherAI",
        ):  # Assuming TogetherAI is a typo or not implemented
            self.messages.append({"role": "user", "content": user_content})
            response = self.llm.chat.completions.create(
                model=os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo-0125"),
                messages=self.messages,
                # temperature=self.temperature,
                # max_tokens=self.max_tokens,
            )
            return response.choices[0].message.content
        return None


class LLMFactory:
    """A factory for creating LLM instances based on the provider."""

    provider_map: Dict[str, Callable[..., Union[ChatOpenAI, OpenAI]]] = {
        "ChatOpenAI": lambda **kwargs: ChatOpenAI(
            temperature=kwargs.get("temperature", 0.7),
            model_name=kwargs.get(
                "model", os.getenv("OPENAI_MODEL", "gpt-3.5-turbo-0125")
            ),
        ),
        "ChatTogetherAI": lambda **kwargs: ChatOpenAI(
            temperature=kwargs.get("temperature", 0.7),
            model_name=kwargs.get(
                "model",
                os.getenv(
                    "TOGETHER_MODEL_NAME", "mistralai/Mixtral-8x7B-Instruct-v0.1"
                ),
            ),
            openai_api_key=kwargs.get(
                "openai_api_key", os.environ.get("TOGETHER_API_KEY")
            ),
            openai_api_base=kwargs.get(
                "openai_api_base",
                os.getenv("OPENAI_API_BASE_URL", "https://api.together.xyz/v1"),
            ),
        ),
        "ChatFireworksAI": lambda **kwargs: ChatFireworks(
            fireworks_api_key=kwargs.get(
                "fireworks_api_key", os.environ.get("FIREWORKS_API_KEY")
            ),
            model=kwargs.get(
                "model",
                os.getenv(
                    "FIREWORKS_MODEL_NAME",
                    "accounts/fireworks/models/mixtral-8x7b-instruct",
                ),
            ),
            temperature=kwargs.get("temperature", 0.7),
        ),
        # "ChatMistralAI": lambda **kwargs: ChatMistralAI(
        #     mistral_api_key = kwargs.get("mistral_api_key", os.environ.get("MISTRAL_API_KEY")),
        #     model = kwargs.get("model", os.getenv("MISTRAL_MODEL_NAME", "mistral-large-latest")),
        #     temperature=kwargs.get("temperature", 0.7),
        #     kwargs = {'stream': False}
        # ),
        # "OpenAI": lambda **kwargs: OpenAI(
        #     api_key=kwargs.get("openai_api_key", os.environ.get("OPENAI_API_KEY")),
        # ),
        # "Ollama": lambda **kwargs: ChatOllama(
        #     model = kwargs.get("model", os.getenv("OLLAMA_MODEL", "gemma:2b")),
        # ),
        # "LangchainTogether": lambda **kwargs: Together(
        #     model = kwargs.get("model", os.getenv("TOGETHERAI_MODEL_NAME", "mistralai/Mixtral-8x7B-Instruct-v0.1")),
        #     together_api_key = kwargs.get("openai_api_key", os.environ.get("TOGETHER_API_KEY")),
        # ),
        # "TogetherAI": lambda **kwargs: OpenAI(
        #     # model_name=kwargs.get("model", os.getenv("OPENAI_API_KEY", 'gpt-3.5-turbo')),
        #     api_key=kwargs.get("openai_api_key", os.environ.get("TOGETHER_API_KEY")),
        #     base_url=kwargs.get(
        #         "openai_api_base", os.getenv("OPENAI_API_BASE_URL", None)
        #     ),
        # ),
    }

    @staticmethod
    def create_llm(provider: str, **kwargs: Any) -> Union[ChatOpenAI, OpenAI]:
        """Creates an LLM instance based on the specified provider.

        Args:
            provider: The name of the provider.
            **kwargs: Additional keyword arguments for the provider's constructor.

        Returns:
            An instance of the specified LLM provider.

        Raises:
            NotImplementedError: If the provider is not supported.
        """
        if provider not in LLMFactory.provider_map:
            raise NotImplementedError(f"LLM provider '{provider}' not implemented.")
        return LLMFactory.provider_map[provider](**kwargs)
