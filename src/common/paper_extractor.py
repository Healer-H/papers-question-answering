from __future__ import annotations

import json
import logging

import nltk
import regex as re
from dotenv import load_dotenv
from groq import Groq
from langchain_community.document_loaders import PDFMinerLoader
from langchain_core.documents import Document
from openai import OpenAI
from prompt.prompt_generator import PromptGenerator

nltk.download('punkt_tab')
load_dotenv()
openai_client = OpenAI()
groq_client = Groq()


class PaperExtractor:
    def __init__(
        self,
    ):
        self.prompt_generator = PromptGenerator()

    def preprocess_text(
        self,
        text: str,
    ) -> str:

        _text = re.sub(r'-\s+', '', text)
        _text = re.sub(r'^.\n', '', _text, flags=re.MULTILINE)
        _text = _text.replace('\n\n', '\n')

        return _text

    def _split_text_by_keywords(
        self,
        text: str,
        keywords: list[str],
    ) -> list[str]:
        split_pattern = '|'.join(map(re.escape, keywords))
        split_texts = re.split(split_pattern, text, flags=re.IGNORECASE)
        return split_texts

    def split_text_by_keywords(
        self,
        text: str,
    ) -> list[str]:
        with open('split_words.txt') as f:
            split_words = f.readlines()
        split_words = [word.strip() for word in split_words]

        return self._split_text_by_keywords(text, split_words)

    def split_text_by_sentences(
        self,
        text: str,
    ) -> list[str]:
        split_texts = nltk.sent_tokenize(text)
        split_texts = [text.strip() for text in split_texts]
        split_texts = [re.sub(r'\n', ' ', text) for text in split_texts]
        return split_texts

    def _extract_json_object(
        self,
        text: str,
    ):
        """
        Extracts a single JSON object from a given text string
            and parses it into a Python dictionary.

        :param text: The input string containing a JSON object.
        :return: A Python dictionary representing the extracted
            JSON object, or None if no valid JSON is found.
        """
        # Regular expression to match a JSON object
        json_pattern = r'\{(?:[^{}]|(?))*\}'

        # Find the first JSON object in the text
        match = re.search(json_pattern, text)

        if match:
            json_str = match.group(0)
            try:
                parsed_obj = json.loads(json_str)
                return parsed_obj
            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse JSON object: {
                              json_str
                              }. Error: {e}")
                return None
        else:
            logging.info('No JSON object found in the text.')
            return []

    def _extract_json_objects(
        self,
        text: str,
    ) -> list[dict]:
        """
        Extracts JSON objects from a given text string
            and parses them into Python dictionaries.

        :param text: The input string containing JSON objects.
        :return: A list of Python dictionaries representing
            the extracted JSON objects.
        """
        # Regular expression to match JSON objects
        json_pattern = r'\{(?:[^{}]|(?R))*\}'

        # Find all JSON objects in the text
        json_objects = re.findall(json_pattern, text)

        # Parse JSON strings into Python dictionaries
        parsed_objects = []
        for obj in json_objects:
            try:
                parsed_obj = json.loads(obj)
                parsed_objects.append(parsed_obj)
            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse JSON object: {
                              obj
                              }. Error: {e}")

        return parsed_objects

    def _rewrite_sentences_by_llm(
        self,
        sentences: list[str],
        batch_size: int = 16,
        model='gemma2-9b-it',
    ) -> list[str]:
        start = 0
        rewrited_sentences = []
        while True:
            batch_sentences = sentences[
                start:min(
                    start + batch_size, len(sentences),
                )
            ]

            # Generate the prompt
            prompt = self.prompt_generator.generate_rewrite_sentences_prompt(
                sentences=batch_sentences,
            )

            chat_completion = groq_client.chat.completions.create(
                messages=[
                    {
                        'role': 'user',
                        'content': prompt,
                    },
                ],
                model=model,
            )
            try:
                rewrited_sentences_batch = self._extract_json_objects(
                    chat_completion.choices[0].message.content,
                )[0].get('sentences', [])
            except (IndexError, TypeError):
                rewrited_sentences_batch = []

            rewrited_sentences_batch = [
                sentence.get(
                    'text',
                ) for sentence in rewrited_sentences_batch
            ]
            rewrited_sentences.extend(rewrited_sentences_batch)

            start += batch_size
            if start >= len(sentences):
                break
        return rewrited_sentences

    def _get_embedding(self, text, model='text-embedding-3-small'):
        text = text.replace('\n', ' ')
        return openai_client.embeddings.\
            create(input=[text], model=model).data[0].embedding

    def load_content(self, path) -> list[Document]:
        document_loader = PDFMinerLoader(path)
        document = document_loader.load()
        preprocessed_text = self.preprocess_text(document[0].page_content)
        sentences = self.split_text_by_sentences(preprocessed_text)
        rewrited_sentences = self._rewrite_sentences_by_llm(sentences)
        return rewrited_sentences
