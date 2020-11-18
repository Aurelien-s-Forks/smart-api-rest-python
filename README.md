# Building AI Systems API
[![Travis CI Build](https://travis-ci.com/Building-AI-Systems/smart-api-rest-python.svg?branch=master)](https://travis-ci.com/Building-AI-Systems/smart-api-rest-python.svg?branch=master)

## Description

This API allows to retrieve data from sensors placed in a building. An artificial intelligence will process this data to optimize energy consumption, adapt the temperature in the rooms or create scenarios to predict incidents.

## Getting Started

### Run with Docker

1. Grant exec on scripts
```bash
chmod u+x docker_*
```

2. Build the Docker image
```bash
./docker_build.sh
```

3. Push the Docker image
```bash
./docker_push.sh
```

4. Run the Docker image
```bash
./docker_deploy.sh
```

5. Access the API

From here, you can access the API [here](http://api.bai-systems.cf).

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