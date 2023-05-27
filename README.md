# Comwork AI

Comwork AI API that bring all the AI models you want as an API using a ModelDriver's abstract:

```python
class ModelDriver(ABC):
    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def generate_response(self, prompt: Prompt):
        pass
```

This API is also used as an internal component for Comwork Cloud, more details here: https://doc.cloud.comwork.io/docs/tutorials/cwai

## Git repositories

* Main repo: https://gitlab.comwork.io/oss/cwai/cwai-api.git
* Github mirror: https://github.com/idrissneumann/cwai-api.git
* Gitlab mirror: https://gitlab.com/ineumann/cwai-api.git

## Getting started in local

## Prepare configurations

```shell
cp .env.dist .env # replace your variables in the .env file you just created
```

## Run the containers

```shell
docker-compose -f docker-compose-local.yml up --build --force-recreate
```

Then you can open http://localhost:8000 and test the API via Swagger.

## Models

* GPT2
* Bloom (beware it'll take more than 300Gb of storage)
* bert-base-multilingual-uncased-sentiment

In order to avoid downloading to much data, you can override the list of the models with this variable:

```
ENABLED_MODELS='["gpt2", "mock"]'
```

For example here, we only load the 500mb of data coming from GPT2
