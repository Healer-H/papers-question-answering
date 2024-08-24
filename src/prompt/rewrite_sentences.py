from __future__ import annotations
instruction = """
You are tasked with rewriting a batch of sentences to improve clarity and focus. Follow these steps for each sentence in the batch:

1. Extract Key Information: For each sentence, identify and extract the most important words and the main topic. These should be words that allow others to easily understand the core subject of the sentence.

2. Remove Redundant Words: Identify any words within each sentence that are irrelevant, meaningless, or unnecessary for understanding the sentence's topic. Remove these words.

3. Rewrite the Sentence: Using the key information extracted, rewrite each sentence to be concise and focused. Ensure that all unnecessary words are removed, and the rewritten sentence clearly conveys the intended meaning.

Input Format:
The input will be provided within `<sentences>` and `</sentences>` tags, with each tag on a separate line. There will be multiple sentences between these tags, with each sentence is splited by a <break> tag.

Expected Output Format: Your response should be formatted as a JSON object with the key "sentences". The value should be a list of dictionaries, where each dictionary includes:

    "idx": The index of the sentence within the batch.
    "text": The revised sentence following the criteria above.

Constraints:
- Do not create new content or make assumptions beyond the provided information. If certain parts of a sentence are unclear or unfamiliar, leave them as they are.
- Output Requirement: The output must be a JSON object without any additional explanations or text.
"""

examples = """
Example:

Given Input (Batch Size: 2):
<sentences>
Efficient Retriever for Multi-Hop Question Answering Ziyuan Zhuang1∗, Zhiyang Zhang1∗, Sitao Cheng1, Fangkai Yang2, Jia Liu1, Shujian Huang1, Qingwei Lin2, Saravan Rajmohan2, Dongmei Zhang2, Qi Zhang2 1 State Key Laboratory for Novel Software Technology, Nanjing University, China 2 Microsoft ziyuan.zhuang@smail.nju.edu.cn<break>Scalable Neural Methods for Reasoning Over Logic Rules in Natural Language Processing Smith A., John B., University of Oxford, UK john.smith@oxford.ac.uk
</sentences>

Step 1: Extract key information for each sentence:
- Sentence 1: "Retriever", "Multi-Hop Question Answering"
- Sentence 2: "Scalable Neural Methods", "Reasoning Over Logic Rules", "Natural Language Processing"

Step 2: Remove unnecessary words:
- Sentence 1: "Ziyuan Zhuang1∗", "Sitao Cheng1", "ziyuan.zhuang@smail.nju.edu.cn", etc. (Personal names and emails)
- Sentence 2: "Smith A.", "John B.", "john.smith@oxford.ac.uk", etc. (Personal names and emails)

Step 3: Rewrite the sentences:
- Sentence 1: "Efficient Retriever for Multi-Hop Question Answering"
- Sentence 2: "Scalable Neural Methods for Reasoning Over Logic Rules in NLP"

Expected JSON Output:
```
{
  "sentences": [
    {
      "idx": 1,
      "text": "Efficient Retriever for Multi-Hop Question Answering"
    },
    {
      "idx": 2,
      "text": "Scalable Neural Methods for Reasoning Over Logic Rules in NLP"
    }
  ]
}
"""

sentences = """
Now is your turn
Input:

<sentences>
{sentences}
</sentences>

Response:
"""

REWRITE_SENTENCES = {
    'instruction': instruction,
    'examples': examples,
    'sentences': sentences,
}
