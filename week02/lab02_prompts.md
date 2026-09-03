# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticated the tool, GitHub Copilot CLI 1.0.82 

### Antigravity CLI

I installed and authenticated the tool, agy --version 1.1.24


## Shared task

### Shared prompt
```text
Write a Python function count_vowels(text: str) -> int that counts the number of vowels a, e, i, o, and u in the given text, ignoring case. Do not count the letter y as a vowel. The function should return an integer.
```
### Copilot CLI observations
  Copilot CLI inspected the repository and implemented count_vowels as a compact expression using sum(). For each character, it converted the character to lowercase and checked whether it was contained in the string "aeiou". This approach handles uppercase and lowercase vowels and does not count y because y is not included in the vowel string. 

### Antigravity CLI observations
Antigravity CLI suggested a slightly more structured implementation using a set of vowels and a generator expression. It emphasized clarity by including a docstring and explaining each step. The use of a set provides faster membership checks, and the logic correctly excludes 'y'. I questioned whether the set or the string approach was more efficient, but both are correct. I would verify behavior on edge cases such as empty strings, uppercase input, and strings containing non alphabetic characters.

### Comparison
 Both CLI tools produced correct implementations of count_vowels, but their styles differed. Copilot CLI returned a very compact one line solution using sum(char.lower() in "aeiou" for char in text). This version is concise and easy to read, but it relies on a string for membership checks. Antigravity CLI used a set, which is slightly more explicit and efficient for repeated membership testing. It also included a detailed docstring and explanation, which made the reasoning clearer. Both approaches ignore case and correctly exclude 'y'. I chose the Antigravity version because it is more explicit and aligns better with typical Python style guides, but either implementation would pass the tests.

## Test-guided implementation
After selecting an implementation, I ran the provided tests using uv run --directory week02 python -m pytest tests/ -v. The tests checked behavior on lowercase, uppercase, empty strings, and strings containing non vowel characters. My initial implementation passed all tests, but I still manually inspected the logic to ensure it matched the function contract exactly. The contract requires counting only a, e, i, o, u and ignoring case, while excluding y. The final code uses a lowercase conversion and a vowel set, which satisfies all requirements. No revisions were needed after testing, and the behavior matched both the prompt and the test expectations

## Preferred tool combination
 In my workflow, each tool serves a different purpose. Copilot in VS Code is convenient for quick inline suggestions while editing files. Copilot CLI is useful when I want to test prompts inside the repository context and see how the agent interprets local files. Antigravity CLI provides more structured explanations and sometimes clearer reasoning. Browser chat is helpful when I need longer explanations or want to explore alternative approaches. Currently, I prefer using VS Code Copilot plus Copilot CLI because they integrate smoothly with my editor. However, if I need more detailed reasoning or want to compare multiple approaches, I might switch to Antigravity CLI.
