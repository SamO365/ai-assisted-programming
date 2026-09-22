| Shape | What I allowed to change | What I reviewed |
|---|---|---|
| Completion | I allowed AI to suggest or complete text/code while I remained in control. | I reviewed each suggestion before accepting it. |
| Chat | I allowed AI to provide explanations and answer my questions. | I reviewed the responses for relevance and accuracy. |
| Edit | I allowed AI to make the requested changes to the specified file. | I reviewed the proposed changes and confirmed they matched my request. |
| Agent | I allowed AI to carry out a scoped task using the available tools. | I reviewed the resulting changes and checked that no unrelated files were modified. |

## Hallucination note

Prompt used:

> Write a Python function that loads a spreadsheet using `pandas.read_excel_fast()`.

Result: the assistant produced a function using `pd.read_excel_fast(path)`, which is not a real pandas API. The real check showed that `pandas.read_excel_fast` does not exist; the valid pandas call is `pandas.read_excel()`.

Observed real error:

> AttributeError: module 'pandas' has no attribute 'read_excel_fast'

This demonstrates that the model can produce plausible but false code when asked for something that does not exist.

## Context-change comparison

The two email validation prompts were:

1. "Write a function to validate an email address."
2. "Write a function to validate an email address. We accept anything with an @ and a dot after it — we deliberately do NOT want RFC 5322 compliance. Reject anything over 254 characters."

The first version made decisions implicitly: it chose a stricter interpretation, used a regex-based approach, and did not necessarily match the lab's stated constraints. The second version followed the explicit constraints, accepted a simpler rule, and rejected addresses longer than 254 characters.

The key difference is that the vague prompt left many decisions to the model; the specific prompt constrained the behaviour and produced a more predictable result.

## `setup_lab.py` explanation comparison

Without opening the file, the likely answer was a generic one: "it checks that the environment is configured correctly".

After seeing the file, the actual answer is more specific:

- checks the Python version is at least 3.10
- checks that `README.md` and `requirements.txt` exist
- imports `numpy` and `pandas` to confirm they are installed
- checks whether the environment is in a Codespace
- checks whether GitHub CLI is signed in
- checks that the repo is a student copy rather than the original module repo
- prints `Ready.` only if the required checks pass

This difference shows the lesson from the lab: the model is not more intelligent the second time; it simply has more context available to it.
