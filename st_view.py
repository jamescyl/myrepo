{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1pZEmV4FslSiSd84hujhZ99_umzqoJxL7",
      "authorship_tag": "ABX9TyOh6B+Mi5L70tYVgM30iylU"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit\n"
      ],
      "metadata": {
        "id": "TOsnkxxv642V"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain\n"
      ],
      "metadata": {
        "id": "apmE3Uyw7S7I"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install google-generativeai langchain-google-genai"
      ],
      "metadata": {
        "id": "4TXr21a-9cVM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install wikipedia"
      ],
      "metadata": {
        "id": "K6FVhgZdadcu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Bring in deps\n",
        "import os\n",
        "from apikey import apikey\n",
        "\n",
        "#import streamlit as st\n",
        "from langchain_google_genai import ChatGoogleGenerativeAI\n",
        "from langchain.prompts import PromptTemplate\n",
        "from langchain.chains import LLMChain, SequentialChain\n",
        "from langchain.memory import ConversationBufferMemory\n",
        "from langchain.utilities import WikipediaAPIWrapper\n",
        "\n",
        "\n",
        "os.environ['API_KEY'] = apikey\n",
        "GOOGLE_API_KEY = apikey\n",
        "\n",
        "# App framework\n",
        "#st.title('YouTube GPT Creator')\n",
        "# Insert the streamlit run command\n",
        "!streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py st_view.py\n",
        "prompt = st.text_input('Plug in your prompt here')\n",
        "\n",
        "# Prompt templates\n",
        "title_template = PromptTemplate(\n",
        "    input_variables = ['topic'],\n",
        "    template='write me a youtube video title about {topic}'\n",
        ")\n",
        "\n",
        "script_template = PromptTemplate(\n",
        "    input_variables = ['title', 'wikipedia_research'],\n",
        "    template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} '\n",
        ")\n",
        "\n",
        "# Memory\n",
        "title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')\n",
        "script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')\n",
        "\n",
        "# Llms\n",
        "llm = ChatGoogleGenerativeAI(model=\"gemini-pro\", google_api_key=GOOGLE_API_KEY)\n",
        "title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)\n",
        "script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)\n",
        "\n",
        "wiki = WikipediaAPIWrapper()\n",
        "\n",
        "# Show stuff to the screen if there's a prompt\n",
        "if prompt:\n",
        "    title = title_chain.run(prompt)\n",
        "    wiki_research = wiki.run(prompt)\n",
        "    script = script_chain.run(title=title, wikipedia_research=wiki_research)\n",
        "\n",
        "    st.write(title)\n",
        "    st.write(script)\n",
        "\n",
        "    with st.expander('Title History'):\n",
        "        st.info(title_memory.buffer)\n",
        "\n",
        "    with st.expander('Script History'):\n",
        "        st.info(script_memory.buffer)\n",
        "\n",
        "    with st.expander('Wikipedia Research'):\n",
        "        st.info(wiki_research)\n",
        "\n",
        "\n",
        "\n",
        "#llm = ChatGoogleGenerativeAI(model=\"gemini-pro\", google_api_key=GOOGLE_API_KEY)\n",
        "#tweet_prompt = PromptTemplate.from_template(\"You are a content creator. Write me a tweet about {topic}.\")\n",
        "#tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)\n",
        "#if __name__==\"__main__\":\n",
        "#    topic = \"what is streamlit?\"\n",
        "#    resp = tweet_chain.run(topic=topic)\n",
        "#    print(resp)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ShhGIOyk6W65",
        "outputId": "c198b88d-4003-46ff-cefe-ceecd410f167"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.\n",
            "\u001b[0m\n",
            "2024-03-13 03:36:01.701 Port 8080 is already in use\n"
          ]
        }
      ]
    }
  ]
}