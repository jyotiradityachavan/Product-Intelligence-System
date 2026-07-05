import uuid

import streamlit as st

from src.graph.workflow import run_product_intelligence_graph
from src.memory.session_memory import SessionMemory
from src.utils.report_writer import create_markdown_report, save_report


st.set_page_config(
    page_title="Product Intelligence RAG System",
    page_icon="📊",
    layout="wide",
)


@st.cache_resource
def get_memory():
    return SessionMemory()


memory = get_memory()

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("Product Intelligence Multi-Agent RAG System")
st.caption("Advanced RAG + LangGraph agents + evidence-backed recommendations")


with st.sidebar:
    st.header("Controls")

    if st.button("Clear Session"):
        memory.clear(st.session_state.session_id)
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.subheader("Example Questions")
    examples = [
        "What product areas should we prioritize next quarter and why?",
        "Which customer pain points are creating the highest retention risk?",
        "What features are most important for Enterprise customers?",
        "Are we losing deals because of integrations?",
        "Generate an executive summary of customer feedback.",
    ]

    selected_example = st.selectbox(
        "Choose an example",
        [""] + examples,
    )

    use_example = st.button("Use Example Question")


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("Ask a product intelligence question...")

if use_example and selected_example:
    prompt = selected_example


if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Running multi-agent analysis..."):
            history = memory.get_history(st.session_state.session_id)
            result = run_product_intelligence_graph(prompt, history)

            answer = result["final_answer"]
            st.markdown(answer)

            with st.expander("Research Notes"):
                st.markdown(result["research_notes"])

            with st.expander("Validation Notes"):
                st.markdown(result["validation_notes"])

            with st.expander("Retrieved Sources"):
                for index, doc in enumerate(result["retrieved_docs"], start=1):
                    source = doc.metadata.get("source", "unknown")
                    st.markdown(f"**Source {index}:** `{source}`")
                    st.write(doc.page_content[:800])

            report = create_markdown_report(
                query=prompt,
                final_answer=result["final_answer"],
                research_notes=result["research_notes"],
                validation_notes=result["validation_notes"],
                recommendations=result["recommendations"],
            )

            report_path = save_report(report)

            st.download_button(
                label="Download Executive Report",
                data=report,
                file_name="executive_report.md",
                mime="text/markdown",
            )

            st.caption(f"Report also saved locally: {report_path}")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    memory.add_turn(
        st.session_state.session_id,
        prompt,
        answer,
    )
