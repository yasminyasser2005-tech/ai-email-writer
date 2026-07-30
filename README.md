# AI Email Writer

## Problem
Responding to customer complaints professionally takes time and 
emotional energy, especially when the original complaint is angry, 
vague, or poorly written.

## Solution
An AI tool that takes a raw customer complaint and generates a 
polished, professional email reply acknowledging the specific issue, 
apologizing appropriately, and offering a next step, without inventing 
facts that weren't in the original message.

## Architecture
Simple, single-step prompt engineering (no retrieval or vector 
database needed here) the complaint text is passed directly to an 
LLM with a carefully constrained system prompt controlling tone, 
structure, and factual accuracy.

## Key design decisions
- Explicit instruction not to invent specific facts (refund amounts, 
  order numbers) not present in the original complaint a real 
  business risk if left unconstrained
- Apologizes without admitting legal fault, matching how real 
  customer service replies are typically worded
- Adjustable tone (professional / casual / formal) to fit different 
  business contexts

## Tech stack
Python, Streamlit, Groq API (Llama 3.3 70B)

## Demo
[Watch the demo video]https://github.com/yasminyasser2005-tech/ai-email-writer/raw/refs/heads/main/Screen%20Recording%202026-07-30%20134054.mp4
