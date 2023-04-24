import openai

class SQL_Traslator:
    def __init__(self, api_key) -> None:
        openai.api_key = api_key
        self._creation_db_script = ""

    def convert_to_sql(self, text_for_query: str):  
        completion = openai.Completion.create(engine="text-davinci-003",
                                            prompt="Conviérteme a un SELECT en sql la siguiente petición:" + text_for_query + "\n, Dentro de una base de datos creada con el siguiente script: " + self._creation_db_script,
                                            max_tokens=100)
        return completion.choices[0].text