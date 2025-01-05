from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


class LLMProcessor:
    def __init__(self, model_path: str, model_type: str = "mistral"):
        """
        Initialize the LLM model based on the selected type.
        """
        if model_type == "mistral":
            print("Using Mistral model...")
        else:
            raise ValueError(f"Unsupported model type: {model_type}")

        # Load the model
        self.llm = LlamaCpp(
            model_path=model_path,
            n_ctx=2048,
            temperature=0.3,
            max_tokens=500,
            n_threads=4,
            verbose=False
        )

    def clean_transcription(self, text: str) -> str:
        """
        Clean transcription using the selected LLM.
        """
        prompt = PromptTemplate(
            template=(
                "Clean the following subtitles by removing timestamps, duplicates, "
                "and formatting artifacts. Merge fragmented lines into coherent sentences:\n\n"
                "{text}\n\nCleaned Text:"
            ),
            input_variables=["text"],
        )
        chain = LLMChain(prompt=prompt, llm=self.llm)
        return chain.run(text)