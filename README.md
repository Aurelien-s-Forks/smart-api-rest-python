# Building AI Systems API

## Description

This API allows to retrieve data from sensors placed in a building. An artificial intelligence will process this data to optimize energy consumption, adapt the temperature in the rooms or create scenarios to predict incidents.

## Getting Started

### Run with Docker

1. Build the Docker image
```bash
docker build -t riipeckx/bai-systems-smart-api-rest-python:latest .
```

2. Push the Docker image
```bash
docker push riipeckx/bai-systems-smart-api-rest-python:latest
```

3. Run the Docker image
```bash
chmod u+x docker_deploy.sh docker_stop.sh docker_restart.sh && ./docker_deploy.sh
```

### Installation

1. Clone the repo
```sh
git clone git@github.com:Building-AI-Systems/smart-api-rest-python.git
```

2. Install Python >= 2.7.0

[Python Download](https://www.python.org/downloads/)

3. Install requirements

```bash
pip install requirements.txt 
```

## Usage

To edit the project you can open it at its root with any IDE like IntelliJ IDEA, PyCharm or VSCode.

This project is fully coded with Python so you must have the base knowledges to edit it.

## Roadmap

See the [open issues](https://github.com/Building-AI-Systems/smart-api-rest-python/issues) for a list of proposed features (and known issues).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/myFeature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/myFeature`)
5. Open a Pull Request

## License
[MIT](https://choosealicense.com/licenses/mit/)