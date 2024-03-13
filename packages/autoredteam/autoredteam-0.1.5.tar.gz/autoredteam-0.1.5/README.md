# autoredteam

Automated Red Teaming Test suite by [vijil](https://www.vijil.ai/).

## CLI calling patterns

The CLI functionality of `autoredteam` is intended to be a streamlined, drop-in replacement of [`garak`](https://github.com/leondz/garak/).
Currently, you can use it to kick off tests by either module (`--tests`) or dimension (`--dimensions`).

```
python -m autoredteam --model_type <> --model_name <> --tests <>
python -m autoredteam --model_type <> --model_name <> --dimensions <>
```
We currently support LLMs hosted on a number of model providers as agents. For a model provider, there are three possible deployment types: local model, public API, and private endpoint. Some providers offer only a subset of these deployment types.

The following table provides respective `--model_type` values for each such provider x deployment type. If a deployment type is not listed for a provider, the respective radio button should be inactive in the GUI.

| Agent | Deployment Type | `model_type`
|---|---|---|
| Anyscale | public API | `anyscale` |
| Hugging Face | public API | `huggingface` |
| | private endpoint | `huggingface.InferenceEndpoint` |
| Mistral | public API | `mistral` |
| Replicate | public API | `replicate` |
| | private endpoint | `replicate.ReplicateEndpoint` |
| OctoAI | public API | `octo` |
| | private endpoint | `octo.OctoEndpoint` |
| OpenAI | public API | `openai` |
| Together | public API | `together` |
| REST API | public API | `rest` |

When `model_type` is `rest`, a config file supplied as `model_name`, which contains the URL, API key name, and prompt and response handlers to handle input and output patterns associated with the specific URL. Example as follows

```
python -m autoredteam --model_type rest --model_name notebooks/config/together.json --tests <>
```