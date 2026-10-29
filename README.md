# Autonomous ML Lab: Free local Llama agent

Daily GitHub coding agent using **Ollama + Llama 3.2 3B** on your Windows computer. No paid model API key.

## Windows setup

1. Install Ollama from https://ollama.com/download/windows
2. In PowerShell run: `ollama pull llama3.2:3b`
3. Check Ollama is running: `ollama list`
4. In GitHub repository Settings > Actions > Runners > New self-hosted runner, choose Windows x64. Follow GitHub's PowerShell commands to download, configure, and start the runner. When configuring, add the label `ml-lab`. Keep the runner online during the scheduled run.
5. Under Settings > Actions > General, enable read/write workflow permissions and allow Actions to create pull requests.
6. Under Actions, run **Daily ML Agent** manually once.

The workflow runs daily at 16:17 UTC, 9:17 AM PDT or 8:17 AM PST. A sleeping or offline desktop cannot execute the workflow. Scheduled GitHub runs can be delayed.

## Safety

This public repository uses a self-hosted runner. Never run untrusted pull request workflows on it. Do not enable automatic merges. Keep the runner on a separate, minimally privileged Windows account, ideally in a disposable VM. This workflow compiles generated Python for syntax only and does not run generated project code. Review generated code before executing it.

Ollama uses your local CPU/GPU and disk space. It does not require OpenAI API billing.
