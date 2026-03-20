#!/usr/bin/env node
/**
 * Gemini CLI wrapper — calls Gemini via Google AI SDK.
 *
 * Simple mode:
 *   node scripts/gemini.mjs "your prompt here"
 *   echo "prompt" | node scripts/gemini.mjs --stdin
 *   node scripts/gemini.mjs --file path/to/prompt.txt
 *   node scripts/gemini.mjs --system "you are a medical expert" "your prompt"
 *
 * QA visual mode (multimodal):
 *   node scripts/gemini.mjs \
 *     --slide s-hook \
 *     --file aulas/metanalise/slides/01-hook.html \
 *     --png qa-screenshots/static/s-hook/s0.png \
 *     --mp4 qa-screenshots/videos/s-hook.mp4 \
 *     --json
 *
 * Output: .audit/{slide-id}_result.json (auto-save when --slide)
 *
 * Env: GEMINI_API_KEY must be set.
 */

import { GoogleGenerativeAI } from "@google/generative-ai";
import { readFileSync, writeFileSync, existsSync, mkdirSync } from "fs";
import { resolve, extname, join } from "path";

const MODEL = "gemini-3.1-pro-preview";
const QA_PROMPT_TEMPLATE = "docs/prompts/gemini-slide-qa.md";
const AUDIT_DIR = ".audit";

function usage() {
  console.error(`Usage:
  node scripts/gemini.mjs "prompt"
  node scripts/gemini.mjs --system "system instruction" "prompt"
  node scripts/gemini.mjs --file prompt.txt
  echo "prompt" | node scripts/gemini.mjs --stdin
  node scripts/gemini.mjs --json "prompt"          (force JSON output)
  node scripts/gemini.mjs --temp 0.3 "prompt"      (set temperature)

  QA visual (multimodal):
  node scripts/gemini.mjs --slide s-hook --file slide.html --png screenshot.png --mp4 video.mp4 --json`);
  process.exit(1);
}

function readBase64(filePath) {
  const abs = resolve(filePath);
  if (!existsSync(abs)) {
    console.error(`ERROR: File not found: ${abs}`);
    process.exit(1);
  }
  return readFileSync(abs).toString("base64");
}

function mimeFromExt(filePath) {
  const ext = extname(filePath).toLowerCase();
  const map = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".mp4": "video/mp4",
    ".webm": "video/webm",
  };
  return map[ext] || "application/octet-stream";
}

function loadQaPrompt(slideHtml, slideId) {
  const templatePath = resolve(QA_PROMPT_TEMPLATE);
  if (!existsSync(templatePath)) {
    console.error(`ERROR: QA prompt template not found: ${templatePath}`);
    process.exit(1);
  }
  const template = readFileSync(templatePath, "utf-8");

  // Extract the prompt block between ~~~ markers
  const match = template.match(/~~~\n([\s\S]*?)\n~~~/);
  const prompt = match ? match[1] : template;

  // Inject available variables
  return prompt
    .replace(/\{\{SLIDE_ID\}\}/g, slideId)
    .replace(/\{\{RAW_HTML\}\}/g, slideHtml);
}

function saveAudit(slideId, content) {
  if (!existsSync(AUDIT_DIR)) mkdirSync(AUDIT_DIR, { recursive: true });
  const outPath = join(AUDIT_DIR, `${slideId}_result.json`);
  writeFileSync(outPath, content, "utf-8");
  console.error(`Saved → ${outPath}`);
}

async function readStdin() {
  const chunks = [];
  for await (const chunk of process.stdin) chunks.push(chunk);
  return Buffer.concat(chunks).toString("utf-8").trim();
}

async function main() {
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    console.error("ERROR: GEMINI_API_KEY not set in environment.");
    process.exit(1);
  }

  const args = process.argv.slice(2);
  if (args.length === 0) usage();

  let prompt = "";
  let systemInstruction = undefined;
  let temperature = undefined;
  let jsonMode = false;
  let slideId = null;
  let filePath = null;
  const pngPaths = [];
  let mp4Path = null;

  // Parse args
  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case "--stdin":
        prompt = await readStdin();
        break;
      case "--file":
        filePath = args[++i];
        break;
      case "--system":
        systemInstruction = args[++i];
        break;
      case "--json":
        jsonMode = true;
        break;
      case "--temp":
        temperature = parseFloat(args[++i]);
        break;
      case "--slide":
        slideId = args[++i];
        break;
      case "--png":
        pngPaths.push(args[++i]);
        break;
      case "--mp4":
        mp4Path = args[++i];
        break;
      case "--help":
      case "-h":
        usage();
        break;
      default:
        prompt = args[i];
    }
  }

  // QA visual mode: --slide triggers multimodal with template
  const qaMode = slideId !== null;

  if (qaMode) {
    if (!filePath) {
      console.error("ERROR: QA mode (--slide) requires --file with slide HTML.");
      process.exit(1);
    }
    const slideHtml = readFileSync(resolve(filePath), "utf-8");
    prompt = loadQaPrompt(slideHtml, slideId);
    if (!temperature) temperature = 1.0;
    if (!jsonMode) jsonMode = true;
  } else if (filePath) {
    // Simple mode: --file is the prompt itself
    prompt = readFileSync(resolve(filePath), "utf-8").trim();
  }

  if (!prompt) {
    console.error("ERROR: No prompt provided.");
    usage();
  }

  const genAI = new GoogleGenerativeAI(apiKey);

  const modelConfig = { model: MODEL };
  if (systemInstruction) modelConfig.systemInstruction = systemInstruction;

  const model = genAI.getGenerativeModel(modelConfig);

  const generationConfig = {};
  if (temperature !== undefined) generationConfig.temperature = temperature;
  if (jsonMode) generationConfig.responseMimeType = "application/json";

  // Build content parts
  const parts = [{ text: prompt }];

  // Attach PNGs
  for (const png of pngPaths) {
    parts.push({
      inlineData: {
        mimeType: mimeFromExt(png),
        data: readBase64(png),
      },
    });
  }

  // Attach MP4
  if (mp4Path) {
    parts.push({
      inlineData: {
        mimeType: mimeFromExt(mp4Path),
        data: readBase64(mp4Path),
      },
    });
  }

  const result = await model.generateContent({
    contents: [{ role: "user", parts }],
    generationConfig,
  });

  const text = result.response.text();

  // Auto-save when in QA mode
  if (qaMode) {
    saveAudit(slideId, text);
  }

  process.stdout.write(text);
  if (!text.endsWith("\n")) process.stdout.write("\n");
}

main().catch((err) => {
  console.error("Gemini API error:", err.message || err);
  process.exit(1);
});
