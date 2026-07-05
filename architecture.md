# Architecture

## Overview

The Product Intelligence System is a Minimum Viable Product demonstrating advanced Retrieval-Augmented Generation, multi-agent workflows, memory-aware conversation, and executive report generation.

The system ingests product-related documents such as customer support tickets, feature requests, PRDs, meeting notes, GitHub issues, and competitor analysis. It stores embedded document chunks in Chroma and uses LangGraph to coordinate specialized agents.

## Architecture Diagram

```mermaid
flowchart TD
    A[Product Documents] --> B[Document Loaders]
    B --> C[Text Splitter]
    C --> D[Embedding Model]
    D --> E[Chroma Vector Store]

    U[User Query] --> G[LangGraph Supervisor Workflow]
    M[Session Memory] --> G
    E --> R[Researcher Agent]
    G --> R

    R --> C1[Critic Validator Agent]
    C1 --> S[Summarizer Agent]
    S --> REC[Recommender Agent]
    REC --> O[Final Answer]

    REC --> REP[Executive Report Generator]
    O --> UI[Streamlit UI]
    REP --> UI
