from __future__ import annotations

from prompt.rewrite_sentences import REWRITE_SENTENCES


class PromptGenerator:
    def generate_rewrite_sentences_prompt(
        self,
        sentences: list[str],
    ):
        _sentences = '<break>'.join([
            sentence.strip()
            for sentence in sentences
        ])
        prompt = REWRITE_SENTENCES['instruction'] +\
            REWRITE_SENTENCES['examples'] +\
            REWRITE_SENTENCES['sentences'].format(sentences={_sentences})
        return prompt
