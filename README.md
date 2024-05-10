# build_startup_using_AI_Agents
build_startup_using_AI_Agents


## Setting Up build_startup_using_AI_Agents Environment

To set up the `build_startup_using_AI_Agents` environment, follow these steps:

Note : Make sure Neo4J DB is running locally. 

1. Create a virtual environment using Python's built-in `venv` module:

    ```bash
    python -m venv build_startup_using_AI_Agents
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        build_startup_using_AI_Agents\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source build_startup_using_AI_Agents/bin/activate
        ```

3. Install dependencies 
   ```bash
   pip install -r requirements.txt
   ```
5. install ollama 
6. install mistral in ollama
   ```bash
   ollama run mistral
   ```
7. Configure model
   ```bash
   (build_startup_using_AI_Agents) ~\PycharmProjects\build_startup_using_AI_Agents>metagpt --init-config
   ```
8. Add model  at ~\.metagpt\config2.yaml
9. Let's start the debate

   ```bash
   python start_debate.py --idea="Talk about how world should develop Artificial intelligence"
   ```


