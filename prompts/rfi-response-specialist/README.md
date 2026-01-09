# GovRFI-Response-Specialist — Git Kit

This repo kit gives you everything you need to create and configure the Custom GPT in ChatGPT.
There is no official "import GPT from YAML" function in ChatGPT today; you will *paste* the
instructions and optionally upload templates/knowledge files.

## Contents
- gpt/govrfi-response-specialist.gpt.yaml
  - Repo-storable spec (what the GPT is and how it should behave)
- gpt/system_instructions.txt
  - Paste this into ChatGPT → Create GPT → Configure → Instructions
- templates/RFI-DOSSIER-TEMPLATE.md
  - Upload to GPT Knowledge (recommended authoritative dossier format)
- templates/RFI-DOSSIER-TEMPLATE.yaml
  - Optional structured dossier format if you want automation later
- examples/
  - Samples you can adapt (placeholders; add your own content)

## Create the GPT in ChatGPT (manual, fast)
1) ChatGPT → Explore GPTs → Create
2) Configure:
   - Name: GovRFI-Response-Specialist
   - Description: see the YAML spec
3) Paste the contents of `gpt/system_instructions.txt` into Instructions
4) Enable:
   - File uploads: ON
   - Advanced Data Analysis: ON
   - Web browsing: ON
5) Knowledge (persistence):
   - Upload `templates/RFI-DOSSIER-TEMPLATE.md`
   - For each live RFI, create `RFI-<SolicitationNumber>-DOSSIER.md` from that template and upload it too.
     That dossier becomes the source of truth across multi-day chats.

## Operating discipline (non-negotiable)
- One RFI = one dossier file.
- Keep the dossier current. If it's wrong, your response will be wrong.
- Start each session with: "Load the RFI dossier from knowledge and give me a context reload."

## Suggested repo layout
- Commit this kit as-is, then create a folder per RFI under `rfi/` and store:
  - the RFI notice
  - attachments
  - your dossier file
  - draft versions

## License
Internal use.
