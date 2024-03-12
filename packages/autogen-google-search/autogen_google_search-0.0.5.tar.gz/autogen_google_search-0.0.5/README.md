A tool that integrates the autogen with Google Searcher.



Using AutoGen to achieve multi-agent integration with Google Search, it can serve as a function in the Tools for other agents to use, enabling seamless integration with LangChain.



Create a file named OAI_CONFIG_LIST in the current directory with the following content format:
```
[
    {
        "model": "gpt-3.5-turbo",
        "api_key": "sk-xxxx"
    },
    {
        "model": "gpt-4",
        "api_key": "sk-xxxx",
        "base_url": "xxxx"
    }
]
```