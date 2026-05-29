# Spatial AI Modeling System

Human-in-the-loop Workflow for Space Product Prototyping and Generative Modeling

空间 AI 建模系统：面向空间产品原型与生成式建模的人机协同工作流

## One-line summary

An AI-assisted spatial modeling workflow that converts site data, spatial rules, and design intent into verifiable Rhino/Grasshopper prototypes through modular GH Python cells, JSON rules, building generator patterns, and human validation.

## Problem

AI can generate code quickly, but spatial modeling workflows often fail when data, rules, GH components, facade logic, and visual judgment are mixed together. The result can be unstable geometry, missing breps, mismatched outputs, and unclear preview behavior.

## Approach

The system decomposes the workflow into data, rules, GH cells, generators, validation, AI prompts, and GitHub packaging. Codex handles structured data, first-pass code, validators, and documentation. ChatGPT supports building generator logic and visual debugging prompts. Rhino/GH and human judgment validate the final output.

## Tools

- Python
- JSON Schema
- Grasshopper Python
- RhinoCommon
- Rhino/GH
- Codex
- ChatGPT
- GitHub

## Outcome

The project is a reusable system for AI-assisted spatial modeling, not a fully autonomous architecture generator. It demonstrates product thinking, workflow design, and practical computational design validation.

