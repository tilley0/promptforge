#!/usr/bin/env python
from __future__ import annotations

import os
import json
from pathlib import Path
from typing import Optional

import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from tenacity import retry, stop_after_attempt, wait_exponential

app = typer.Typer(no_args_is_help=True)
console = Console()

def read_yaml(path: Path) -> dict:
    try:
        import yaml  # type: ignore
    except Exception:
        typer.echo("PyYAML not found. Install with: pip install pyyaml")
        raise typer.Exit(code=1)
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def resolve_model(provider: str, cfg: dict) -> str:
    if provider == "openai":
        return cfg.get("model") or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    if provider == "anthropic":
        return cfg.get("model") or os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-latest")
    return cfg.get("model") or "gpt-4o-mini"

@retry(wait=wait_exponential(multiplier=1, min=1, max=8), stop=stop_after_attempt(3))
def call_openai(model: str, system_prompt: str, message: str) -> str:
    from openai import OpenAI
    client = OpenAI()
    rsp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
    )
    return rsp.choices[0].message.content or ""

@retry(wait=wait_exponential(multiplier=1, min=1, max=8), stop=stop_after_attempt(3))
def call_anthropic(model: str, system_prompt: str, message: str) -> str:
    import anthropic
    client = anthropic.Client()
    rsp = client.messages.create(
        model=model,
        max_tokens=800,
        system=system_prompt,
        messages=[{"role": "user", "content": message}],
    )
    return "".join(block.text for block in rsp.content if getattr(block, "text", None))

@app.command()
def main(
    config: Path = typer.Option(Path("configs/example_agent.yaml"), "--config", "-c", exists=True),
    message: str = typer.Option(..., "--message", "-m", help="User message to send"),
    provider: Optional[str] = typer.Option(None, "--provider", "-p", help="openai|anthropic"),
) -> None:
    """
    Minimal single-turn chat runner for smoke testing providers and models.
    """
    load_dotenv()

    cfg = read_yaml(config)
    provider = (provider or os.getenv("PROVIDER") or cfg.get("provider") or "openai").lower()
    system_prompt = cfg.get("system_prompt", "You are a helpful AI assistant.")
    model = resolve_model(provider, cfg)

    console.print(Panel.fit(f"[bold]promptforge[/bold] • provider=[cyan]{provider}[/cyan] • model=[magenta]{model}[/magenta]"))
    console.print(f"[bold]System:[/bold] {system_prompt}")
    console.print(f"[bold]User:[/bold] {message}")

    try:
        if provider == "anthropic":
            output = call_anthropic(model, system_prompt, message)
        else:
            output = call_openai(model, system_prompt, message)
    except Exception as e:
        console.print(f"[red]Provider call failed:[/red] {e}")
        raise typer.Exit(code=1)

    console.rule("Assistant")
    console.print(output.strip())
    console.rule()

    # Emit a minimal JSON artifact to experiments/
    out_dir = Path("experiments")
    out_dir.mkdir(parents=True, exist_ok=True)
    artifact = {
        "provider": provider,
        "model": model,
        "system": system_prompt,
        "message": message,
        "output": output,
    }
    (out_dir / "last_run.json").write_text(json.dumps(artifact, indent=2), encoding="utf-8")
    console.print(f"[green]Saved:[/green] experiments/last_run.json")

if __name__ == "__main__":
    app()
